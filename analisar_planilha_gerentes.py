"""
Script para analisar a planilha e encontrar dados por gerente
"""
import urllib.request

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSf71N2ZusoPVlFxeAwG0yLMRQi3rMiYsf422EnY-zU-NrGf3y142prw-9_kOyXfNrsDQ3kkxKF09uw/pub?output=csv"

def baixar_dados():
    """Baixa os dados do Google Sheets"""
    try:
        print("Baixando dados do Google Sheets...")
        with urllib.request.urlopen(CSV_URL) as response:
            csv_data = response.read().decode('utf-8')
        return csv_data
    except Exception as e:
        print(f"Erro ao baixar dados: {e}")
        return None

def analisar_planilha(csv_data):
    """Analisa a estrutura da planilha"""
    linhas = [linha for linha in csv_data.strip().split('\n') if linha.strip()]
    
    print("=" * 60)
    print("ANALISE DA PLANILHA - PROCURANDO DADOS POR GERENTE")
    print("=" * 60)
    
    print(f"\nTotal de linhas: {len(linhas)}")
    print("\nPrimeiras 50 linhas da planilha:")
    print("-" * 60)
    
    for i, linha in enumerate(linhas[:50]):
        colunas = [c.strip() for c in linha.split(',')]
        primeira_col = colunas[0].upper() if colunas else ""
        
        # Procura por palavras-chave relacionadas a gerentes
        if 'GERENTE' in primeira_col or 'ADMISSOES' in primeira_col or 'DESLIGAMENTOS' in primeira_col:
            print(f"\n>>> LINHA {i+1} (POSSIVEL SECAO DE GERENTES):")
            print(f"    {linha[:200]}...")
        
        # Mostra algumas linhas para referência
        if i < 20:
            print(f"{i+1:3d}: {linha[:100]}")

if __name__ == "__main__":
    csv_data = baixar_dados()
    if csv_data:
        analisar_planilha(csv_data)
    else:
        print("Erro ao baixar dados da planilha")

