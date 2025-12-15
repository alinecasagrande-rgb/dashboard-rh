"""
Script para atualizar dados de colaboradores, admissões e desligamentos por gerente
a partir da planilha do Google Sheets
"""
import json
import urllib.request
import csv
import io

# Link CSV da planilha do Google Sheets
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

def processar_dados_gerentes(csv_data):
    """Processa dados por gerente da planilha"""
    linhas = [linha for linha in csv_data.strip().split('\n') if linha.strip()]
    
    dados_gerentes = {
        'colaboradores': {},
        'admissoes': {},
        'desligamentos': {}
    }
    
    meses = []
    secao_atual = None
    header_encontrado = False
    
    for i, linha in enumerate(linhas):
        colunas = [c.strip() for c in linha.split(',')]
        
        if not colunas or not colunas[0]:
            continue
        
        primeira_col = colunas[0].upper()
        
        # Detecta seções de gerentes
        if 'GERENTE' in primeira_col and ('COLABORADORES' in primeira_col or 'FUNCIONARIOS' in primeira_col):
            secao_atual = 'colaboradores_gerente'
            header_encontrado = False
            continue
        elif 'GERENTE' in primeira_col and ('ADMISSOES' in primeira_col or 'ADMITIDOS' in primeira_col):
            secao_atual = 'admissoes_gerente'
            header_encontrado = False
            continue
        elif 'GERENTE' in primeira_col and ('DESLIGAMENTOS' in primeira_col or 'DEMISSOES' in primeira_col or 'DEMITIDOS' in primeira_col):
            secao_atual = 'desligamentos_gerente'
            header_encontrado = False
            continue
        
        # Detecta linha de cabeçalho
        if primeira_col == 'GERENTE' or primeira_col.startswith('GERENTE') or 'GERENTE' in primeira_col:
            if len(colunas) > 1:
                meses = [m.lower().strip() for m in colunas[1:] if m.strip()]
                header_encontrado = True
            continue
        
        # Processa linhas de dados de gerentes
        if header_encontrado and secao_atual and colunas[0]:
            gerente = colunas[0].strip()
            if not gerente or gerente.upper() == 'TOTAL':
                continue
            
            # Processa valores mensais
            valores = []
            for j, valor_str in enumerate(colunas[1:], start=0):
                if j < len(meses):
                    try:
                        valor_limpo = valor_str.replace(',', '.').strip()
                        if valor_limpo:
                            valor = float(valor_limpo)
                            valores.append((meses[j], valor))
                    except:
                        pass
            
            if valores:
                if secao_atual == 'colaboradores_gerente':
                    dados_gerentes['colaboradores'][gerente] = dict(valores)
                elif secao_atual == 'admissoes_gerente':
                    dados_gerentes['admissoes'][gerente] = dict(valores)
                elif secao_atual == 'desligamentos_gerente':
                    dados_gerentes['desligamentos'][gerente] = dict(valores)
    
    return dados_gerentes, meses

