# 🔄 Atualização Automática do Dashboard - Guia Completo

## 📋 Situação Atual

**IMPORTANTE:** Atualmente, o dashboard **NÃO atualiza automaticamente** quando você modifica a planilha do Google Sheets.

### Como Funciona Hoje (Processo Manual):

```
┌─────────────────────┐
│  Google Sheets      │
│  (Planilha)         │
└──────────┬──────────┘
           │
           │ Você atualiza os dados
           ▼
┌─────────────────────┐
│  Seu Computador     │
│  - Executa script   │
│  - Atualiza JSON    │
└──────────┬──────────┘
           │
           │ Você faz commit e push
           ▼
┌─────────────────────┐
│  GitHub             │
│  - Recebe dados.json│
│  - GitHub Pages     │
│    atualiza         │
└─────────────────────┘
```

**Problema:** Você precisa fazer tudo manualmente:
1. ✅ Você atualiza a planilha do Google Sheets
2. ❌ O dashboard no GitHub **NÃO atualiza automaticamente**
3. ⚙️ Você precisa executar manualmente:
   - `ATUALIZAR_DADOS.bat` (ou `python processar_dados_final.py`)
   - Fazer commit e push do `dados.json` atualizado

---

## 🚀 Solução: GitHub Actions (Atualização Automática)

Criei um arquivo `.github/workflows/atualizar-dados.yml` que permite atualização automática!

### Como Funciona (Processo Automático):

```
┌─────────────────────┐
│  Google Sheets      │
│  (Planilha)         │
└──────────┬──────────┘
           │
           │ Você atualiza os dados
           │ (ou aguarda horário agendado)
           ▼
┌─────────────────────┐
│  GitHub Actions     │
│  (Servidor Cloud)   │
│  - Executa script   │
│  - Baixa dados      │
│  - Processa JSON    │
└──────────┬──────────┘
           │
           │ Commit e push automático
           ▼
┌─────────────────────┐
│  GitHub             │
│  - Recebe dados.json│
│  - GitHub Pages     │
│    atualiza (5-10min)│
└─────────────────────┘
```

### Fluxo Detalhado Passo a Passo:

1. **Execução Automática Diária**: 
   - O GitHub Actions executa o script diariamente às 8h (horário de Brasília)
   - Você não precisa fazer nada!

2. **Execução Manual**: 
   - Você pode executar manualmente quando quiser através da interface do GitHub

3. **Processo Automático Completo**:
   - ✅ **Passo 1**: GitHub Actions baixa o código do repositório
   - ✅ **Passo 2**: Configura Python no servidor
   - ✅ **Passo 3**: Executa `processar_dados_final.py`
   - ✅ **Passo 4**: Script baixa dados do Google Sheets (via CSV público)
   - ✅ **Passo 5**: Script processa e atualiza `dados.json`
   - ✅ **Passo 6**: GitHub Actions verifica se houve mudanças
   - ✅ **Passo 7**: Se houver mudanças, faz commit e push automaticamente
   - ✅ **Passo 8**: GitHub Pages detecta a mudança e atualiza o site (5-10 minutos)

### Como Ativar (Passo a Passo Detalhado):

#### **Passo 1: Preparar o Ambiente Local**

1. Abra o PowerShell na pasta do projeto:
   - Pressione `Shift + Botão Direito` na pasta
   - Selecione "Abrir janela do PowerShell aqui"

2. Verifique se o Git está instalado:
   ```powershell
   git --version
   ```
   Se não estiver instalado, baixe em: https://git-scm.com/download/win

3. Verifique se está conectado ao repositório:
   ```powershell
   git remote -v
   ```
   Deve mostrar a URL do seu repositório GitHub.

#### **Passo 2: Adicionar o Workflow ao Repositório**

1. **Adicione o arquivo de workflow:**
   ```powershell
   git add .github/workflows/atualizar-dados.yml
   git add ATUALIZACAO_AUTOMATICA.md
   ```

2. **Faça o commit:**
   ```powershell
   git commit -m "Adicionar atualização automática de dados via GitHub Actions"
   ```

