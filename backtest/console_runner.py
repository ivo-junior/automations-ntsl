"""
Console Runner para Sistema de Backtest NTSL

Este script permite executar backtests via console de forma interativa,
carregando dados CSV e estratégias NTSL facilmente.
"""

import os
import sys
import argparse
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional 
from .ntsl_parser import NTSLParser
from .backtest_engine import BacktestEngine
from .data_provider import DataProvider

class ConsoleRunner:
    """Runner principal para execução via console"""
    
    def __init__(self):
        self.parser = NTSLParser()
        self.engine = BacktestEngine()
        self.data_provider = DataProvider()
        # Definir diretórios base do projeto
        self.base_dir = Path(__file__).parent.parent.resolve()
        self.strategies_dir = self.base_dir / "estrategias"
        self.automations_dir = self.strategies_dir / "automations"
        self.data_dir = self.base_dir / "backtest" / "dados"
        
        # Criar diretórios se não existirem
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
    def run_interactive(self):
        """Executa backtest de forma interativa"""
        print("=" * 70)
        print("SISTEMA DE BACKTEST NTSL - MODO INTERATIVO")
        print("=" * 70)
        
        # Mostrar estrutura do projeto
        self._display_project_structure()
        
        try:
            # 1. Solicitar estratégia
            strategy_path = self._get_strategy_path()
            strategy = self.parser.parse_file(strategy_path)
            
            print(f"\nEstratégia carregada: {strategy.name}")
            print(f"   Arquivo: {Path(strategy_path).name}")
            print(f"   Magic Number: {strategy.magic_number}")
            print(f"   Parâmetros: {len(strategy.inputs)} encontrados")
            
            # 2. Solicitar dados
            data_path = self._get_data_path()
            target_interval = self._get_target_interval()
            asset_name = Path(data_path).stem.split('_')[0] # Extrai nome do ativo do arquivo
            data = self._load_data(data_path, target_interval)
            
            # 3. Configurar período (opcional)
            start_date, end_date = self._get_date_range(data)
            if start_date and end_date:
                data = data[(data.index >= start_date) & (data.index <= end_date)]
                print(f"Período filtrado: {start_date.date()} a {end_date.date()}")
            
            # 4. Executar backtest
            print(f"\nExecutando backtest...")
            result = self.engine.run_backtest(strategy, data, asset=asset_name, timeframe=target_interval)
            
            # 5. Mostrar resultados
            self._display_results(result)
            
            # 6. Opções de exportação
            self._export_options(result)
            
        except KeyboardInterrupt:
            print(f"\nOperação cancelada pelo usuário")
        except Exception as e:
            print(f"\nErro durante execução: {str(e)}")
            import traceback
            traceback.print_exc()
    
    def run_batch(self, strategy_path: str, data_path: str, start_date: str = None, 
                  end_date: str = None, output_dir: str = None, timeframe: Optional[str] = None):
        """Executa backtest em modo batch (não-interativo)"""
        
        try:
            print(f"MODO BATCH - Executando {strategy_path}")
            asset_name = Path(data_path).stem.split('_')[0]
            timeframe_str = f"{timeframe}min" if timeframe else "1min"

            # Carregar estratégia
            strategy = self.parser.parse_file(strategy_path)
            
            # Carregar e reamostrar dados
            data = self.data_provider.get_data(
                symbol=data_path, 
                start_date=start_date or '',
                end_date=end_date or '',
                source='local_csv',
                target_interval=timeframe_str
            )
            
            # Filtrar período se especificado
            if start_date and end_date:
                start = pd.to_datetime(start_date)
                end = pd.to_datetime(end_date)
                data = data[(data.index >= start) & (data.index <= end)]
            
            # Executar backtest
            result = self.engine.run_backtest(strategy, data, asset=asset_name, timeframe=timeframe_str)
            
            # Exportar resultados
            if output_dir and result:
                base_output_dir = self.base_dir / output_dir
                csv_dir = base_output_dir.parent / "trades"
                charts_dir = base_output_dir.parent / "graficos"
                
                excel_dir = base_output_dir
                excel_dir.mkdir(parents=True, exist_ok=True)
                csv_dir.mkdir(parents=True, exist_ok=True)
                charts_dir.mkdir(parents=True, exist_ok=True)

                # filename_base = self._generate_filename_base(result)
                # self._export_excel_report(result, filename_base, excel_dir)
                # self._export_trades_csv(result, filename_base, csv_dir)
                # self._export_equity_chart(result, filename_base, charts_dir)

            if result:
                self._display_results(result)
            
            return result
            
        except Exception as e:
            print(f"Erro no modo batch: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
    
    def _get_strategy_path(self) -> str:
        """Solicita caminho da estratégia com seleção interativa"""
        print(f"\nSELEÇÃO DE ESTRATÉGIA NTSL")
        print(f"-" * 40)
        
        # Verificar se diretório de automações existe
        if not self.automations_dir.exists():
            print(f"Diretório não encontrado: {self.automations_dir}")
            return self._get_strategy_path_manual()
        
        # Listar arquivos .txt no diretório de automações
        txt_files = list(self.automations_dir.rglob("*.txt"))
        
        if not txt_files:
            print(f"Nenhum arquivo .txt encontrado em {self.automations_dir}")
            return self._get_strategy_path_manual()
        
        # Organizar por subpasta para melhor visualização
        files_by_category = {}
        for file in txt_files:
            category = file.parent.name
            if category not in files_by_category:
                files_by_category[category] = []
            files_by_category[category].append(file)
        
        print(f"Estratégias disponíveis em {self.automations_dir.name}/:")
        print()
        
        all_files = []
        index = 1
        
        for category, files in files_by_category.items():
            print(f"{category.replace('_', ' ').title()}:")
            for file in files:
                print(f"   {index:2d}. {file.name}")
                all_files.append(file)
                index += 1
            print()
        
        print(f"   0. Digitar caminho manualmente")
        print(f"   q. Sair")
        
        while True:
            try:
                choice = input(f"\nEscolha uma estratégia (1-{len(all_files)}, 0, q): ").strip()
                
                if choice.lower() == 'q':
                    raise KeyboardInterrupt("Operação cancelada pelo usuário")
                
                if choice == '0':
                    return self._get_strategy_path_manual()
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(all_files):
                    selected_file = all_files[choice_num - 1]
                    print(f"Selecionado: {selected_file.relative_to(self.base_dir)}")
                    return str(selected_file)
                else:
                    print(f"Opção inválida. Digite um número entre 1 e {len(all_files)}")
                    
            except ValueError:
                print(f"Digite um número válido")
            except KeyboardInterrupt:
                raise
    
    def _get_strategy_path_manual(self) -> str:
        """Solicita caminho da estratégia manualmente"""
        print(f"\nENTRADA MANUAL DE ESTRATÉGIA")
        print(f"-" * 35)
        
        while True:
            path = input(f"Caminho da estratégia (.txt): ").strip()
            
            if not path:
                continue
            
            # Converter para Path e expandir caminhos relativos
            path_obj = Path(path)
            
            # Se não é absoluto, tentar relativo ao diretório base
            if not path_obj.is_absolute():
                test_paths = [
                    Path(path).resolve(),
                    self.data_dir / path,
                    self.base_dir / path
                ]
                
                for test_path in test_paths:
                    if test_path.exists():
                        path_obj = test_path
                        break
            
            if path_obj.exists():
                return str(path_obj)
            else:
                print(f"Arquivo não encontrado: {path}")
                print(f"Dica: Use caminhos relativos como 'orquestrador_moderado_1.txt'")
    
    def _get_data_path(self) -> str:
        """Solicita caminho dos dados CSV com seleção interativa"""
        print(f"\nSELEÇÃO DE DADOS (CSV)")
        print(f"-" * 30)
        
        # Verificar se diretório de dados existe
        if not self.data_dir.exists():
            print(f"Diretório de dados não encontrado: {self.data_dir}")
            print(f"Criando diretório...")
            self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Listar arquivos CSV no diretório de dados
        csv_files = list(self.data_dir.glob("*.csv"))
        
        if csv_files:
            print(f"Arquivos CSV disponíveis em {self.data_dir.name}/:")
            print()
            
            for i, file in enumerate(csv_files, 1):
                # Mostrar informações básicas do arquivo
                try:
                    file_size = file.stat().st_size
                    size_mb = file_size / (1024 * 1024)
                    print(f"   {i:2d}. {file.name} ({size_mb:.1f} MB)")
                except:
                    print(f"   {i:2d}. {file.name}")
            
            print(f"\n   0. Digitar caminho manualmente")
            print(f"   q. Sair")
            
            while True:
                try:
                    choice = input(f"\nEscolha um arquivo (1-{len(csv_files)}, 0, q): ").strip()
                    
                    if choice.lower() == 'q':
                        raise KeyboardInterrupt("Operação cancelada pelo usuário")
                    
                    if choice == '0':
                        break
                    
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(csv_files):
                        selected_file = csv_files[choice_num - 1]
                        print(f"Selecionado: {selected_file.name}")
                        return str(selected_file)
                    else:
                        print(f"Opção inválida. Digite um número entre 1 e {len(csv_files)}")
                        
                except ValueError:
                    print(f"Digite um número válido")
                except KeyboardInterrupt:
                    raise
        else:
            print(f"Diretório vazio: {self.data_dir}")
            print(f"Coloque seus arquivos CSV neste diretório para seleção automática")
        
        return self._get_data_path_manual()
    
    def _get_data_path_manual(self) -> str:
        """Solicita caminho dos dados CSV manualmente"""
        print(f"\nENTRADA MANUAL DE DADOS")
        print(f"-" * 30)
        print(f"Formatos suportados:")
        print(f"   - CSV do Profit Pro")
        print(f"   - Colunas: Date/Time, Open, High, Low, Close, Volume")
        print(f"   - Separadores: vírgula, ponto-e-vírgula (auto-detectado)")
        
        while True:
            path = input(f"\nCaminho do arquivo CSV: ").strip()
            
            if not path:
                continue
            
            # Converter para Path e expandir caminhos relativos
            path_obj = Path(path)
            
            # Se não é absoluto, tentar relativo ao diretório base
            if not path_obj.is_absolute():
                test_paths = [
                    Path(path).resolve(),
                    self.data_dir / path,
                    self.base_dir / path
                ]
                
                for test_path in test_paths:
                    if test_path.exists():
                        path_obj = test_path
                        break
            
            if path_obj.exists():
                return str(path_obj)
            else:
                print(f"Arquivo não encontrado: {path}")
                print(f"Dica: Coloque o CSV em {self.data_dir} para seleção automática")
    
    def _display_project_structure(self):
        """Exibe a estrutura de diretórios do projeto"""
        print(f"\nESTRUTURA DO PROJETO:")
        print(f"-" * 30)
        print(f"{self.base_dir.name}/")
        print(f"   estrategias/")
        print(f"      automations/          <- Estratégias NTSL (.txt)")
        print(f"   backtest/")
        print(f"      dados/               <- Dados CSV (1 minuto)")
        print(f"   examples/")
        print(f"      quick_test.py        <- Este script")
        print()

    def _get_target_interval(self) -> Optional[str]:
        """Solicita o tempo gráfico para reamostragem, validando a entrada."""
        print(f"\nTEMPO GRÁFICO PARA ANÁLISE (Daytrade: 1 a 30 minutos)")
        print(f"-" * 55)
        while True:
            interval_str = input(f"Digite o tempo em minutos (ex: 5, 15, 30) [Enter=1]: ").strip()
            if not interval_str:
                return "1min"
            
            try:
                interval_min = int(interval_str)
                if 1 <= interval_min <= 30:
                    # Converte para o formato de frequência do Pandas (ex: '15min')
                    return f"{interval_min}min"
                else:
                    print("Valor fora do intervalo permitido (1 a 30 minutos).")
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
        
    def _load_data(self, data_path: str, target_interval: Optional[str]) -> pd.DataFrame:
        """Carrega dados do CSV"""
        print(f"\nCarregando dados de {os.path.basename(data_path)}...")
        
        return self.data_provider.get_data(
            symbol=data_path, 
            start_date=None, 
            end_date=None, 
            source='local_csv',
            target_interval=target_interval
        )
    
    def _get_date_range(self, data: pd.DataFrame) -> tuple:
        """Solicita filtro de período (opcional)"""
        print(f"\nFILTRO DE PERÍODO (Opcional)")
        print(f"-" * 30)
        print(f"Dados disponíveis: {data.index[0].date()} a {data.index[-1].date()}")
        print(f"Total de barras: {len(data)}")
        
        use_filter = input(f"\nFiltrar período? (s/N): ").strip().lower()
        
        if use_filter in ['s', 'sim', 'y', 'yes']:
            try:
                start_str = input(f"Data início (YYYY-MM-DD): ").strip()
                end_str = input(f"Data fim (YYYY-MM-DD): ").strip()
                
                start_date = pd.to_datetime(start_str) if start_str else None
                end_date = pd.to_datetime(end_str) if end_str else None
                
                return start_date, end_date
            except:
                print(f"Formato de data inválido, usando período completo")
        
        return None, None
    
    def _display_results(self, result):
        """Exibe resultados do backtest no formato consolidado."""
        print(f"\n" + "=" * 60)
        print(f"RESULTADOS DO BACKTEST - {result.strategy_name}")
        print(f"   Ativo: {result.asset} | Timeframe: {result.timeframe}")
        print(f"=" * 60)
        
        if not result.metrics:
            print(f"Nenhuma operação executada")
            return
        
        m = result.metrics
        
        # --- Resumo Principal ---
        print(f"\n>> Resumo Principal")
        print(f"   Saldo Líquido Total: R$ {m['net_profit']:.2f}")
        print(f"   Fator de Lucro: {m['profit_factor']:.2f}")
        print(f"   Percentual de Acerto: {m['win_rate']:.1f}%")
        print(f"   Total de Operações: {m['total_trades']}")

        # --- Detalhes Financeiros ---
        print(f"\n>> Detalhes Financeiros")
        print(f"   Lucro Bruto: R$ {m['gross_profit']:.2f}")
        print(f"   Prejuízo Bruto: R$ {m['gross_loss']:.2f}")
        print(f"   Custos Totais: R$ {m['total_costs']:.2f}")

        # --- Detalhes Operacionais ---
        print(f"\n>> Detalhes Operacionais")
        print(f"   Operações Vencedoras: {m['winning_trades']}")
        print(f"   Operações Perdedoras: {m['losing_trades']}")
        print(f"   Média por Trade: R$ {m['avg_trade']:.2f}")
        print(f"   Média Ganho / Média Perda: {abs(m['avg_winner']/m['avg_loser']) if m['avg_loser'] != 0 else 'inf':.2f}")
        
        # --- Lista de Trades ---
        if len(result.trades) > 0:
            print(f"\nÚLTIMAS 5 OPERAÇÕES:")
            print(f"{ '#':<3} {'Tipo':<5} {'Entrada':<16} {'Saída':<16} {'Resultado':<10}")
            print(f"-" * 60)
            
            for i, trade in enumerate(result.trades[-5:], 1):
                entry_str = trade.entry_time.strftime('%d/%m %H:%M')
                exit_str = trade.exit_time.strftime('%d/%m %H:%M') if trade.exit_time else 'ABERTO'
                result_str = f"R$ {trade.result:.2f}" if trade.result is not None else "N/A"
                
                print(f"{i:<3} {trade.direction:<5} {entry_str:<16} {exit_str:<16} {result_str:<10}")
            
            if len(result.trades) > 5:
                print(f"... de um total de {len(result.trades)} operações")
    
    def _generate_filename_base(self, result) -> str:
        """Gera o nome base para os arquivos de resultado."""
        strategy_name = result.strategy_name.replace(' ', '_')
        asset = result.asset
        timeframe = result.timeframe
        period = result.period.replace(' ', '')
        return f"{strategy_name}_{asset}_{timeframe}_{period}"

    def _export_options(self, result):
        """Oferece opções de exportação com salvamento automático."""
        print(f"\nOPÇÕES DE EXPORTAÇÃO:")
        print(f"1. Relatório detalhado (Excel)")
        print(f"2. Lista de trades (CSV)")
        print(f"3. Gráfico de equity (PNG)")
        print(f"4. Todos os arquivos")
        print(f"5. Não exportar")
        
        choice = input(f"\nEscolha uma opção (1-5) [Enter=5]: ").strip()
        
        if not choice or choice == '5':
            return

        # Define os diretórios de saída padrão, criando se não existirem
        base_output_dir = self.base_dir / "resultados"
        excel_dir = base_output_dir / "backtests"
        csv_dir = base_output_dir / "trades"
        charts_dir = base_output_dir / "graficos"
        
        excel_dir.mkdir(parents=True, exist_ok=True)
        csv_dir.mkdir(parents=True, exist_ok=True)
        charts_dir.mkdir(parents=True, exist_ok=True)

        filename_base = self._generate_filename_base(result)
        
        if choice in ['1', '4']:
            self._export_excel_report(result, filename_base, excel_dir)
        if choice in ['2', '4']:
            self._export_trades_csv(result, filename_base, csv_dir)
        if choice in ['3', '4']:
            self._export_equity_chart(result, filename_base, charts_dir)
    
    def _export_excel_report(self, result, filename_base: str, output_dir: Path):
        """Exporta relatório em Excel"""
        try:
            filepath = output_dir / f"{filename_base}.xlsx"
            
            with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
                # Resumo
                summary_data = {
                    'Métrica': list(result.metrics.keys()),
                    'Valor': list(result.metrics.values())
                }
                pd.DataFrame(summary_data).to_excel(writer, sheet_name='Resumo', index=False)
                
                # Trades
                if result.trades:
                    trades_df = pd.DataFrame([t.__dict__ for t in result.trades])
                    trades_df.to_excel(writer, sheet_name='Trades', index=False)
            
            print(f"Relatório Excel salvo em: {filepath.relative_to(self.base_dir)}")
            
        except Exception as e:
            print(f"Erro ao salvar Excel: {str(e)}")
    
    def _export_trades_csv(self, result, filename_base: str, output_dir: Path):
        """Exporta lista de trades em CSV"""
        try:
            filepath = output_dir / f"{filename_base}.csv"
            trades_df = pd.DataFrame([t.__dict__ for t in result.trades])
            trades_df.to_csv(filepath, index=False, date_format='%Y-%m-%d %H:%M:%S')
            print(f"Trades CSV salvos em: {filepath.relative_to(self.base_dir)}")
            
        except Exception as e:
            print(f"Erro ao salvar CSV: {str(e)}")
    
    def _export_equity_chart(self, result, filename_base: str, output_dir: Path):
        """Exporta gráfico de equity"""
        try:
            import matplotlib.pyplot as plt
            
            filepath = output_dir / f"{filename_base}.png"
            
            plt.figure(figsize=(12, 6))
            result.equity_curve.plot(grid=True, linewidth=2, 
                                     title=f'Curva de Equity - {result.strategy_name} | {result.asset} | {result.timeframe}')
            plt.xlabel('Data')
            plt.ylabel('Resultado Acumulado (R$)')
            plt.tight_layout()
            plt.savefig(filepath, dpi=300)
            plt.close()
            
            print(f"Gráfico de equity salvo em: {filepath.relative_to(self.base_dir)}")
            
        except Exception as e:
            print(f"Erro ao salvar gráfico: {str(e)}")

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='Sistema de Backtest NTSL')
    parser.add_argument('--strategy', '-s', help='Caminho da estratégia NTSL')
    parser.add_argument('--data', '-d', help='Caminho do arquivo CSV')
    parser.add_argument('--start-date', help='Data início (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='Data fim (YYYY-MM-DD)')
    parser.add_argument('--output', '-o', help='Diretório de saída')
    parser.add_argument('--timeframe', '-t', help='Tempo gráfico em minutos (ex: 5, 15)')
    parser.add_argument('--batch', action='store_true', help='Modo batch (não-interativo)')
    
    args = parser.parse_args()
    
    runner = ConsoleRunner()
    
    if args.batch and args.strategy and args.data:
        # Modo batch
        result = runner.run_batch(
            args.strategy, 
            args.data, 
            args.start_date, 
            args.end_date, 
            args.output,
            args.timeframe
        )
    else:
        # Modo interativo
        runner.run_interactive()

if __name__ == "__main__":
    main()
