"""
Script para verificar valores de admissões e demissões por gerente em dezembro
"""
import json

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

idx = 11  # Índice de dezembro

print("=" * 60)
print("ADMISSOES E DEMISSOES POR GERENTE - DEZEMBRO")
print("=" * 60)

print("\n1. ADMISSOES POR GERENTE:")
print("-" * 60)
gerentes_admissoes = dados['porGerenteEvolucao']['admissoes']['labels']
total_admissoes = 0
for i, gerente in enumerate(gerentes_admissoes):
    valores = dados['porGerenteEvolucao']['admissoes']['dados'][i]
    if len(valores) > idx:
        valor = valores[idx]
        total_admissoes += valor
        print(f"  {gerente}: {valor}")
    else:
        print(f"  {gerente}: FALTA DEZEMBRO (tem apenas {len(valores)} meses)")

print(f"\nTotal admissoes: {total_admissoes}")
print(f"Total esperado (da planilha): 18")

print("\n" + "=" * 60)
print("2. DEMISSOES POR GERENTE:")
print("-" * 60)
gerentes_demissoes = dados['porGerenteEvolucao']['demissoes']['labels']
total_demissoes = 0
for i, gerente in enumerate(gerentes_demissoes):
    valores = dados['porGerenteEvolucao']['demissoes']['dados'][i]
    if len(valores) > idx:
        valor = valores[idx]
        total_demissoes += valor
        print(f"  {gerente}: {valor}")
    else:
        print(f"  {gerente}: FALTA DEZEMBRO (tem apenas {len(valores)} meses)")

print(f"\nTotal demissoes: {total_demissoes}")
print(f"Total esperado (da planilha): 28")

