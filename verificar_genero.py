"""
Script para verificar valores de gênero (masculino e feminino)
"""
import json

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("DADOS DE GENERO (MASCULINO E FEMININO)")
print("=" * 60)

generos = dados['demographics']['gender']['labels']
valores = dados['demographics']['gender']['data']

print("\nValores atuais:")
total = 0
for i, genero in enumerate(generos):
    valor = valores[i]
    total += valor
    print(f"  {genero}: {valor}")

print(f"\nTotal: {total}")
print(f"Total esperado (colaboradores dezembro): 605")

if total != 605:
    print(f"\n⚠️  PROBLEMA: O total ({total}) nao corresponde ao esperado (605)")
    diferenca = 605 - total
    print(f"Diferença: {diferenca}")

