# 🚀 Publicar Dashboard - Guia Rápido

Seu repositório: **https://github.com/alinecasagrande-rgb/dashboard-rh.git**

## ⚡ Opção 1: GitHub Desktop (MAIS FÁCIL - Recomendado)

### Passo 1: Instalar GitHub Desktop
1. Baixe: https://desktop.github.com/
2. Instale o programa
3. Faça login com sua conta GitHub (alinecasagrande-rgb)

### Passo 2: Publicar
1. Abra o GitHub Desktop
2. Clique em **"File"** > **"Add Local Repository"**
3. Clique em **"Choose..."** e selecione a pasta: `C:\Users\rcamcb\Dashboard Recursos Humanos`
4. Clique em **"Add repository"**
5. Na parte inferior, preencha:
   - **Summary**: "Primeira versão do Dashboard de RH"
6. Clique em **"Commit to main"**
7. Clique em **"Publish repository"** (botão azul no topo)
8. Marque **"Keep this code private"** se quiser privado, ou deixe desmarcado para público
9. Clique em **"Publish repository"**

✅ **Pronto!** Seus arquivos estão no GitHub!

### Passo 3: Ativar GitHub Pages
1. No GitHub Desktop, clique em **"Repository"** > **"View on GitHub"**
2. No navegador, clique em **"Settings"** (Configurações)
3. No menu lateral, clique em **"Pages"**
4. Em **"Source"**, selecione:
   - Branch: **main**
   - Folder: **/ (root)**
5. Clique em **"Save"**
6. Aguarde 2-5 minutos
7. Seu dashboard estará em: **https://alinecasagrande-rgb.github.io/dashboard-rh**

---

## 🔧 Opção 2: Git via Terminal (Avançado)

### Passo 1: Instalar Git
1. Baixe: https://git-scm.com/download/win
2. Instale (aceite as opções padrão)
3. **Reinicie o PowerShell** após instalar

### Passo 2: Configurar Git (primeira vez)
Abra o PowerShell e execute:

```powershell
git config --global user.name "Aline Casagrande"
git config --global user.email "seu-email@exemplo.com"
```

**⚠️ IMPORTANTE**: Substitua o email pelo seu email do GitHub!

### Passo 3: Publicar
No PowerShell, na pasta do projeto, execute:

```powershell
cd "C:\Users\rcamcb\Dashboard Recursos Humanos"

# Inicializar repositório
git init

# Adicionar arquivos
git add .

# Fazer commit
git commit -m "Primeira versão do Dashboard de RH"

# Adicionar repositório remoto
git remote add origin https://github.com/alinecasagrande-rgb/dashboard-rh.git

# Enviar para GitHub
git branch -M main
git push -u origin main
```

Se pedir login, use:
- **Usuário**: alinecasagrande-rgb
- **Senha**: Use um **Personal Access Token** (não a senha normal)

Para criar token: GitHub > Settings > Developer settings > Personal access tokens > Generate new token

---

## 📋 Checklist

- [ ] Repositório criado no GitHub ✅
- [ ] Git instalado OU GitHub Desktop instalado
- [ ] Arquivos publicados no GitHub
- [ ] GitHub Pages ativado
- [ ] Dashboard acessível online

---

## 🔗 Links Úteis

- **Repositório**: https://github.com/alinecasagrande-rgb/dashboard-rh
- **Dashboard Online**: https://alinecasagrande-rgb.github.io/dashboard-rh (após ativar Pages)
- **GitHub Desktop**: https://desktop.github.com/
- **Git para Windows**: https://git-scm.com/download/win

---

## ❓ Precisa de Ajuda?

Se encontrar problemas:
1. **Git não funciona**: Use GitHub Desktop (Opção 1)
2. **Erro de autenticação**: Crie um Personal Access Token
3. **Dashboard não aparece**: Aguarde 5-10 minutos após ativar Pages

