# ⚡ Solução Rápida para o Erro de Carregamento

## ❌ Erro que você está vendo:
```
Erro de rede ao carregar dados.json. Verifique se o arquivo existe na mesma pasta que index.html
```

## ✅ SOLUÇÃO: Use o Servidor Local

### **Passo 1: Inicie o Servidor**

**Opção A - Mais Fácil:**
- Clique duas vezes no arquivo: **`ABRIR_DASHBOARD.bat`**

**Opção B - Manual:**
- Abra o terminal na pasta do projeto
- Execute: `python servidor_local.py`

### **Passo 2: O Navegador Abrirá Automaticamente**

O dashboard abrirá em: `http://localhost:8000/index.html`

### **Passo 3: Para Parar o Servidor**

- Pressione `CTRL+C` no terminal

---

## 🔍 Por Que Isso Acontece?

Quando você abre o `index.html` diretamente (clicando duas vezes), o navegador bloqueia o carregamento de arquivos locais por segurança (política CORS).

**Usando o servidor local**, o navegador trata como um site normal e permite carregar o `dados.json`.

---

## ✅ Verificação Rápida

1. ✅ O arquivo `dados.json` existe? → **SIM** (já verificado)
2. ✅ O arquivo está na mesma pasta? → **SIM** (já verificado)
3. ✅ Você está usando o servidor local? → **Use agora!**

---

## 🎯 Resumo

**NÃO abra o `index.html` diretamente!**

**SEMPRE use:** `ABRIR_DASHBOARD.bat` ou `python servidor_local.py`

Isso resolve o problema! 🚀


