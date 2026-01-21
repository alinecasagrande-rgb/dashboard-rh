"""
Script final para processar dados do Google Sheets corretamente
"""
import json
import urllib.request
import csv
import io

# Link CSV da planilha do Google Sheets
# Link atualizado para a planilha correta
CSV_URL = "https://docs.google.com/spreadsheets/d/1_JoETFEN0c5554x3_C1jjAgGu_2yEBtSqiZCEnQZGuQ/export?format=csv&gid=0"

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

def processar_planilha(csv_data):
    """Processa a planilha completa"""
    linhas = [linha for linha in csv_data.strip().split('\n') if linha.strip()]
    
    dados = {
        'colaboradores': {},
        'admissoes': {},
        'desligamentos': {},
        'turnover': {},
        'aprendizes': {},
        'pcd': {}
    }
    
    meses = []
    secao_atual = None
    header_encontrado = False
    
    for i, linha in enumerate(linhas):
        colunas = [c.strip() for c in linha.split(',')]
        
        if not colunas or not colunas[0]:
            continue
        
        primeira_col = colunas[0].upper()
        
        # Detecta seções
        if 'COLABORADORES' in primeira_col and 'ESTABELECIMENTO' in primeira_col:
            secao_atual = 'colaboradores'
            header_encontrado = False
            continue
        elif 'ADMITIDOS' in primeira_col and 'ESTABELECIMENTO' in primeira_col:
            secao_atual = 'admissoes'
            header_encontrado = False
            continue
        elif ('DESLIGAMENTOS' in primeira_col or 'DEMITIDOS' in primeira_col) and 'ESTABELECIMENTO' in primeira_col:
            secao_atual = 'desligamentos'
            header_encontrado = False
            continue
        elif 'TURNOVER' in primeira_col:
            secao_atual = 'turnover'
            header_encontrado = False
            continue
        elif 'APRENDIZ' in primeira_col and 'ESTABELECIMENTO' in primeira_col:
            secao_atual = 'aprendizes'
            header_encontrado = False
            continue
        elif 'PCD' in primeira_col and 'ESTABELECIMENTO' in primeira_col:
            secao_atual = 'pcd'
            header_encontrado = False
            continue
        
        # Detecta linha de cabeçalho (Estab, Estabelecimento, janeiro, fevereiro, etc.)
        if primeira_col == 'ESTAB' or primeira_col.startswith('ESTAB') or primeira_col == 'ESTABELECIMENTO':
            if len(colunas) > 1:
                meses = [m.lower().strip() for m in colunas[1:] if m.strip()]
                header_encontrado = True
            continue
        
        # Processa linhas de dados
        if header_encontrado and secao_atual and colunas[0]:
            estab = colunas[0]
            if estab.upper() == 'TOTAL GERAL' or estab.upper() == 'TOTAL':
                estab = 'TOTAL'
            
            # Processa valores mensais
            valores = []
            for j, valor_str in enumerate(colunas[1:], start=0):
                if j < len(meses):
                    try:
                        # Remove espaços e converte vírgula para ponto
                        valor_limpo = valor_str.replace(',', '.').strip()
                        if valor_limpo:
                            valor = float(valor_limpo)
                            valores.append((meses[j], valor))
                    except:
                        pass
            
            if valores and secao_atual:
                dados[secao_atual][estab] = dict(valores)
    
    return dados, meses