3. **Envie para o GitHub:**
   ```powershell
   git push
   ```

#### **Passo 3: Ativar GitHub Actions (Primeira Vez)**

1. Acesse seu repositório no GitHub (ex: `https://github.com/seu-usuario/dashboard-rh`)

2. Clique na aba **"Actions"** (no topo do repositório)

3. Se aparecer uma mensagem sobre habilitar Actions:
   - Clique em **"I understand my workflows, go ahead and enable them"**
   - Ou vá em **Settings → Actions → General** e habilite "Allow all actions"

4. Você verá o workflow **"Atualizar Dados do Google Sheets"** na lista

#### **Passo 4: Testar Execução Manual (Recomendado)**

1. Na aba **Actions**, clique no workflow **"Atualizar Dados do Google Sheets"**

2. Clique no botão **"Run workflow"** (canto superior direito)

3. Selecione a branch **"main"** (ou "master")

4. Clique em **"Run workflow"** novamente

5. Aguarde alguns minutos e verifique:
   - O workflow deve aparecer como "em execução" (amarelo)
   - Após alguns minutos, deve ficar verde (sucesso) ou vermelho (erro)
   - Clique na execução para ver os logs detalhados

#### **Passo 5: Verificar se Funcionou**

1. Após o workflow executar com sucesso:
   - Vá na aba **"Code"** do repositório
   - Verifique se o arquivo `dados.json` foi atualizado (última modificação recente)
   - Clique em `dados.json` para ver o conteúdo

2. Aguarde 5-10 minutos e acesse seu dashboard no GitHub Pages:
   - URL: `https://seu-usuario.github.io/nome-repositorio`
   - Os dados devem estar atualizados!

#### **Passo 6: Configurar Horário (Opcional)**

O workflow está configurado para executar **diariamente às 8h** (horário de Brasília).

Para alterar o horário:

1. Edite o arquivo `.github/workflows/atualizar-dados.yml`

2. Localize a linha:
   ```yaml
   - cron: '0 11 * * *'
   ```

3. O formato cron é: `minuto hora dia mês dia-da-semana` (horário UTC)

   **Exemplos:**
   - `'0 11 * * *'` = 8h da manhã (Brasília, UTC-3)
   - `'0 14 * * *'` = 11h da manhã (Brasília, UTC-3)
   - `'0 20 * * *'` = 17h da tarde (Brasília, UTC-3)
   - `'0 */6 * * *'` = A cada 6 horas
   - `'0 * * * *'` = A cada hora
   - `'*/30 * * * *'` = A cada 30 minutos

4. **Importante:** Horário UTC = Horário de Brasília - 3 horas
   - Se quiser 8h da manhã em Brasília → use `'0 11 * * *'` (11h UTC)
   - Se quiser 9h da manhã em Brasília → use `'0 12 * * *'` (12h UTC)

5. Salve, faça commit e push:
   ```powershell
   git add .github/workflows/atualizar-dados.yml
   git commit -m "Ajustar horário de atualização automática"
   git push
   ```

---

## 🔍 Explicação Técnica Detalhada do Workflow

Vamos entender **linha por linha** como funciona o arquivo `.github/workflows/atualizar-dados.yml`:

### Estrutura do Arquivo:

```yaml
name: Atualizar Dados do Google Sheets
```
**O que faz:** Define o nome do workflow que aparece na interface do GitHub.

```yaml
on:
  schedule:
    - cron: '0 11 * * *'
  workflow_dispatch:
```
**O que faz:** Define **quando** o workflow executa:
- `schedule`: Executa automaticamente no horário agendado (cron)
- `workflow_dispatch`: Permite executar manualmente pela interface do GitHub

```yaml
jobs:
  atualizar-dados:
    runs-on: ubuntu-latest
```
**O que faz:** Define o "trabalho" (job) que será executado:
- `runs-on: ubuntu-latest`: Usa um servidor Linux (gratuito do GitHub)

