"""
Script completo para processar dados do Google Sheets e atualizar dados.json
"""
import json
import urllib.request
import csv
import io
import re

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSf71N2ZusoPVlFxeAwG0yLMRQi3rMiYsf422EnY-zU-NrGf3y142prw-9_kOyXfNrsDQ3kkxKF09uw/pub?output=csv"

def baixar_dados():
    """Baixa os dados do Google Sheets"""
    try:
        print("Baixando dados do Google Sheets...")
        with urllib.request.urlopen(CSV_URL) as response:
            csv_data = response.read().decode('utf-8')
        print("Dados baixados com sucesso!")
        return csv_data
    except Exception as e:
        print(f"Erro ao baixar dados: {e}")
        return None

def processar_dados_completos(csv_data):
    """Processa todos os dados da planilha"""
    linhas = csv_data.strip().split('\n')
    
    # Encontra o mês atual (primeira linha com dados)
    mes_atual = None
    dados_estabelecimentos = {}
    dados_admissoes = {}
    dados_desligamentos = {}
    dados_turnover = {}
    
    # Processa linha por linha
    secao_atual = None
    estabelecimento_atual = None
    
    for i, linha in enumerate(linhas):
        colunas = [c.strip() for c in linha.split(',')]
        
        # Detecta seções
        if len(colunas) > 0:
            primeira_col = colunas[0].upper()
            
            # Detecta mês
            if 'NOVEMBRO' in primeira_col or 'NOV' in primeira_col:
                mes_atual = 'novembro'
            
            # Detecta seções
            if 'COLABORADORES' in primeira_col and 'ESTABELECIMENTO' in primeira_col:
                secao_atual = 'colaboradores'
            elif 'ADMISSOES' in primeira_col or 'ADMISS' in primeira_col:
                secao_atual = 'admissoes'
            elif 'DESLIGAMENTOS' in primeira_col or 'DESLIG' in primeira_col:
                secao_atual = 'desligamentos'
            elif 'TURNOVER' in primeira_col:
                secao_atual = 'turnover'
            
            # Processa dados numéricos
            if colunas[0].isdigit() or colunas[0] in ['101', '102', '103', '104', '105', '106', '108', 'TOTAL']:
                estab = colunas[0]
                if len(colunas) > 1 and colunas[1]:
                    try:
                        valor = float(colunas[1].replace(',', '.'))
                        if secao_atual == 'colaboradores':
                            dados_estabelecimentos[estab] = valor
                        elif secao_atual == 'admissoes':
                            dados_admissoes[estab] = valor
                        elif secao_atual == 'desligamentos':
                            dados_desligamentos[estab] = valor
                        elif secao_atual == 'turnover':
                            dados_turnover[estab] = valor
                    except:
                        pass
    
    return {
        'mes': mes_atual or 'novembro',
        'colaboradores': dados_estabelecimentos,
        'admissoes': dados_admissoes,
        'desligamentos': dados_desligamentos,
        'turnover': dados_turnover
    }

def atualizar_dados_json(dados_processados):
    """Atualiza o arquivo dados.json"""
    try:
        # Carrega dados atuais
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        mes = dados_processados['mes']
        
        # Verifica se o mês já existe
        if mes not in dados['labels']:
            dados['labels'].append(mes)
            indice_mes = len(dados['labels']) - 1
        else:
            indice_mes = dados['labels'].index(mes)
        
        # Atualiza colaboradores
        estabelecimentos = dados['colaboradores']['estabelecimentos']
        for i, estab in enumerate(estabelecimentos):
            if estab in dados_processados['colaboradores']:
                # Garante que o array tem o tamanho correto
                while len(dados['colaboradores']['dados'][i]) <= indice_mes:
                    dados['colaboradores']['dados'][i].append(0.0)
                dados['colaboradores']['dados'][i][indice_mes] = dados_processados['colaboradores'][estab]
        
        # Atualiza totais de colaboradores
        total_colab = dados_processados['colaboradores'].get('TOTAL', sum([v for k, v in dados_processados['colaboradores'].items() if k != 'TOTAL']))
        while len(dados['colaboradores']['totais']) <= indice_mes:
            dados['colaboradores']['totais'].append(0.0)
        dados['colaboradores']['totais'][indice_mes] = total_colab
        
        # Atualiza admissões
        for i, estab in enumerate(estabelecimentos):
            if estab in dados_processados['admissoes']:
                while len(dados['admitidos']['dados'][i]) <= indice_mes:
                    dados['admitidos']['dados'][i].append(0)
                dados['admitidos']['dados'][i][indice_mes] = int(dados_processados['admissoes'][estab])
        
        total_admissoes = dados_processados['admissoes'].get('TOTAL', sum([v for k, v in dados_processados['admissoes'].items() if k != 'TOTAL']))
        while len(dados['admitidos']['totais']) <= indice_mes:
            dados['admitidos']['totais'].append(0)
        dados['admitidos']['totais'][indice_mes] = int(total_admissoes)
        
        # Atualiza desligamentos
        for i, estab in enumerate(estabelecimentos):
            if estab in dados_processados['desligamentos']:
                while len(dados['desligados']['dados'][i]) <= indice_mes:
                    dados['desligados']['dados'][i].append(0)
                dados['desligados']['dados'][i][indice_mes] = int(dados_processados['desligamentos'][estab])
        
        total_desligamentos = dados_processados['desligamentos'].get('TOTAL', sum([v for k, v in dados_processados['desligamentos'].items() if k != 'TOTAL']))
        while len(dados['desligados']['totais']) <= indice_mes:
            dados['desligados']['totais'].append(0)
        dados['desligados']['totais'][indice_mes] = int(total_desligamentos)
        
        # Atualiza turnover
        if dados_processados['turnover']:
            for i, estab in enumerate(dados['turnover']['labels']):
                if estab in dados_processados['turnover']:
                    dados['turnover']['rates'][i] = dados_processados['turnover'][estab]
        
        # Salva o arquivo
        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        
        print(f"\nDados de {mes} atualizados com sucesso!")
        return True
        
    except Exception as e:
        print(f"Erro ao atualizar dados.json: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("Processador de Dados do Google Sheets")
    print("=" * 60)
    
    # Baixa dados
    csv_data = baixar_dados()
    if not csv_data:
        return
    
    # Mostra amostra
    print("\nPrimeiras 20 linhas dos dados:")
    linhas = csv_data.split('\n')[:20]
    for i, linha in enumerate(linhas):
        print(f"{i+1}: {linha[:100]}")
    
    # Processa dados
    print("\nProcessando dados...")
    dados_processados = processar_dados_completos(csv_data)
    
    print("\nDados processados:")
    print(f"Mes: {dados_processados['mes']}")
    print(f"Colaboradores: {dados_processados['colaboradores']}")
    print(f"Admissoes: {dados_processados['admissoes']}")
    print(f"Desligamentos: {dados_processados['desligamentos']}")
    print(f"Turnover: {dados_processados['turnover']}")
    
    # Atualiza JSON
    if atualizar_dados_json(dados_processados):
        print("\n" + "=" * 60)
        print("SUCESSO! Dados atualizados no arquivo dados.json")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("ERRO ao atualizar dados")
        print("=" * 60)

if __name__ == "__main__":
    main()


