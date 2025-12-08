"""
Script para verificar problemas nos dados de admissão e gerentes
"""
import json
import urllib.request
import csv
import io

def baixar_dados_planilha():
    """Baixa os dados do Google Sheets"""
    CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSf71N2ZusoPVlFxeAwG0yLMRQi3rMiYsf422EnY-zU-NrGf3y142prw-9_kOyXfNrsDQ3kkxKF09uw/pub?output=csv"
    try:
        with urllib.request.urlopen(CSV_URL) as response:
            csv_data = response.read().decode('utf-8')
        return csv_data
    except Exception as e:
        print(f"Erro ao baixar: {e}")
        return None

def analisar_planilha(csv_data):
    """Analisa a estrutura completa da planilha"""
    linhas = csv_data.strip().split('\n')
    
    print("=" * 60)
    print("ANALISE COMPLETA DA PLANILHA")
    print("=" * 60)
    
    # Mostra todas as linhas para entender a estrutura
    print("\nTodas as linhas da planilha:")
    for i, linha in enumerate(linhas[:100], 1):  # Primeiras 100 linhas
        if linha.strip():
            print(f"{i:3d}: {linha[:150]}")

def verificar_dados_json():
    """Verifica os dados atuais no JSON"""
    with open('dados.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    print("\n" + "=" * 60)
    print("DADOS ATUAIS NO JSON")
    print("=" * 60)
    
    print(f"\nMeses: {len(dados['labels'])} meses")
    print(f"Ultimo mes: {dados['labels'][-1]}")
    
    print("\nAdmissoes por estabelecimento (novembro):")
    for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
        valor = dados['admitidos']['dados'][i][-1]
        print(f"  {estab}: {valor}")
    print(f"Total admissoes novembro: {dados['admitidos']['totais'][-1]}")
    
    print("\nDados por gerente - Colaboradores:")
    print(f"  Numero de gerentes: {len(dados['porGerenteEvolucao']['colaboradores']['labels'])}")
    print(f"  Valores por gerente: {len(dados['porGerenteEvolucao']['colaboradores']['dados'][0])} meses")
    if len(dados['porGerenteEvolucao']['colaboradores']['dados'][0]) < len(dados['labels']):
        print(f"  PROBLEMA: Gerentes tem {len(dados['porGerenteEvolucao']['colaboradores']['dados'][0])} meses, mas deveria ter {len(dados['labels'])}")
    
    print("\nDados por gerente - Admissoes:")
    print(f"  Numero de gerentes: {len(dados['porGerenteEvolucao']['admissoes']['labels'])}")
    print(f"  Valores por gerente: {len(dados['porGerenteEvolucao']['admissoes']['dados'][0])} meses")
    if len(dados['porGerenteEvolucao']['admissoes']['dados'][0]) < len(dados['labels']):
        print(f"  PROBLEMA: Admissoes por gerente tem {len(dados['porGerenteEvolucao']['admissoes']['dados'][0])} meses, mas deveria ter {len(dados['labels'])}")

def main():
    # Verifica dados JSON
    verificar_dados_json()
    
    # Baixa e analisa planilha
    print("\n" + "=" * 60)
    print("BAIXANDO PLANILHA PARA ANALISE...")
    print("=" * 60)
    csv_data = baixar_dados_planilha()
    if csv_data:
        analisar_planilha(csv_data)

if __name__ == "__main__":
    main()


