"""
Script para verificar valores de colaboradores por gerente em dezembro
"""
import json

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

idx = 11  # Índice de dezembro

print("=" * 60)
print("COLABORADORES POR GERENTE - DEZEMBRO")
print("=" * 60)

gerentes = dados['porGerenteEvolucao']['colaboradores']['labels']
print(f"\nTotal de gerentes: {len(gerentes)}")
print(f"\nValores de dezembro:")

for i, gerente in enumerate(gerentes):
    valores = dados['porGerenteEvolucao']['colaboradores']['dados'][i]
    if len(valores) > idx:
        print(f"  {gerente}: {valores[idx]}")
    else:
        print(f"  {gerente}: FALTA DEZEMBRO (tem apenas {len(valores)} meses)")

