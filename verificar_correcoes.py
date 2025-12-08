"""
Verifica se as correções foram aplicadas corretamente
"""
import json

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("VERIFICACAO DAS CORRECOES")
print("=" * 60)

print("\n1. ADMISSOES DE NOVEMBRO:")
print("-" * 60)
indice_novembro = len(dados['labels']) - 1
total = 0
for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
    valor = dados['admitidos']['dados'][i][indice_novembro]
    total += valor
    print(f"  {estab}: {valor}")
print(f"  TOTAL: {total} (esperado: 21)")
print(f"  Total no JSON: {dados['admitidos']['totais'][indice_novembro]}")

print("\n2. DADOS POR GERENTE - NOVEMBRO:")
print("-" * 60)
print("Colaboradores por gerente (novembro):")
for i, gerente in enumerate(dados['porGerenteEvolucao']['colaboradores']['labels']):
    valor = dados['porGerenteEvolucao']['colaboradores']['dados'][i][indice_novembro]
    print(f"  {gerente}: {valor}")

print("\nAdmissoes por gerente (novembro):")
for i, gerente in enumerate(dados['porGerenteEvolucao']['admissoes']['labels']):
    valor = dados['porGerenteEvolucao']['admissoes']['dados'][i][indice_novembro]
    print(f"  {gerente}: {valor}")

print("\nDemissoes por gerente (novembro):")
for i, gerente in enumerate(dados['porGerenteEvolucao']['demissoes']['labels']):
    valor = dados['porGerenteEvolucao']['demissoes']['dados'][i][indice_novembro]
    print(f"  {gerente}: {valor}")

print("\n" + "=" * 60)
print("VERIFICACAO CONCLUIDA")
print("=" * 60)


