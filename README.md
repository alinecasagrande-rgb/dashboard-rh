# 📊 Dashboard de Recursos Humanos

Dashboard executivo interativo para visualização de indicadores estratégicos de RH.

## 🚀 Acesso Rápido

### Opção 1: GitHub Pages (Recomendado)
Acesse o dashboard diretamente pelo navegador através do GitHub Pages:
**https://[seu-usuario].github.io/[nome-do-repositorio]**

### Opção 2: Local
1. Clone o repositório
2. Execute `ABRIR_DASHBOARD.bat` (Windows)
3. O dashboard abrirá automaticamente no navegador

## 📋 Funcionalidades

- **Visão Geral**: KPIs principais e gráficos consolidados
- **Colaboradores**: Evolução do quadro de colaboradores
- **Movimentação**: Admissões e desligamentos
- **Detalhes por Estabelecimento**: Análise detalhada por unidade
- **Por Gerente**: Evolução por gerente responsável
- **Por Segmento**: Análise por segmento de negócio
- **Turnover**: Indicadores de rotatividade

## 🔄 Atualização de Dados

### Método Automático (Recomendado)
1. Atualize os dados na planilha do Google Sheets
2. Execute `ATUALIZAR_DADOS.bat`
3. Os dados serão atualizados automaticamente

### Método Manual
1. Edite o arquivo `dados.json` diretamente
2. Siga o formato JSON existente

## 📁 Estrutura do Projeto

```
├── index.html              # Página principal do dashboard
├── dashboard.js            # Lógica JavaScript do dashboard
├── dados.json              # Dados do dashboard (JSON)
├── logo.png                # Logo da empresa
├── servidor_local.py       # Servidor local para desenvolvimento
├── processar_dados_final.py # Script para atualizar dados do Google Sheets
├── ABRIR_DASHBOARD.bat     # Atalho para abrir o dashboard
└── ATUALIZAR_DADOS.bat     # Atalho para atualizar dados
```

## 🛠️ Requisitos

- Python 3.7+ (para scripts de atualização)
- Navegador moderno (Chrome, Firefox, Edge, Safari)
- Conexão com internet (para carregar bibliotecas externas)

## 📖 Documentação Adicional

- `LEIA_ME_PRIMEIRO.txt` - Instruções iniciais
- `INICIO_RAPIDO.txt` - Guia rápido de uso
- `COMO_ABRIR_DASHBOARD.md` - Como abrir o dashboard
- `COMO_ATUALIZAR_DO_GOOGLE_SHEETS.md` - Como atualizar dados
- `COMO_ADICIONAR_LOGO.md` - Como adicionar logo da empresa

## 🔧 Tecnologias Utilizadas

- HTML5 / CSS3
- JavaScript (ES6+)
- Chart.js (gráficos)
- Tailwind CSS (estilização)
- Font Awesome (ícones)

## 📝 Licença

Uso interno da empresa.

## 👥 Suporte

Para dúvidas ou problemas, consulte a documentação na pasta do projeto ou entre em contato com a equipe de TI.