def atualizar_dados_json(dados_gerentes, meses_planilha):
    """Atualiza o arquivo dados.json com dados por gerente"""
    try:
        # Carrega dados atuais
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        meses_json = dados['labels']
        indice_novembro = len(meses_json) - 1
        
        print(f"\nAtualizando dados por gerente para novembro (indice {indice_novembro})...")
        
        # Atualiza colaboradores por gerente
        if dados_gerentes['colaboradores']:
            print("\nColaboradores por gerente:")
            for i, gerente_label in enumerate(dados['porGerenteEvolucao']['colaboradores']['labels']):
                # Tenta encontrar correspondência (pode ter variações no nome)
                gerente_encontrado = None
                for gerente_planilha, valores in dados_gerentes['colaboradores'].items():
                    if gerente_label.upper().replace(' ', '') in gerente_planilha.upper().replace(' ', '') or \
                       gerente_planilha.upper().replace(' ', '') in gerente_label.upper().replace(' ', ''):
                        gerente_encontrado = gerente_planilha
                        break
                
                if gerente_encontrado and 'novembro' in dados_gerentes['colaboradores'][gerente_encontrado]:
                    novo_valor = dados_gerentes['colaboradores'][gerente_encontrado]['novembro']
                    valor_antigo = dados['porGerenteEvolucao']['colaboradores']['dados'][i][indice_novembro]
                    dados['porGerenteEvolucao']['colaboradores']['dados'][i][indice_novembro] = novo_valor
                    print(f"  {gerente_label}: {valor_antigo} -> {novo_valor}")
        
        # Atualiza admissões por gerente
        if dados_gerentes['admissoes']:
            print("\nAdmissoes por gerente:")
            for i, gerente_label in enumerate(dados['porGerenteEvolucao']['admissoes']['labels']):
                gerente_encontrado = None
                for gerente_planilha, valores in dados_gerentes['admissoes'].items():
                    if gerente_label.upper().replace(' ', '') in gerente_planilha.upper().replace(' ', '') or \
                       gerente_planilha.upper().replace(' ', '') in gerente_label.upper().replace(' ', ''):
                        gerente_encontrado = gerente_planilha
                        break
                
                if gerente_encontrado and 'novembro' in dados_gerentes['admissoes'][gerente_encontrado]:
                    novo_valor = int(dados_gerentes['admissoes'][gerente_encontrado]['novembro'])
                    valor_antigo = dados['porGerenteEvolucao']['admissoes']['dados'][i][indice_novembro]
                    dados['porGerenteEvolucao']['admissoes']['dados'][i][indice_novembro] = novo_valor
                    print(f"  {gerente_label}: {valor_antigo} -> {novo_valor}")
        
        # Atualiza desligamentos por gerente
        if dados_gerentes['desligamentos']:
            print("\nDesligamentos por gerente:")
            for i, gerente_label in enumerate(dados['porGerenteEvolucao']['demissoes']['labels']):
                gerente_encontrado = None
                for gerente_planilha, valores in dados_gerentes['desligamentos'].items():
                    if gerente_label.upper().replace(' ', '') in gerente_planilha.upper().replace(' ', '') or \
                       gerente_planilha.upper().replace(' ', '') in gerente_label.upper().replace(' ', ''):
                        gerente_encontrado = gerente_planilha
                        break
                
                if gerente_encontrado and 'novembro' in dados_gerentes['desligamentos'][gerente_encontrado]:
                    novo_valor = float(dados_gerentes['desligamentos'][gerente_encontrado]['novembro'])
                    valor_antigo = dados['porGerenteEvolucao']['demissoes']['dados'][i][indice_novembro]
                    dados['porGerenteEvolucao']['demissoes']['dados'][i][indice_novembro] = novo_valor
                    print(f"  {gerente_label}: {valor_antigo} -> {novo_valor}")
        
        # Salva o arquivo
        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        
        print("\n" + "=" * 60)
        print("DADOS ATUALIZADOS COM SUCESSO!")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"Erro ao atualizar dados.json: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("ATUALIZAR DADOS POR GERENTE DA PLANILHA")
    print("=" * 60)
    
    # Baixa dados
    csv_data = baixar_dados()
    if not csv_data:
        return
    
    # Processa dados
    print("\nProcessando dados da planilha...")
    dados_gerentes, meses = processar_dados_gerentes(csv_data)
    
    print(f"\nMeses encontrados: {meses}")
    print(f"\nGerentes encontrados:")
    print(f"  Colaboradores: {len(dados_gerentes['colaboradores'])} gerentes")
    print(f"  Admissoes: {len(dados_gerentes['admissoes'])} gerentes")
    print(f"  Desligamentos: {len(dados_gerentes['desligamentos'])} gerentes")
    
    if not dados_gerentes['colaboradores'] and not dados_gerentes['admissoes'] and not dados_gerentes['desligamentos']:
        print("\nAVISO: Nenhum dado de gerente encontrado na planilha.")
        print("Verifique se a planilha tem secoes com 'GERENTE' no titulo.")
        return
    
    # Atualiza JSON
    if atualizar_dados_json(dados_gerentes, meses):
        print("\nAgora voce pode fazer commit e push das alteracoes!")
    else:
        print("\nERRO ao atualizar dados")

if __name__ == "__main__":
    main()

