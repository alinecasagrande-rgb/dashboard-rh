"""
Verifica se a correção dos gerentes foi aplicada
"""
import json

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("VERIFICACAO - DADOS POR GERENTE")
print("=" * 60)

meses_esperados = len(dados['labels'])
print(f"\nMeses esperados: {meses_esperados}")
print(f"Meses: {dados['labels']}")

print("\nColaboradores por gerente:")
for i, gerente in enumerate(dados['porGerenteEvolucao']['colaboradores']['labels']):
    array = dados['porGerenteEvolucao']['colaboradores']['dados'][i]
    status = "OK" if len(array) == meses_esperados else "ERRO"
    print(f"  {status} {gerente}: {len(array)} meses (ultimo: {array[-1]})")

print("\nAdmissoes por gerente:")
for i, gerente in enumerate(dados['porGerenteEvolucao']['admissoes']['labels']):
    array = dados['porGerenteEvolucao']['admissoes']['dados'][i]
    status = "OK" if len(array) == meses_esperados else "ERRO"
    print(f"  {status} {gerente}: {len(array)} meses (ultimo: {array[-1]})")

print("\nDemissoes por gerente:")
for i, gerente in enumerate(dados['porGerenteEvolucao']['demissoes']['labels']):
    array = dados['porGerenteEvolucao']['demissoes']['dados'][i]
    status = "OK" if len(array) == meses_esperados else "ERRO"
    print(f"  {status} {gerente}: {len(array)} meses (ultimo: {array[-1]})")

print("\n" + "=" * 60)
print("VERIFICACAO CONCLUIDA")
print("=" * 60)


