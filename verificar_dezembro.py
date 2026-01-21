"""
Script para verificar dados de dezembro
"""
import json

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

idx = 11  # Índice de dezembro

print("=" * 60)
print("VERIFICACAO - DADOS DE DEZEMBRO")
print("=" * 60)

print("\nCOLABORADORES POR ESTABELECIMENTO:")
for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
    valor = dados['colaboradores']['dados'][i][idx]
    print(f"  {estab}: {valor}")

print(f"\nTotal geral colaboradores: {dados['colaboradores']['totais'][idx]}")

print("\nADMISSOES POR ESTABELECIMENTO:")
for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
    valor = dados['admitidos']['dados'][i][idx]
    print(f"  {estab}: {valor}")

print(f"\nTotal geral admissoes: {dados['admitidos']['totais'][idx]}")

print("\nDESLIGAMENTOS POR ESTABELECIMENTO:")
for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
    valor = dados['desligados']['dados'][i][idx]
    print(f"  {estab}: {valor}")

print(f"\nTotal geral desligamentos: {dados['desligados']['totais'][idx]}")

