# 🔧 Solução: Porta 8000 Já Está em Uso

## ❌ Erro que você está vendo:
```
OSError: [WinError 10048] Normalmente é permitida apenas uma utilização de cada endereço de soquete
```

## ✅ Soluções

### **Solução 1: Fechar Servidores Anteriores (RECOMENDADO)**

1. **Clique duas vezes no arquivo:**
   ```
   FECHAR_SERVIDOR.bat
   ```

2. **Aguarde** o script fechar os processos

3. **Execute novamente:** `ABRIR_DASHBOARD.bat`

### **Solução 2: O Servidor Agora Usa Porta Automática**

O script foi atualizado! Agora ele:
- ✅ Detecta automaticamente se a porta 8000 está ocupada
- ✅ Usa outra porta automaticamente (8001, 8002, etc.)
- ✅ Mostra qual porta está sendo usada

**Basta executar:** `ABRIR_DASHBOARD.bat` novamente

### **Solução 3: Fechar Manualmente**

1. **Abra o Gerenciador de Tarefas** (Ctrl+Shift+Esc)
2. **Procure por processos Python** rodando
3. **Finalize os processos** relacionados ao servidor
4. **Execute novamente:** `ABRIR_DASHBOARD.bat`

---

## 🔍 Por Que Isso Acontece?

- O servidor anterior não foi fechado corretamente
- Outro programa está usando a porta 8000
- Múltiplas janelas do servidor estão abertas

---

## ✅ Verificação

Após usar qualquer solução:

1. Execute `ABRIR_DASHBOARD.bat`
2. Verifique se o servidor inicia sem erros
3. O navegador deve abrir automaticamente

---

## 🎯 Resumo

**Se a porta estiver ocupada:**
1. Use `FECHAR_SERVIDOR.bat` primeiro
2. Depois execute `ABRIR_DASHBOARD.bat`

**Ou simplesmente execute `ABRIR_DASHBOARD.bat` novamente** - ele agora encontra uma porta livre automaticamente!