```yaml
steps:
  - name: Checkout código
    uses: actions/checkout@v3
```
**O que faz:** Baixa o código do repositório para o servidor.
- É como fazer um `git clone` no servidor do GitHub

```yaml
  - name: Configurar Python
    uses: actions/setup-python@v4
    with:
      python-version: '3.11'
```
**O que faz:** Instala Python 3.11 no servidor.
- Necessário para executar o script `processar_dados_final.py`

```yaml
  - name: Baixar e processar dados do Google Sheets
    run: |
      python processar_dados_final.py
```
**O que faz:** Executa o script Python que:
1. Baixa os dados do Google Sheets (via URL CSV pública)
2. Processa os dados
3. Atualiza o arquivo `dados.json` localmente no servidor

```yaml
  - name: Verificar se dados.json foi modificado
    id: verificar-mudancas
    run: |
      if [ -n "$(git status --porcelain dados.json)" ]; then
        echo "changed=true" >> $GITHUB_OUTPUT
      else
        echo "changed=false" >> $GITHUB_OUTPUT
      fi
```
**O que faz:** Verifica se o arquivo `dados.json` foi modificado:
- Se foi modificado → `changed=true`
- Se não foi modificado → `changed=false`
- Isso evita fazer commits desnecessários quando não há mudanças

```yaml
  - name: Commit e Push das mudanças
    if: steps.verificar-mudancas.outputs.changed == 'true'
    run: |
      git config --local user.email "action@github.com"
      git config --local user.name "GitHub Action"
      git add dados.json
      git commit -m "Atualização automática de dados do Google Sheets [skip ci]"
      git push
```
**O que faz:** Se houve mudanças, faz commit e push:
- `if: ...`: Só executa se `changed == 'true'`
- Configura o Git (nome e email do "autor" do commit)
- Adiciona `dados.json` ao staging
- Faz commit com mensagem automática
- `[skip ci]`: Evita que este commit dispare outro workflow (evita loop infinito)
- Faz push para o repositório

### Fluxo Completo de Execução:

```
1. GitHub detecta horário agendado (ou você clica "Run workflow")
   ↓
2. Cria servidor Linux temporário (gratuito)
   ↓
3. Baixa código do repositório (git checkout)
   ↓
4. Instala Python 3.11
   ↓
5. Executa: python processar_dados_final.py
   ├─ Baixa CSV do Google Sheets
   ├─ Processa dados
   └─ Atualiza dados.json
   ↓
6. Verifica se dados.json mudou
   ↓
7. Se mudou:
   ├─ Configura Git
   ├─ git add dados.json
   ├─ git commit
   └─ git push
   ↓
8. GitHub Pages detecta mudança (5-10 minutos)
   ↓
9. Dashboard atualizado! ✅
```

---

## ⚙️ Outras Opções de Atualização

### Opção 1: Webhook do Google Sheets (Avançado)

Você pode configurar um webhook que dispara quando a planilha é atualizada:

**Como funciona:**
```
Google Sheets atualizado
    ↓
Webhook dispara (Zapier/Make.com/n8n)
    ↓
Chama API do GitHub para executar workflow
    ↓
Workflow executa imediatamente
    ↓
Dashboard atualizado em minutos
```

**Passo a passo:**

1. **Criar Personal Access Token no GitHub:**
   - Vá em: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Clique em "Generate new token"
   - Dê permissão: `repo` (acesso completo ao repositório)
   - Copie o token gerado (guarde com segurança!)

2. **Configurar no Zapier/Make.com:**
   - **Trigger:** "Google Sheets - New or Updated Row"
   - **Action:** "GitHub - Trigger Workflow"
   - Configure:
     - Repository: seu-usuario/dashboard-rh
     - Workflow: atualizar-dados.yml
     - Token: o token que você criou

3. **Vantagens:**
   - ✅ Atualização imediata (não precisa esperar horário agendado)
   - ✅ Só executa quando há mudanças reais

4. **Desvantagens:**
   - ❌ Requer conta paga em Zapier/Make.com (ou limite gratuito)
   - ❌ Mais complexo de configurar
   - ❌ Precisa gerenciar token de acesso

