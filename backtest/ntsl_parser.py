import re
import ast
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass

@dataclass
class NTSLStrategy:
    """Representa uma estratégia NTSL parseada"""
    name: str
    magic_number: int
    inputs: Dict[str, Any]
    variables: Dict[str, Any] 
    functions: Dict[str, str]
    main_logic: str
    risk_params: Dict[str, float]

class NTSLParser:
    """
    Parser que converte código NTSL em estrutura Python executável
    Baseado na documentação oficial em docs/
    """
    
    def __init__(self):
        self.strategy = None
        # Mapeamento baseado em docs/funcoes_constantes_NTSL.md
        self.ntsl_functions_map = {
            'Media': 'smma',
            'Average': 'sma', 
            'WAverage': 'wma',
            'XAverage': 'ema',
            'AvgTrueRange': 'atr',
            'BollingerBands': 'bollinger_bands',
            'RSI': 'rsi',
            'Stochastic': 'stochastic',
            'MACD': 'macd',
            'Close': 'close',
            'High': 'high', 
            'Low': 'low',
            'Open': 'open_price',
            'Volume': 'volume',
            'Time': 'time',
            'Date': 'date',
            'Position': 'position',
            'OpenResult': 'open_result'
        }
        
        # Constantes NTSL baseadas na documentação
        self.ntsl_constants = {
            'clBlack': 0x000000,
            'clWhite': 0xFFFFFF, 
            'clRed': 0x0000FF,
            'clGreen': 0x008000,
            'clBlue': 0xFF0000,
            'clYellow': 0x00FFFF,
            'clFuchsia': 0xFF00FF,
            'clAqua': 0xFFFF00
        }
    
    def parse_file(self, ntsl_file_path: str) -> NTSLStrategy:
        """Parseia arquivo NTSL e retorna estratégia estruturada"""
        with open(ntsl_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return self.parse_content(content)
    
    def parse_content(self, ntsl_code: str) -> NTSLStrategy:
        """Parseia conteúdo NTSL seguindo sintaxe documentada"""
        # Remover comentários de linha e bloco
        clean_code = self._remove_comments(ntsl_code)
        
        # Extrair seções na ordem correta
        inputs = self._extract_inputs(clean_code)
        variables = self._extract_variables(clean_code) 
        functions = self._extract_functions(clean_code)
        main_logic = self._extract_main_logic(clean_code)
        
        # Extrair parâmetros de risco
        risk_params = self._extract_risk_parameters(inputs)
        
        strategy = NTSLStrategy(
            name=inputs.get('nomeEstrategia', 'Unknown'),
            magic_number=inputs.get('numeroMagico', 0), 
            inputs=inputs,
            variables=variables,
            functions=functions,
            main_logic=main_logic,
            risk_params=risk_params
        )
        
        self.strategy = strategy
        return strategy
    
    def _remove_comments(self, code: str) -> str:
        """Remove comentários NTSL (// e {})"""
        # Comentários de linha
        code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)
        # Comentários de bloco
        code = re.sub(r'\{[^}]*\}', '', code, flags=re.DOTALL)
        return code
    
    def _extract_inputs(self, code: str) -> Dict[str, Any]:
        """Extrai seção Input conforme sintaxe NTSL"""
        inputs = {}
        
        # Padrão: Input ... (conteúdo até próxima seção)
        input_section = re.search(
            r'Input\s+(.*?)(?=Var\s|function\s|begin\s|end\s*;|\Z)', 
            code, 
            re.DOTALL | re.IGNORECASE
        )
        
        if input_section:
            content = input_section.group(1).strip()
            
            # Processar declarações linha por linha
            lines = content.split('\n')
            for line in lines:
                line = line.strip()
                if not line or line.startswith('//'):
                    continue
                    
                # Padrão: nomeVariavel(valor);
                match = re.match(r'(\w+)\s*\(\s*([^)]+)\s*\)\s*;', line)
                if match:
                    var_name = match.group(1)
                    var_value = match.group(2).strip()
                    inputs[var_name] = self._parse_value(var_value)
        
        return inputs
    
    def _extract_variables(self, code: str) -> Dict[str, Any]:
        """Extrai seção Var conforme sintaxe NTSL"""
        variables = {}
        
        var_section = re.search(
            r'Var\s+(.*?)(?=function\s|begin\s|\Z)', 
            code, 
            re.DOTALL | re.IGNORECASE
        )
        
        if var_section:
            content = var_section.group(1).strip()
            
            # Processar declarações de variáveis
            # Padrão: var1, var2, var3: TipoVariavel;
            declarations = re.findall(
                r'([^:;]+):\s*(\w+)\s*;', 
                content, 
                re.IGNORECASE
            )
            
            for vars_list, var_type in declarations:
                var_names = [v.strip() for v in vars_list.split(',')]
                default_value = self._get_default_value_for_type(var_type)
                
                for var_name in var_names:
                    var_name = var_name.strip()
                    if var_name:
                        variables[var_name] = default_value
        
        return variables
    
    def _extract_functions(self, code: str) -> Dict[str, str]:
        """Extrai funções definidas pelo usuário"""
        functions = {}
        
        # Padrão: function NomeFuncao(parametros): TipoRetorno;
        function_pattern = r'function\s+(\w+)\s*\([^)]*\)\s*:\s*\w+\s*;(.*?)end\s*;'
        matches = re.finditer(function_pattern, code, re.DOTALL | re.IGNORECASE)
        
        for match in matches:
            func_name = match.group(1)
            func_body = match.group(2).strip()
            functions[func_name] = func_body
        
        return functions
    
    def _extract_main_logic(self, code: str) -> str:
        """Extrai lógica principal (begin...end)"""
        main_match = re.search(
            r'begin\s*(.*?)\s*end\s*\.?\s*$', 
            code, 
            re.DOTALL | re.IGNORECASE
        )
        return main_match.group(1).strip() if main_match else ""
    
    def _extract_risk_parameters(self, inputs: Dict) -> Dict[str, float]:
        """Extrai parâmetros de risco baseado em padrões do catálogo"""
        risk_keys = [
            'riscoMaximoDiario', 'lucroMaximoDiario', 'maxTradesPorDia',
            'contratosPorOperacao', 'fatorAtrStop', 'fatorAtrGain',
            'custoPorContrato', 'pontosPorTick', 'scoreMinimoEntrada'
        ]
        
        risk_params = {}
        for key in risk_keys:
            if key in inputs:
                try:
                    risk_params[key] = float(inputs[key])
                except (ValueError, TypeError):
                    risk_params[key] = 0.0
        
        return risk_params
    
    def _parse_value(self, value_str: str) -> Any:
        """Converte string de valor para tipo Python apropriado"""
        value_str = value_str.strip().strip('"\'')
        
        # Boolean (NTSL usa True/False)
        if value_str.lower() == 'true':
            return True
        elif value_str.lower() == 'false':
            return False
        
        # Integer
        try:
            if '.' not in value_str and not value_str.lower().startswith('0x'):
                return int(value_str)
        except ValueError:
            pass
        
        # Float
        try:
            return float(value_str)
        except ValueError:
            pass
        
        # Hexadecimal (cores)
        if value_str.lower().startswith('0x'):
            try:
                return int(value_str, 16)
            except ValueError:
                pass
        
        # String
        return value_str
    
    def _get_default_value_for_type(self, type_name: str):
        """Retorna valor padrão baseado no tipo NTSL documentado"""
        type_defaults = {
            'Integer': 0,
            'Float': 0.0,
            'Boolean': False,
            'String': ""
        }
        return type_defaults.get(type_name, 0)
    
    def convert_to_python_logic(self, ntsl_logic: str) -> str:
        """Converte lógica NTSL para Python executável"""
        python_code = ntsl_logic
        
        # Substituir funções NTSL por equivalentes Python
        for ntsl_func, python_func in self.ntsl_functions_map.items():
            pattern = rf'\b{ntsl_func}\s*\('
            replacement = f'{python_func}('
            python_code = re.sub(pattern, replacement, python_code, flags=re.IGNORECASE)
        
        # Substituir operadores
        replacements = [
            (r'\band\b', ' and ', re.IGNORECASE),
            (r'\bor\b', ' or ', re.IGNORECASE), 
            (r'\bnot\b', ' not ', re.IGNORECASE),
            (r'\bthen\b', ':', re.IGNORECASE),
            (r'\bif\b([^t])', r'if \1', re.IGNORECASE),
            (r'\belse\b', 'else', re.IGNORECASE),
            (r':=', '=', 0),
            (r';$', '', re.MULTILINE)
        ]
        
        for pattern, replacement, flags in replacements:
            python_code = re.sub(pattern, replacement, python_code, flags=flags)
        
        return python_code
