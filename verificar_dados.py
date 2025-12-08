"""
Script para verificar e mostrar os dados processados
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("VERIFICACAO DOS DADOS ATUALIZADOS")
print("=" * 60)

print(f"\nMeses disponiveis: {len(dados['labels'])} meses")
print(f"Meses: {dados['labels']}")

print(f"\nColaboradores - Total geral (novembro): {dados['colaboradores']['totais'][-1]}")
print(f"Admissoes - Total geral (novembro): {dados['admitidos']['totais'][-1]}")
print(f"Desligamentos - Total geral (novembro): {dados['desligados']['totais'][-1]}")

print("\nColaboradores por estabelecimento (novembro):")
for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
    valor = dados['colaboradores']['dados'][i][-1]
    print(f"  {estab}: {valor}")

print("\nAdmissoes por estabelecimento (novembro):")
for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
    valor = dados['admitidos']['dados'][i][-1]
    print(f"  {estab}: {valor}")

print("\nDesligamentos por estabelecimento (novembro):")
for i, estab in enumerate(dados['colaboradores']['estabelecimentos']):
    valor = dados['desligados']['dados'][i][-1]
    print(f"  {estab}: {valor}")

print("\n" + "=" * 60)
print("Dados verificados com sucesso!")
print("=" * 60)