### Opção 2: Atualização Manual (Atual)

Continue usando o processo manual quando precisar de atualização imediata:

**Processo:**
1. Execute `ATUALIZAR_DADOS.bat` (ou `python processar_dados_final.py`)
2. Verifique se `dados.json` foi atualizado
3. Faça commit e push:
   ```powershell
   git add dados.json
   git commit -m "Atualização manual de dados"
   git push
   ```

**Quando usar:**
- Quando você precisa atualizar imediatamente
- Quando o workflow automático falhou
- Para testar se os dados estão corretos antes de publicar

### Opção 3: Atualização Mais Frequente

Edite o workflow para executar mais vezes:

**Exemplos de configuração cron:**

| Frequência | Cron | Descrição |
|------------|------|-----------|
| Diário 8h | `'0 11 * * *'` | Uma vez por dia às 8h (Brasília) |
| Diário 9h | `'0 12 * * *'` | Uma vez por dia às 9h (Brasília) |
| A cada 6h | `'0 */6 * * *'` | 4 vezes por dia (0h, 6h, 12h, 18h UTC) |
| A cada 3h | `'0 */3 * * *'` | 8 vezes por dia |
| A cada hora | `'0 * * * *'` | 24 vezes por dia |
| A cada 30min | `'*/30 * * * *'` | 48 vezes por dia |

**⚠️ Atenção:**
- GitHub Actions tem limite de 2000 minutos/mês no plano gratuito
- Executar muito frequentemente pode esgotar o limite
- Recomendação: máximo 1 vez por hora para planos gratuitos

**Como alterar:**

1. Edite `.github/workflows/atualizar-dados.yml`
2. Altere a linha do cron:
   ```yaml
   schedule:
     - cron: '0 */6 * * *'  # A cada 6 horas
   ```
3. Faça commit e push

---

## 📝 Resumo

| Método | Automático? | Frequência | Complexidade |
|--------|------------|------------|--------------|
| **Manual** | ❌ Não | Quando você quiser | ⭐ Fácil |
| **GitHub Actions (agendado)** | ✅ Sim | Diário (configurável) | ⭐⭐ Médio |



---

## ✅ Recomendação

**Use o GitHub Actions** (já configurado):
- ✅ Atualiza automaticamente
- ✅ Não precisa fazer nada manualmente
- ✅ Funciona 24/7
- ✅ Você pode executar manualmente quando quiser

Basta fazer commit e push do arquivo `.github/workflows/atualizar-dados.yml`!

---

## 🆘 Troubleshooting Detalhado

### Problema 1: O workflow não executa automaticamente

**Sintomas:**
- Workflow não aparece na aba Actions
- Workflow não executa no horário agendado

**Soluções:**

1. **Verificar se o arquivo existe:**
   ```powershell
   # No PowerShell, verifique se o arquivo existe:
   Test-Path .github\workflows\atualizar-dados.yml
   ```
   Deve retornar `True`. Se retornar `False`, o arquivo não foi commitado.

2. **Verificar se foi commitado e enviado:**
   ```powershell
   git log --oneline --all -- .github/workflows/atualizar-dados.yml
   ```
   Deve mostrar o commit que adicionou o arquivo.

3. **Verificar se Actions está habilitado:**
   - Vá em: GitHub → Seu Repositório → Settings → Actions → General
   - Verifique se "Allow all actions and reusable workflows" está selecionado
   - Clique em "Save"

4. **Verificar permissões do repositório:**
   - Se o repositório é privado, verifique se tem Actions habilitado
   - Repositórios privados têm limite de minutos gratuitos

5. **Verificar horário do cron:**
   - O horário está em UTC, não em horário local
   - Use um conversor online: https://crontab.guru
   - Exemplo: `'0 11 * * *'` = 11h UTC = 8h Brasília (UTC-3)

### Problema 2: Erro ao processar dados

**Sintomas:**
- Workflow executa mas falha
- Mensagem de erro nos logs

**Soluções:**

