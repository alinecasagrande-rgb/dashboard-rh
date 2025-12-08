# 🔧 Solução para Erro "NetworkError when attempting to fetch resource"

## ❌ Problema

Quando você abre o `index.html` diretamente no navegador (clicando duas vezes), o navegador bloqueia o carregamento do arquivo `dados.json` por questões de segurança (CORS).

## ✅ Soluções

### **Solução 1: Usar Servidor Local (RECOMENDADO)**

Esta é a melhor solução e funciona perfeitamente:

1. **Execute o servidor local:**
   - **Opção A:** Clique duas vezes no arquivo `ABRIR_DASHBOARD.bat`
   - **Opção B:** No terminal, execute: `python servidor_local.py`

2. **O navegador abrirá automaticamente** com o dashboard funcionando!

3. **Para parar o servidor:** Pressione `CTRL+C` no terminal

### **Solução 2: Abrir com Navegador Específico**

Alguns navegadores são mais permissivos:

1. **Chrome/Edge com flags:**
   - Feche todas as janelas do Chrome/Edge
   - Abra o terminal e execute:
     ```
     chrome.exe --allow-file-access-from-files
     ```
   - Ou para Edge:
     ```
     msedge.exe --allow-file-access-from-files
     ```

2. **Firefox:**
   - Geralmente funciona melhor com arquivos locais
   - Tente abrir o `index.html` diretamente

### **Solução 3: Usar Extensão do Navegador**

Instale uma extensão que permite CORS local:
- **Chrome:** "Allow CORS: Access-Control-Allow-Origin"
- **Firefox:** "CORS Everywhere"

---

## 🎯 Recomendação

**Use sempre a Solução 1 (Servidor Local)** - É a mais confiável e não requer configurações especiais!

---

## 📝 Arquivos Criados

- **`servidor_local.py`** - Servidor HTTP simples em Python
- **`ABRIR_DASHBOARD.bat`** - Atalho para iniciar o servidor (Windows)
- **`dashboard.js`** - Atualizado para funcionar melhor com arquivos locais

---

## ✅ Verificação

Após usar qualquer solução, verifique:
- ✅ O dashboard carrega sem erros
- ✅ Os dados aparecem corretamente
- ✅ Os gráficos são exibidos
- ✅ A competência mostra "Novembro de 2025"

---

## 🆘 Ainda com Problemas?

1. Verifique se o arquivo `dados.json` está na mesma pasta que `index.html`
2. Verifique se o Python está instalado (para o servidor)
3. Tente abrir o console do navegador (F12) e veja se há outros erros