def atualizar_dados_json(dados_processados, meses_planilha):
    """Atualiza o arquivo dados.json"""
    try:
        # Carrega dados atuais
        with open('dados.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        # Mapeia meses
        meses_json = dados['labels']
        
        # Adiciona novos meses que não existem nos labels
        for mes in meses_planilha:
            if mes not in meses_json:
                meses_json.append(mes)
                print(f"  Novo mes adicionado: {mes}")
        
        # Atualiza colaboradores
        estabelecimentos = dados['colaboradores']['estabelecimentos']
        for i, estab in enumerate(estabelecimentos):
            if estab in dados_processados['colaboradores']:
                valores_mes = dados_processados['colaboradores'][estab]
                for mes, valor in valores_mes.items():
                    if mes in meses_json:
                        indice = meses_json.index(mes)
                        # Garante que o array tem o tamanho correto
                        while len(dados['colaboradores']['dados'][i]) <= indice:
                            dados['colaboradores']['dados'][i].append(0.0)
                        dados['colaboradores']['dados'][i][indice] = valor
        
        # Atualiza totais de colaboradores
        if 'TOTAL' in dados_processados['colaboradores']:
            valores_total = dados_processados['colaboradores']['TOTAL']
            for mes, valor in valores_total.items():
                if mes in meses_json:
                    indice = meses_json.index(mes)
                    while len(dados['colaboradores']['totais']) <= indice:
                        dados['colaboradores']['totais'].append(0.0)
                    dados['colaboradores']['totais'][indice] = valor
        
        # Atualiza admissões
        for i, estab in enumerate(estabelecimentos):
            if estab in dados_processados['admissoes']:
                valores_mes = dados_processados['admissoes'][estab]
                for mes, valor in valores_mes.items():
                    if mes in meses_json:
                        indice = meses_json.index(mes)
                        while len(dados['admitidos']['dados'][i]) <= indice:
                            dados['admitidos']['dados'][i].append(0)
                        dados['admitidos']['dados'][i][indice] = int(valor)
        
        if 'TOTAL' in dados_processados['admissoes']:
            valores_total = dados_processados['admissoes']['TOTAL']
            for mes, valor in valores_total.items():
                if mes in meses_json:
                    indice = meses_json.index(mes)
                    while len(dados['admitidos']['totais']) <= indice:
                        dados['admitidos']['totais'].append(0)
                    dados['admitidos']['totais'][indice] = int(valor)
        
        # Atualiza desligamentos
        for i, estab in enumerate(estabelecimentos):
            if estab in dados_processados['desligamentos']:
                valores_mes = dados_processados['desligamentos'][estab]
                for mes, valor in valores_mes.items():
                    if mes in meses_json:
                        indice = meses_json.index(mes)
                        while len(dados['desligados']['dados'][i]) <= indice:
                            dados['desligados']['dados'][i].append(0)
                        dados['desligados']['dados'][i][indice] = int(valor)
        
        if 'TOTAL' in dados_processados['desligamentos']:
            valores_total = dados_processados['desligamentos']['TOTAL']
            for mes, valor in valores_total.items():
                if mes in meses_json:
                    indice = meses_json.index(mes)
                    while len(dados['desligados']['totais']) <= indice:
                        dados['desligados']['totais'].append(0)
                    dados['desligados']['totais'][indice] = int(valor)
        
        # Atualiza turnover (se disponível)
        if dados_processados['turnover']:
            for estab in dados['turnover']['labels']:
                if estab in dados_processados['turnover']:
                    valores_mes = dados_processados['turnover'][estab]
                    # Pega o último mês disponível
                    if meses_json:
                        ultimo_mes = meses_json[-1]
                        if ultimo_mes in valores_mes:
                            indice = dados['turnover']['labels'].index(estab)
                            dados['turnover']['rates'][indice] = valores_mes[ultimo_mes]
        
        # Atualiza aprendizes
        if 'TOTAL' in dados_processados['aprendizes']:
            valores_total = dados_processados['aprendizes']['TOTAL']
            for mes, valor in valores_total.items():
                if mes in meses_json:
                    indice = meses_json.index(mes)
                    while len(dados['aprendizes']['totais']) <= indice:
                        dados['aprendizes']['totais'].append(0)
                    dados['aprendizes']['totais'][indice] = int(valor)
        
        # Atualiza PCD
        if 'TOTAL' in dados_processados['pcd']:
            valores_total = dados_processados['pcd']['TOTAL']
            for mes, valor in valores_total.items():
                if mes in meses_json:
                    indice = meses_json.index(mes)
                    while len(dados['pcd']['totais']) <= indice:
                        dados['pcd']['totais'].append(0)
                    dados['pcd']['totais'][indice] = int(valor)
        
        # Salva o arquivo
        with open('dados.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        
        print("\nDados atualizados com sucesso!")
        return True
        
    except Exception as e:
        print(f"Erro ao atualizar dados.json: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("Processador Final de Dados do Google Sheets")
    print("=" * 60)
    
    # Baixa dados
    csv_data = baixar_dados()
    if not csv_data:
        return
    
    # Processa dados
    print("\nProcessando dados da planilha...")
    dados_processados, meses = processar_planilha(csv_data)
    
    print(f"\nMeses encontrados: {meses}")
    print(f"\nColaboradores processados: {len(dados_processados['colaboradores'])} estabelecimentos")
    print(f"Admissoes processadas: {len(dados_processados['admissoes'])} estabelecimentos")
    print(f"Desligamentos processados: {len(dados_processados['desligamentos'])} estabelecimentos")
    print(f"Aprendizes processados: {len(dados_processados['aprendizes'])} estabelecimentos")
    print(f"PCD processados: {len(dados_processados['pcd'])} estabelecimentos")
    
    # Mostra amostra
    if dados_processados['colaboradores']:
        print("\nAmostra - Colaboradores (101):")
        if '101' in dados_processados['colaboradores']:
            print(dados_processados['colaboradores']['101'])
    
    # Atualiza JSON
    if atualizar_dados_json(dados_processados, meses):
        print("\n" + "=" * 60)
        print("SUCESSO! Arquivo dados.json atualizado")
        print("=" * 60)
        print("\nAgora voce pode abrir o index.html no navegador para ver os dados atualizados!")
    else:
        print("\n" + "=" * 60)
        print("ERRO ao atualizar dados")
        print("=" * 60)

if __name__ == "__main__":
    main()