1. **Verificar link do Google Sheets:**
   - Abra `processar_dados_final.py`
   - Verifique a linha com `CSV_URL`
   - O link deve terminar com `?output=csv`
   - Teste o link no navegador (deve baixar um arquivo CSV)

2. **Verificar se a planilha está pública:**
   - No Google Sheets, clique em "Compartilhar"
   - Deve estar como "Qualquer pessoa com o link pode visualizar"
   - Ou configure como "Público na web"

3. **Verificar estrutura da planilha:**
   - A planilha deve ter as seções esperadas:
     - "Colaboradores por Estabelecimento"
     - "Admitidos por Estabelecimento"
     - "Desligamentos por Estabelecimento"
   - Verifique se os nomes das seções estão corretos

4. **Verificar logs do workflow:**
   - Vá em: Actions → Clique na execução que falhou
   - Expanda o step "Baixar e processar dados"
   - Leia a mensagem de erro completa
   - Copie o erro e verifique o que está errado

### Problema 3: Dados não aparecem atualizados no dashboard

**Sintomas:**
- Workflow executa com sucesso
- `dados.json` foi atualizado no GitHub
- Mas o dashboard ainda mostra dados antigos

**Soluções:**

1. **Aguardar atualização do GitHub Pages:**
   - GitHub Pages pode levar 5-10 minutos para atualizar
   - Aguarde e tente novamente

2. **Limpar cache do navegador:**
   - Pressione `Ctrl + Shift + Delete`
   - Ou `Ctrl + F5` para recarregar forçando cache
   - Ou abra em aba anônima/privada

3. **Verificar se dados.json foi realmente atualizado:**
   - Vá em: GitHub → Seu Repositório → Code → dados.json
   - Clique em "History" (ícone de relógio)
   - Verifique se há commit recente do GitHub Action
   - Clique no commit mais recente e veja as mudanças

4. **Verificar URL do dashboard:**
   - Certifique-se de estar acessando a URL correta do GitHub Pages
   - Formato: `https://seu-usuario.github.io/nome-repositorio`
   - Verifique em: Settings → Pages → "Your site is published at..."

5. **Verificar se há erros no console do navegador:**
   - Abra o dashboard
   - Pressione `F12` (Ferramentas do Desenvolvedor)
   - Vá na aba "Console"
   - Procure por erros em vermelho
   - Se houver erro ao carregar `dados.json`, verifique o caminho

### Problema 4: Workflow executa mas não faz commit

**Sintomas:**
- Workflow executa com sucesso (verde)
- Mas `dados.json` não é atualizado no repositório

**Soluções:**

1. **Verificar se houve mudanças reais:**
   - O workflow só faz commit se os dados mudaram
   - Se você atualizou a planilha mas os dados são os mesmos, não haverá commit
   - Verifique os logs do workflow para ver "changed=false"

2. **Verificar permissões do token:**
   - O workflow usa o token padrão do GitHub Actions
   - Verifique se Actions tem permissão para fazer push
   - Vá em: Settings → Actions → General → Workflow permissions
   - Deve estar como "Read and write permissions"

3. **Verificar se há conflitos:**
   - Se alguém fez commit manual enquanto o workflow executava
   - Pode haver conflito
   - Verifique os logs do workflow para mensagens de erro

### Problema 5: Limite de minutos do GitHub Actions esgotado

**Sintomas:**
- Workflow não executa
- Mensagem sobre limite de minutos

**Soluções:**

1. **Verificar uso atual:**
   - Vá em: GitHub → Settings → Billing
   - Veja quantos minutos foram usados este mês
   - Plano gratuito: 2000 minutos/mês

2. **Reduzir frequência:**
   - Altere o cron para executar menos vezes
   - Exemplo: de "a cada hora" para "diário"

3. **Otimizar o workflow:**
   - O workflow atual é otimizado
   - Não executa commit se não houver mudanças
   - Não há muito o que otimizar além de reduzir frequência

4. **Upgrade do plano (se necessário):**
   - GitHub Pro: $4/mês com mais minutos
   - Ou aguarde o próximo mês (limite reseta)

