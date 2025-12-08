# 📋 Instruções para Atualizar os Dados do Dashboard

## 🎯 Como Atualizar os Dados

Agora os dados estão separados em um arquivo JSON, o que facilita muito a atualização! Siga os passos abaixo:

### **Passo 1: Localizar o Arquivo de Dados**

Abra o arquivo `dados.json` na mesma pasta do dashboard. Este arquivo contém todos os dados que aparecem no dashboard.

### **Passo 2: Atualizar os Dados**

Você pode editar o arquivo `dados.json` diretamente. Os dados estão organizados em seções:

#### **Estrutura dos Dados:**

1. **`labels`** - Lista dos meses (ex: `["janeiro", "fevereiro", "março", ...]`)
   - Adicione novos meses ao final da lista se necessário
   - Exemplo: `["janeiro", "fevereiro", ..., "novembro", "dezembro"]`

2. **`colaboradores`** - Dados de colaboradores por estabelecimento
   - `estabelecimentos`: Lista dos códigos dos estabelecimentos
   - `dados`: Array de arrays, onde cada array interno representa um estabelecimento e contém os valores mensais
   - `totais`: Totais mensais de todos os estabelecimentos

3. **`admitidos`** - Dados de admissões
   - `dados`: Array de arrays com admissões por estabelecimento e mês
   - `totais`: Totais mensais de admissões

4. **`desligados`** - Dados de desligamentos
   - `dados`: Array de arrays com desligamentos por estabelecimento e mês
   - `totais`: Totais mensais de desligamentos

5. **`aprendizes`** - Total de aprendizes por mês
   - `totais`: Array com o total de aprendizes de cada mês

6. **`pcd`** - Total de colaboradores PCD por mês
   - `totais`: Array com o total de PCD de cada mês

7. **`demographics`** - Dados demográficos
   - `gender`: Distribuição por gênero
   - `ageRange`: Distribuição por faixa etária

8. **`porGerenteEvolucao`** - Dados por gerente
   - `colaboradores`, `admissoes`, `demissoes`: Cada um com `labels` (nomes dos gerentes) e `dados` (arrays de valores mensais)

9. **`porSegmentoEvolucao`** - Dados por segmento
   - `colaboradores`: Com `labels` (nomes dos segmentos) e `dados`

10. **`turnover`** - Taxa de turnover
    - `labels`: Estabelecimentos
    - `rates`: Taxas de turnover em porcentagem

### **Passo 3: Importante - Manter a Consistência**

⚠️ **ATENÇÃO**: Ao adicionar um novo mês, você precisa atualizar TODOS os arrays de dados para incluir o novo valor. Todos os arrays devem ter o mesmo número de elementos (correspondente ao número de meses).

**Exemplo:**
- Se você tem 10 meses, cada array deve ter 10 valores
- Se adicionar o 11º mês, todos os arrays devem ter 11 valores

### **Passo 4: Validar o JSON**

Antes de salvar, certifique-se de que:
- ✅ Todas as chaves estão entre aspas duplas
- ✅ Todos os arrays estão entre colchetes `[]`
- ✅ Todos os objetos estão entre chaves `{}`
- ✅ Não há vírgulas extras no final de arrays/objetos
- ✅ Todos os números estão corretos

### **Passo 5: Testar o Dashboard**

1. Salve o arquivo `dados.json`
2. Abra o arquivo `index.html` no navegador
3. Verifique se os dados aparecem corretamente
4. Se houver erro, verifique o console do navegador (F12) para ver mensagens de erro

## 🔧 Dicas Importantes

### **Adicionar um Novo Mês:**

1. Adicione o nome do mês em `labels`:
   ```json
   "labels": [ "janeiro", "fevereiro", ..., "novembro" ]
   ```

2. Adicione um novo valor ao final de cada array em `colaboradores.dados`:
   ```json
   [ 192.0, 191.0, ..., 202.0, 205.0 ]  // novo valor 205.0 no final
   ```

3. Adicione um novo valor em `colaboradores.totais`:
   ```json
   "totais": [ 540.0, 548.0, ..., 601.0, 605.0 ]  // novo total
   ```

4. Repita para todos os outros arrays (`admitidos`, `desligados`, `aprendizes`, `pcd`, etc.)

### **Adicionar um Novo Estabelecimento:**

1. Adicione o código em `colaboradores.estabelecimentos`:
   ```json
   "estabelecimentos": [ "101", "102", ..., "109" ]
   ```

2. Adicione um novo array em `colaboradores.dados` com valores para todos os meses:
   ```json
   "dados": [
     [ 192.0, 191.0, ... ],  // estabelecimento 101
     [ 128.0, 128.0, ... ],  // estabelecimento 102
     ...
     [ 50.0, 52.0, ... ]     // novo estabelecimento 109
   ]
   ```

3. Atualize os totais em `colaboradores.totais` somando os novos valores

### **Ferramentas Úteis:**

- Use um editor de texto com validação JSON (VS Code, Notepad++, etc.)
- Valide o JSON online em: https://jsonlint.com/
- Use uma planilha Excel/Google Sheets para organizar os dados antes de converter para JSON

## 📝 Exemplo de Atualização

Suponha que você quer adicionar os dados de **novembro**:

```json
{
  "labels": [ "janeiro", "fevereiro", ..., "outubro", "novembro" ],
  "colaboradores": {
    "totais": [ 540.0, 548.0, ..., 601.0, 610.0 ],  // adicionei 610.0
    "dados": [
      [ 192.0, ..., 202.0, 205.0 ],  // adicionei 205.0 no final
      [ 128.0, ..., 149.0, 152.0 ],  // adicionei 152.0 no final
      // ... repita para todos os estabelecimentos
    ]
  },
  "admitidos": {
    "totais": [ 10, 16, ..., 28, 30 ],  // adicionei 30
    "dados": [
      [ 2, 2, ..., 3, 4 ],  // adicionei 4 no final
      // ... repita para todos os estabelecimentos
    ]
  }
  // ... continue atualizando todos os outros campos
}
```

## ❓ Problemas Comuns

### **Erro: "Erro ao carregar dados"**
- Verifique se o arquivo `dados.json` está na mesma pasta que `index.html`
- Verifique se o JSON está válido (sem erros de sintaxe)

### **Dados não aparecem**
- Abra o console do navegador (F12) e verifique se há erros
- Verifique se todos os arrays têm o mesmo número de elementos

### **Gráficos não aparecem**
- Verifique se os dados estão no formato correto (números, não strings)
- Verifique se não há valores `null` ou `undefined`

## 📞 Precisa de Ajuda?

Se tiver dúvidas sobre a estrutura dos dados ou encontrar erros, verifique:
1. O console do navegador (F12 → Console)
2. A estrutura do JSON comparando com o exemplo fornecido
3. Se todos os arrays têm o mesmo tamanho

---

**Última atualização:** Os dados estão organizados e prontos para serem atualizados facilmente! 🎉


