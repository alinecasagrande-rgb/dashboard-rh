@echo off
chcp 65001 >nul
echo ============================================================
echo PUBLICAR DASHBOARD NO GITHUB
echo ============================================================
echo.

REM Verificar se Git está instalado
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Git não está instalado!
    echo.
    echo Por favor, instale o Git primeiro:
    echo https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo [OK] Git está instalado
echo.

REM Verificar se já é um repositório Git
if exist .git (
    echo [INFO] Repositório Git já inicializado
    echo.
    echo Deseja continuar e fazer push para o GitHub? (S/N)
    set /p continuar=
    if /i not "%continuar%"=="S" (
        echo Operação cancelada.
        pause
        exit /b 0
    )
) else (
    echo [INFO] Inicializando repositório Git...
    git init
    echo [OK] Repositório inicializado
    echo.
)

echo.
echo ============================================================
echo ADICIONANDO ARQUIVOS
echo ============================================================
git add .
echo [OK] Arquivos adicionados
echo.

echo ============================================================
echo FAZENDO COMMIT
echo ============================================================
git commit -m "Atualização do Dashboard de RH" 2>nul
if errorlevel 1 (
    echo [AVISO] Nenhuma mudança para commitar
) else (
    echo [OK] Commit realizado
)
echo.

echo ============================================================
echo CONFIGURAÇÃO DO REPOSITÓRIO REMOTO
echo ============================================================
echo.
set "repo_url=https://github.com/alinecasagrande-rgb/dashboard-rh.git"
echo [INFO] Usando repositório: %repo_url%
echo.

REM Verificar se o remote já existe
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin "%repo_url%"
    echo [OK] Repositório remoto configurado
) else (
    git remote set-url origin "%repo_url%"
    echo [OK] Repositório remoto atualizado
)
echo.

echo ============================================================
echo ENVIANDO PARA O GITHUB
echo ============================================================
git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo [ERRO] Falha ao enviar para o GitHub!
    echo.
    echo Possíveis causas:
    echo 1. Repositório não existe no GitHub
    echo 2. Problemas de autenticação
    echo 3. Repositório remoto já tem conteúdo diferente
    echo.
    echo SOLUÇÃO: Use o GitHub Desktop ou configure autenticação
    echo.
) else (
    echo.
    echo ============================================================
    echo [SUCESSO] Dashboard publicado no GitHub!
    echo ============================================================
    echo.
    echo Próximos passos:
    echo 1. Acesse seu repositório no GitHub
    echo 2. Vá em Settings ^> Pages
    echo 3. Configure GitHub Pages para publicar o dashboard
    echo.
)

pause


