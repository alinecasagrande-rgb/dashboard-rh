# 🚀 Como Publicar o Dashboard no GitHub

Este guia vai te ajudar a publicar o dashboard no GitHub para que seu diretor tenha acesso.

## 📋 Pré-requisitos

1. **Conta no GitHub**: Se não tiver, crie em [github.com](https://github.com)
2. **Git instalado**: Baixe em [git-scm.com](https://git-scm.com/download/win)

## 🔧 Passo 1: Instalar o Git (se necessário)

1. Baixe o Git para Windows: https://git-scm.com/download/win
2. Execute o instalador (aceite as opções padrão)
3. Reinicie o terminal/PowerShell após instalar

## 📦 Passo 2: Configurar o Git (primeira vez)

Abra o PowerShell ou Git Bash e execute:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@exemplo.com"
```

## 🗂️ Passo 3: Criar Repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login
2. Clique no botão **"+"** no canto superior direito
3. Selecione **"New repository"**
4. Preencha:
   - **Repository name**: `dashboard-rh` (ou outro nome)
   - **Description**: "Dashboard de Recursos Humanos"
   - **Visibility**: Escolha **Public** (para GitHub Pages grátis) ou **Private**
   - **NÃO marque** "Initialize with README" (já temos arquivos)
5. Clique em **"Create repository"**

## 📤 Passo 4: Publicar os Arquivos

### Opção A: Usando PowerShell (Windows)

1. Abra o PowerShell na pasta do projeto:
   - Pressione `Shift + Botão Direito` na pasta
   - Selecione "Abrir janela do PowerShell aqui"

2. Execute os comandos abaixo (um por vez):

```powershell
# Inicializar o repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Primeira versão do Dashboard de RH"

# Adicionar o repositório remoto (substitua SEU-USUARIO e NOME-REPO)
git remote add origin https://github.com/SEU-USUARIO/NOME-REPO.git

# Enviar para o GitHub
git branch -M main
git push -u origin main
```

**⚠️ IMPORTANTE**: Substitua `SEU-USUARIO` e `NOME-REPO` pelos valores reais do seu repositório.

**Exemplo**: Se seu usuário é `joaosilva` e o repositório é `dashboard-rh`:
```powershell
git remote add origin https://github.com/joaosilva/dashboard-rh.git
```

### Opção B: Usando GitHub Desktop (Mais Fácil)

1. Baixe o GitHub Desktop: https://desktop.github.com/
2. Instale e faça login com sua conta GitHub
3. Clique em **"File" > "Add Local Repository"**
4. Selecione a pasta do dashboard
5. Clique em **"Publish repository"**
6. Escolha o nome e visibilidade
7. Clique em **"Publish Repository"**

## 🌐 Passo 5: Ativar GitHub Pages (Hospedar o Dashboard)

1. No repositório do GitHub, clique em **"Settings"** (Configurações)
2. No menu lateral, clique em **"Pages"**
3. Em **"Source"**, selecione **"Deploy from a branch"**
4. Escolha a branch **"main"** e pasta **"/ (root)"**
5. Clique em **"Save"**
6. Aguarde alguns minutos
7. Seu dashboard estará disponível em:
   `https://SEU-USUARIO.github.io/NOME-REPO`

## 🔄 Passo 6: Atualizar o Dashboard (Futuro)

Sempre que fizer alterações:

```powershell
# Adicionar mudanças
git add .

# Fazer commit
git commit -m "Descrição das mudanças"

# Enviar para o GitHub
git push
```

O GitHub Pages atualiza automaticamente em alguns minutos.

## 📝 Arquivos Importantes

- ✅ `index.html` - Página principal
- ✅ `dashboard.js` - Lógica do dashboard
- ✅ `dados.json` - Dados (será atualizado)
- ✅ `logo.png` - Logo da empresa
- ✅ `README.md` - Documentação

## ⚠️ Observações Importantes

1. **Dados Sensíveis**: O arquivo `dados.json` contém dados da empresa. Se o repositório for público, considere:
   - Tornar o repositório privado, OU
   - Não versionar o `dados.json` (adicionar ao `.gitignore`)

2. **Atualização de Dados**: Para atualizar os dados no GitHub:
   - Execute `ATUALIZAR_DADOS.bat` localmente
   - Faça commit e push do `dados.json` atualizado

3. **Acesso do Diretor**: 
   - Se o repositório for público: qualquer um pode ver
   - Se for privado: adicione o diretor como colaborador em Settings > Collaborators

## 🆘 Problemas Comuns

### Erro: "git não é reconhecido"
- **Solução**: Instale o Git (Passo 1)

### Erro: "Authentication failed"
- **Solução**: Use GitHub Desktop ou configure token de acesso pessoal

### Erro: "Repository not found"
- **Solução**: Verifique se o nome do repositório está correto

### Dashboard não aparece no GitHub Pages
- **Solução**: Aguarde 5-10 minutos e verifique se o arquivo `index.html` está na raiz

## 📞 Precisa de Ajuda?

Se encontrar problemas, verifique:
1. Se o Git está instalado: `git --version`
2. Se está logado no GitHub
3. Se o repositório foi criado corretamente
4. Se os arquivos foram enviados: verifique na aba "Code" do GitHub

---

**Pronto!** Seu dashboard agora está no GitHub e pode ser acessado pelo seu diretor! 🎉


