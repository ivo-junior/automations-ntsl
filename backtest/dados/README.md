# 📊 Diretório de Dados para Backtest

Este diretório armazena os arquivos CSV com dados históricos para os backtests.

## 📁 Estrutura Recomendada

```
dados/
├── WINQ23_15min_ago2024.csv
├── WDOQ23_15min_set2024.csv  
├── PETR4_1h_2024.csv
└── README.md
```

## 📝 Formatos Suportados

### CSV do Profit Pro
- **Separadores**: vírgula (`,`) ou ponto-e-vírgula (`;`)
- **Encoding**: UTF-8 ou ANSI
- **Colunas obrigatórias**:
  - Data/Hora (formatos aceitos: `YYYY-MM-DD HH:MM`, `DD/MM/YYYY HH:MM`)
  - Open/Abertura
  - High/Maxima  
  - Low/Minima
  - Close/Fechamento
  - Volume (opcional - será criado automaticamente se ausente)

### Exemplo de CSV válido:
```csv
DateTime,Open,High,Low,Close,Volume
2024-08-14 09:00:00,134.50,134.80,134.20,134.65,1250
2024-08-14 09:15:00,134.65,134.90,134.40,134.75,980
```

## 🎯 Como Obter Dados

### 1. **Profit Pro (Recomendado)**
- Menu: Ferramentas → Exportar Dados
- Selecionar: Ativo, Período, Timeframe
- Formato: CSV com cabeçalho
- Salvar neste diretório

### 2. **Yahoo Finance (Alternativa)**
- O sistema pode baixar automaticamente
- Menos preciso para mini-contratos brasileiros
- Use apenas para testes iniciais

### 3. **MetaTrader 5**
- Exportar histórico como CSV
- Ajustar formato de data se necessário

## 🔧 Configuração

O sistema detecta automaticamente:
- ✅ Formato de data/hora
- ✅ Separador (vírgula ou ponto-e-vírgula)
- ✅ Nomes das colunas (português/inglês)
- ✅ Encoding do arquivo

## 💡 Dicas

1. **Nomeação**: Use nomes descritivos como `ATIVO_TIMEFRAME_PERIODO.csv`
2. **Tamanho**: Arquivos até 50MB são processados rapidamente
3. **Qualidade**: Dados do próprio broker são mais precisos
4. **Backup**: Mantenha cópias dos dados importantes

## ⚠️ Troubleshooting

### Erro: "Colunas obrigatórias não encontradas"
- Verifique se o CSV tem colunas OHLC
- Renomeie colunas conforme necessário

### Erro: "Formato de data inválido"  
- Use formato ISO (YYYY-MM-DD HH:MM:SS)
- Ou formato brasileiro (DD/MM/YYYY HH:MM)

### Arquivo muito lento para carregar
- Divida em períodos menores
- Remova colunas desnecessárias
- Comprima com zip se necessário

## 📞 Suporte

Em caso de problemas com formatos de dados:
1. Verifique os exemplos neste README
2. Teste com um arquivo pequeno primeiro
3. Use o modo debug do console runner
