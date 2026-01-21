"""
Script para verificar valores de colaboradores por segmento
"""
import json

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("VALORES ATUAIS - COLABORADORES POR SEGMENTO")
print("=" * 60)

segmentos = dados['porSegmentoEvolucao']['colaboradores']['labels']
meses = dados['labels']

print(f"\nMeses: {meses}")
print(f"\nValores atuais:")

for i, segmento in enumerate(segmentos):
    valores = dados['porSegmentoEvolucao']['colaboradores']['dados'][i]
    print(f"\n{segmento}:")
    for j, mes in enumerate(meses):
        if j < len(valores):
            print(f"  {mes}: {valores[j]}")

