# 🔄 Como Atualizar os Dados do Dashboard

## ✅ Método Mais Simples (RECOMENDADO)

### **Opção 1: Usar o Atalho (Windows)**

1. **Clique duas vezes no arquivo:** `ATUALIZAR_DADOS.bat`
2. **Aguarde** o script processar os dados
3. **Pronto!** Os dados foram atualizados

### **Opção 2: Usar o Terminal**

1. **Abra o PowerShell ou Prompt de Comando** na pasta do projeto
2. **Execute:**
   ```bash
   python processar_dados_final.py
   ```
3. **Aguarde** a mensagem de sucesso

---

## 📋 O Que o Script Faz

O script `processar_dados_final.py`:

1. ✅ **Baixa automaticamente** os dados do Google Sheets
2. ✅ **Processa** colaboradores, admissões e desligamentos
3. ✅ **Atualiza** o arquivo `dados.json`
4. ✅ **Mantém** todos os dados históricos

---

## 🔗 Link da Planilha

O script está configurado para usar este link:
```
https://docs.google.com/spreadsheets/d/e/2PACX-1vSf71N2ZusoPVlFxeAwG0yLMRQi3rMiYsf422EnY-zU-NrGf3y142prw-9_kOyXfNrsDQ3kkxKF09uw/pub?output=csv
```

**Se você mudar o link da planilha**, edite o arquivo `processar_dados_final.py` na linha 9 e altere o `CSV_URL`.

---

## ❓ Problemas Comuns

### **Erro: "python não é reconhecido"**
- **Solução:** Instale o Python ou use o caminho completo do Python
- Exemplo: `C:\Python314\python.exe processar_dados_final.py`

### **Erro: "Erro ao baixar dados"**
- **Solução:** Verifique sua conexão com a internet
- Verifique se o link da planilha está correto e público

### **Erro: "Erro ao atualizar dados.json"**
- **Solução:** Verifique se o arquivo `dados.json` existe na mesma pasta
- Verifique se você tem permissão para escrever na pasta

---

## ✅ Verificação

Após executar o script, você verá:

```
============================================================
SUCESSO! Arquivo dados.json atualizado
============================================================
```

**Então:**
1. Abra o `index.html` no navegador
2. Recarregue a página (F5)
3. Verifique se os dados estão atualizados

---

## 🎯 Dica

**Execute o script sempre que atualizar a planilha do Google Sheets!**

O processo leva apenas alguns segundos e mantém tudo sincronizado.


