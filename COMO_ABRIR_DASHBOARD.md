# 🚨 ATENÇÃO - COMO ABRIR O DASHBOARD CORRETAMENTE

## ❌ NÃO FAÇA ISSO:

- ❌ **NÃO** clique duas vezes no `index.html`
- ❌ **NÃO** arraste o `index.html` para o navegador
- ❌ **NÃO** abra diretamente pelo explorador de arquivos

**Isso causa o erro:** "Erro de rede ao carregar dados.json"

---

## ✅ FAÇA ISSO:

### **Método 1: Atalho (MAIS FÁCIL)**

1. **Clique duas vezes no arquivo:**
   ```
   ABRIR_DASHBOARD.bat
   ```

2. **Aguarde alguns segundos**

3. **O navegador abrirá automaticamente** com o dashboard funcionando!

### **Método 2: Terminal**

1. Abra o PowerShell ou Prompt de Comando na pasta do projeto
2. Execute:
   ```bash
   python servidor_local.py
   ```
3. O navegador abrirá automaticamente

---

## 🔍 Por Que Isso É Necessário?

Quando você abre o `index.html` diretamente, o navegador bloqueia o carregamento do arquivo `dados.json` por questões de segurança (política CORS).

**Usando o servidor local**, o navegador trata como um site normal e permite carregar todos os arquivos.

---

## ✅ Verificação

Após usar o servidor local, você verá:

- ✅ Dashboard carrega sem erros
- ✅ Dados aparecem corretamente
- ✅ Gráficos são exibidos
- ✅ Todas as abas funcionam

---

## 🆘 Ainda Com Problemas?

1. Verifique se o Python está instalado
2. Verifique se os arquivos estão na mesma pasta:
   - `index.html`
   - `dados.json`
   - `dashboard.js`
   - `servidor_local.py`
3. Tente executar: `python --version` no terminal

---

## 📝 Resumo

**SEMPRE use:** `ABRIR_DASHBOARD.bat`  
**NUNCA abra:** `index.html` diretamente

Isso resolve todos os problemas! 🎯


