"""
Script para importar dados do Google Sheets e atualizar dados.json
"""
import json
import urllib.request
import csv
import io

# Link CSV da planilha (convertido do link HTML)
CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSf71N2ZusoPVlFxeAwG0yLMRQi3rMiYsf422EnY-zU-NrGf3y142prw-9_kOyXfNrsDQ3kkxKF09uw/pub?output=csv"

def baixar_dados_csv():
    """Baixa os dados do Google Sheets em formato CSV"""
    try:
        print("Baixando dados do Google Sheets...")
        with urllib.request.urlopen(CSV_URL) as response:
            csv_data = response.read().decode('utf-8')
        print("Dados baixados com sucesso!")
        return csv_data
    except Exception as e:
        print(f"Erro ao baixar dados: {e}")
        return None

def processar_csv(csv_data):
    """Processa os dados CSV e retorna como lista de dicionários"""
    reader = csv.DictReader(io.StringIO(csv_data))
    dados = list(reader)
    print(f"{len(dados)} linhas processadas")
    return dados

def atualizar_dados_json(dados_csv):
    """Atualiza o arquivo dados.json com os novos dados"""
    try:
        # Carrega o arquivo atual
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        print("\nProcessando dados da planilha...")
        print(f"Estrutura dos dados recebidos: {list(dados_csv[0].keys()) if dados_csv else 'Nenhum dado'}")
        
        # Aqui você precisa mapear os dados do CSV para a estrutura do JSON
        # Isso depende da estrutura exata da sua planilha
        
        # Exemplo de como processar (ajuste conforme sua planilha):
        # - Identificar qual coluna tem os meses
        # - Identificar qual coluna tem os estabelecimentos
        # - Mapear colaboradores, admissões, desligamentos
        
        print("\nMapeamento necessario:")
        print("Por favor, me mostre a estrutura dos dados da planilha para eu poder mapear corretamente.")
        
        # Salva o arquivo (mesmo que não tenha sido atualizado ainda)
        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        
        return dados_csv
        
    except Exception as e:
        print(f"Erro ao processar dados: {e}")
        return None

def main():
    print("=" * 60)
    print("Importador de Dados do Google Sheets")
    print("=" * 60)
    
    # Baixa os dados
    csv_data = baixar_dados_csv()
    if not csv_data:
        return
    
    # Processa o CSV
    dados_csv = processar_csv(csv_data)
    if not dados_csv:
        return
    
    # Mostra uma amostra dos dados
    print("\nAmostra dos dados (primeiras 5 linhas):")
    for i, linha in enumerate(dados_csv[:5]):
        print(f"\nLinha {i+1}:")
        for chave, valor in linha.items():
            print(f"  {chave}: {valor}")
    
    # Atualiza o JSON
    atualizar_dados_json(dados_csv)
    
    print("\n" + "=" * 60)
    print("Processo concluido!")
    print("=" * 60)
    print("\nProximos passos:")
    print("1. Verifique a estrutura dos dados acima")
    print("2. Me informe como os dados estao organizados na planilha")
    print("3. Eu atualizo o mapeamento e finalizo a atualizacao")

if __name__ == "__main__":
    main()