### Problema 6: Erro de autenticação ao fazer push

**Sintomas:**
- Workflow falha no step "Commit e Push"
- Erro: "Permission denied" ou "Authentication failed"

**Soluções:**

1. **Verificar permissões do workflow:**
   - Vá em: Settings → Actions → General
   - Em "Workflow permissions", selecione:
     - ✅ "Read and write permissions"
     - ✅ "Allow GitHub Actions to create and approve pull requests"

2. **Verificar se o repositório permite pushes:**
   - Verifique se não há branch protection rules bloqueando
   - Vá em: Settings → Branches
   - Verifique regras de proteção da branch main

### Como Ver Logs Detalhados:

1. Vá em: GitHub → Seu Repositório → Actions
2. Clique na execução do workflow (sucesso ou falha)
3. Expanda cada step para ver os logs
4. Procure por mensagens em vermelho (erros)
5. Copie mensagens de erro para investigar

### Contato e Suporte:

Se nenhuma solução funcionar:
1. Verifique a documentação oficial: https://docs.github.com/en/actions
2. Procure por problemas similares no GitHub Discussions
3. Verifique se há atualizações nas Actions do GitHub

---

## ❓ Perguntas Frequentes (FAQ)

### P1: O workflow consome muito do limite gratuito do GitHub?

**Resposta:**
- Cada execução leva aproximadamente 1-2 minutos
- Executando 1 vez por dia = ~60 minutos/mês
- Plano gratuito tem 2000 minutos/mês
- **Conclusão:** Você pode executar diariamente sem problemas!

### P2: Posso executar o workflow em múltiplos horários?

**Resposta:**
Sim! Adicione múltiplas linhas no cron:
```yaml
schedule:
  - cron: '0 11 * * *'  # 8h da manhã
  - cron: '0 20 * * *'  # 17h da tarde
```

### P3: O que acontece se eu atualizar a planilha enquanto o workflow está executando?

**Resposta:**
- O workflow baixa os dados no momento que executa
- Se você atualizar durante a execução, a atualização será capturada na próxima execução
- Não há problema, apenas aguarde a próxima execução

### P4: Posso desabilitar a atualização automática temporariamente?

**Resposta:**
Sim, duas opções:

**Opção 1:** Comentar o schedule no workflow:
```yaml
on:
  # schedule:
  #   - cron: '0 11 * * *'  # Desabilitado temporariamente
  workflow_dispatch:
```

**Opção 2:** Desabilitar Actions no repositório:
- Settings → Actions → General
- Desmarque "Allow all actions"

### P5: Como sei se o workflow executou com sucesso?

**Resposta:**
1. Vá em: Actions → "Atualizar Dados do Google Sheets"
2. Verifique a última execução:
   - ✅ Verde = Sucesso
   - ❌ Vermelho = Erro
   - 🟡 Amarelo = Em execução
3. Clique na execução para ver detalhes

### P6: O dashboard atualiza imediatamente após o workflow?

**Resposta:**
Não imediatamente. O processo completo leva:
- Workflow executa: 1-2 minutos
- Commit e push: alguns segundos
- GitHub Pages atualiza: 5-10 minutos
- **Total:** ~10-15 minutos após o workflow iniciar

### P7: Posso usar isso em repositório privado?

**Resposta:**
Sim! Mas:
- Repositórios privados têm limite de 2000 minutos/mês no plano gratuito
- Repositórios públicos têm limite ilimitado
- Funciona igual em ambos

### P8: O que acontece se o script Python falhar?

**Resposta:**
- O workflow marca como "falhou" (vermelho)
- Nenhum commit é feito
- Os dados antigos permanecem
- Você recebe notificação por email (se configurado)
- Verifique os logs para ver o erro

### P9: Posso adicionar notificações quando o dashboard atualizar?

**Resposta:**
Sim! Adicione um step no workflow para enviar email/notificação:

