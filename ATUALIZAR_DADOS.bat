@echo off
chcp 65001 >nul
echo ============================================================
echo ATUALIZANDO DADOS DO DASHBOARD
echo ============================================================
echo.
echo Baixando dados do Google Sheets e atualizando dados.json...
echo.
python processar_dados_final.py
echo.
echo ============================================================
echo.
pause


