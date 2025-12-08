# 📊 Como Atualizar os Dados do Dashboard a partir do Google Sheets

## ✅ Dados de Novembro Já Atualizados

Os dados principais de novembro de 2025 já foram atualizados no arquivo `dados.json` com base na planilha do Google Sheets:

- ✅ **Colaboradores por estabelecimento** (novembro)
- ✅ **Admissões** (novembro)  
- ✅ **Desligamentos** (novembro)
- ✅ **Turnover** (novembro)
- ✅ **Totais gerais**

## 📝 Como Atualizar Dados Futuros

### **Método 1: Atualização Manual (Recomendado para pequenas atualizações)**

1. **Abra a planilha do Google Sheets:**
   - Link: https://docs.google.com/spreadsheets/d/1_JoETFEN0c5554x3_C1jjAgGu_2yEBtSqiZCEnQZGuQ/edit

2. **Identifique os dados que precisa atualizar:**
   - Colaboradores por estabelecimento
   - Admissões por estabelecimento
   - Desligamentos por estabelecimento
   - Totais gerais
   - Dados por gerente (se disponível)
   - Dados por segmento (se disponível)
   - Aprendizes e PCD (se disponível)

3. **Abra o arquivo `dados.json`** e atualize:
   - Adicione o novo mês em `labels`
   - Adicione os novos valores ao final de cada array correspondente

### **Método 2: Exportar do Google Sheets para CSV**

1. **No Google Sheets:**
   - Arquivo → Fazer download → Valores separados por vírgula (.csv)

2. **Use um editor de planilhas** (Excel, Google Sheets) para organizar os dados

3. **Converta manualmente para o formato JSON** seguindo a estrutura do `dados.json`

### **Método 3: Usar a API do Google Sheets (Avançado)**

Para automatizar completamente, você pode criar um script que:
1. Conecta à API do Google Sheets
2. Lê os dados automaticamente
3. Converte para o formato JSON
4. Atualiza o arquivo `dados.json`

**Nota:** Isso requer configuração de credenciais da API do Google.

## 🔍 Estrutura dos Dados na Planilha

Com base na planilha visualizada, a estrutura parece ser:

| Coluna A | Coluna B | Coluna C | Coluna D | Coluna E | Coluna F |
|----------|----------|----------|----------|----------|----------|
| Mês      | Estab.   | Colab.   | Admis.   | Deslig.  | Turnover |

**Exemplo de dados de novembro:**
- 101: 199 colaboradores, 5 admissões, 2 desligamentos, 1.0% turnover
- 102: 142 colaboradores, 3 admissões, 3 desligamentos, 2.1% turnover
- 103: 138 colaboradores, 8 admissões, 5 desligamentos, 3.6% turnover
- ... e assim por diante

## 📋 Checklist de Atualização

Ao adicionar um novo mês, certifique-se de atualizar:

- [ ] `labels` - Adicionar o nome do mês
- [ ] `colaboradores.dados` - Adicionar valores para cada estabelecimento
- [ ] `colaboradores.totais` - Adicionar total geral
- [ ] `admitidos.dados` - Adicionar admissões por estabelecimento
- [ ] `admitidos.totais` - Adicionar total de admissões
- [ ] `desligados.dados` - Adicionar desligamentos por estabelecimento
- [ ] `desligados.totais` - Adicionar total de desligamentos
- [ ] `aprendizes.totais` - Adicionar total de aprendizes (se disponível)
- [ ] `pcd.totais` - Adicionar total de PCD (se disponível)
- [ ] `turnover.rates` - Atualizar taxas de turnover
- [ ] `porGerenteEvolucao` - Atualizar dados por gerente (se disponível)
- [ ] `porSegmentoEvolucao` - Atualizar dados por segmento (se disponível)

## ⚠️ Importante

1. **Todos os arrays devem ter o mesmo número de elementos** (correspondente ao número de meses)
2. **Valide o JSON** antes de salvar (use https://jsonlint.com/)
3. **Teste o dashboard** após atualizar para garantir que tudo funciona

## 🆘 Precisa de Ajuda?

Se tiver dificuldades para atualizar:
1. Verifique o console do navegador (F12) para erros
2. Valide o JSON em https://jsonlint.com/
3. Compare com a estrutura atual do `dados.json`

---

**Última atualização:** Novembro de 2025 ✅