```yaml
- name: Enviar notificação
  if: steps.verificar-mudancas.outputs.changed == 'true'
  run: |
    # Exemplo usando curl para webhook (Discord, Slack, etc.)
    curl -X POST "URL_DO_WEBHOOK" \
      -H "Content-Type: application/json" \
      -d '{"message": "Dashboard atualizado com sucesso!"}'
```

### P10: Como faço backup dos dados antes de atualizar?

**Resposta:**
O Git já faz isso automaticamente! Cada commit mantém histórico:
- Vá em: GitHub → dados.json → History
- Você pode ver todas as versões anteriores
- Pode reverter se necessário

---

## 📊 Exemplos Práticos

### Exemplo 1: Configurar para atualizar 2x por dia

**Objetivo:** Atualizar às 8h e às 18h (horário de Brasília)

**Solução:**
```yaml
on:
  schedule:
    - cron: '0 11 * * *'  # 8h Brasília (11h UTC)
    - cron: '0 21 * * *'  # 18h Brasília (21h UTC)
  workflow_dispatch:
```

### Exemplo 2: Atualizar apenas em dias úteis

**Objetivo:** Atualizar de segunda a sexta às 8h

**Solução:**
```yaml
on:
  schedule:
    - cron: '0 11 * * 1-5'  # Segunda (1) a Sexta (5) às 8h
  workflow_dispatch:
```

**Nota:** No cron, domingo = 0 ou 7, segunda = 1, ..., sábado = 6

### Exemplo 3: Atualizar a cada 4 horas

**Objetivo:** Manter dados sempre atualizados durante o dia

**Solução:**
```yaml
on:
  schedule:
    - cron: '0 */4 * * *'  # A cada 4 horas
  workflow_dispatch:
```

**Cuidado:** Isso usa ~360 minutos/mês (ainda dentro do limite gratuito)

### Exemplo 4: Verificar se atualizou corretamente

**Passo a passo:**
1. Anote um valor atual do dashboard (ex: Total de colaboradores = 150)
2. Atualize a planilha Google Sheets (mude para 155)
3. Execute o workflow manualmente
4. Aguarde 10-15 minutos
5. Recarregue o dashboard (Ctrl+F5)
6. Verifique se o valor mudou para 155

### Exemplo 5: Reverter atualização incorreta

**Se os dados ficaram errados:**
1. Vá em: GitHub → dados.json → History
2. Clique no commit anterior (antes do erro)
3. Clique em "Browse files"
4. Copie o conteúdo do dados.json
5. Faça commit manual com os dados corretos:
   ```powershell
   # Cole o conteúdo correto no dados.json
   git add dados.json
   git commit -m "Reverter dados incorretos"
   git push
   ```

---

## 📚 Recursos Adicionais

### Documentação Oficial:
- **GitHub Actions:** https://docs.github.com/en/actions
- **Cron Syntax:** https://crontab.guru
- **Python no GitHub Actions:** https://github.com/actions/setup-python

### Ferramentas Úteis:
- **Conversor de Horário UTC:** https://www.timeanddate.com/worldclock/converter.html
- **Validador de Cron:** https://crontab.guru
- **GitHub Actions Status:** https://www.githubstatus.com

### Tutoriais Relacionados:
- Como configurar notificações por email
- Como adicionar testes automatizados
- Como fazer deploy em múltiplos ambientes

---

## ✅ Checklist de Configuração

Use este checklist para garantir que tudo está configurado corretamente:

- [ ] Arquivo `.github/workflows/atualizar-dados.yml` existe
- [ ] Arquivo foi commitado e enviado ao GitHub
- [ ] GitHub Actions está habilitado no repositório
- [ ] Workflow aparece na aba Actions
- [ ] Teste manual executado com sucesso
- [ ] `dados.json` foi atualizado após teste
- [ ] Dashboard mostra dados atualizados
- [ ] Horário do cron está correto (verificado com conversor)
- [ ] Planilha Google Sheets está pública
- [ ] Link CSV está correto no script Python
- [ ] Permissões do workflow estão corretas (read/write)

---

**Pronto!** Agora você tem um guia completo e detalhado sobre atualização automática do dashboard! 🎉

