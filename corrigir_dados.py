"""
Script para corrigir dados de admissão e adicionar novembro aos gerentes
"""
import json

# Carrega dados atuais
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("CORRIGINDO DADOS")
print("=" * 60)

# Dados corretos de admissão de novembro (da planilha)
admissoes_novembro_corretas = {
    '101': 5,
    '102': 3,
    '103': 8,
    '104': 1,
    '105': 2,
    '106': 2,
    '108': 0,
    'TOTAL': 21
}

print("\n1. Corrigindo admissões de novembro...")
estabelecimentos = dados['colaboradores']['estabelecimentos']
indice_novembro = len(dados['labels']) - 1  # Último índice (novembro)

for i, estab in enumerate(estabelecimentos):
    if estab in admissoes_novembro_corretas:
        valor_correto = admissoes_novembro_corretas[estab]
        valor_atual = dados['admitidos']['dados'][i][indice_novembro]
        dados['admitidos']['dados'][i][indice_novembro] = valor_correto
        print(f"  {estab}: {valor_atual} -> {valor_correto}")

# Corrige total
dados['admitidos']['totais'][indice_novembro] = admissoes_novembro_corretas['TOTAL']
print(f"  TOTAL: {dados['admitidos']['totais'][indice_novembro]}")

print("\n2. Adicionando novembro aos dados por gerente...")
print("   (Mantendo valores de outubro como referência)")

# Adiciona novembro aos colaboradores por gerente
for i in range(len(dados['porGerenteEvolucao']['colaboradores']['dados'])):
    ultimo_valor = dados['porGerenteEvolucao']['colaboradores']['dados'][i][-1]
    dados['porGerenteEvolucao']['colaboradores']['dados'][i].append(ultimo_valor)
    print(f"  {dados['porGerenteEvolucao']['colaboradores']['labels'][i]}: {ultimo_valor}")

# Adiciona novembro às admissões por gerente
for i in range(len(dados['porGerenteEvolucao']['admissoes']['dados'])):
    ultimo_valor = dados['porGerenteEvolucao']['admissoes']['dados'][i][-1]
    dados['porGerenteEvolucao']['admissoes']['dados'][i].append(ultimo_valor)
    print(f"  {dados['porGerenteEvolucao']['admissoes']['labels'][i]}: {ultimo_valor}")

# Adiciona novembro às demissões por gerente
for i in range(len(dados['porGerenteEvolucao']['demissoes']['dados'])):
    ultimo_valor = dados['porGerenteEvolucao']['demissoes']['dados'][i][-1]
    dados['porGerenteEvolucao']['demissoes']['dados'][i].append(ultimo_valor)
    print(f"  {dados['porGerenteEvolucao']['demissoes']['labels'][i]}: {ultimo_valor}")

# Adiciona novembro aos segmentos
print("\n3. Adicionando novembro aos dados por segmento...")
for i in range(len(dados['porSegmentoEvolucao']['colaboradores']['dados'])):
    ultimo_valor = dados['porSegmentoEvolucao']['colaboradores']['dados'][i][-1]
    dados['porSegmentoEvolucao']['colaboradores']['dados'][i].append(ultimo_valor)

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("DADOS CORRIGIDOS COM SUCESSO!")
print("=" * 60)
print("\nVerificacao:")
print(f"  Admissoes novembro - Total: {dados['admitidos']['totais'][indice_novembro]}")
print(f"  Gerentes - Colaboradores: {len(dados['porGerenteEvolucao']['colaboradores']['dados'][0])} meses")
print(f"  Gerentes - Admissoes: {len(dados['porGerenteEvolucao']['admissoes']['dados'][0])} meses")


