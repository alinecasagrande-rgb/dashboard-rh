"""
Script para verificar dados de colaboradores por gerente
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("VERIFICACAO - COLABORADORES POR GERENTE")
print("=" * 60)

meses_esperados = len(dados['labels'])
indice_novembro = meses_esperados - 1

print(f"\nTotal de meses: {meses_esperados}")
print(f"Ultimo mes: {dados['labels'][indice_novembro]}")
print(f"Indice de novembro: {indice_novembro}")

print("\n" + "=" * 60)
print("COLABORADORES POR GERENTE (NOVEMBRO):")
print("=" * 60)

for i, gerente in enumerate(dados['porGerenteEvolucao']['colaboradores']['labels']):
    array = dados['porGerenteEvolucao']['colaboradores']['dados'][i]
    meses_array = len(array)
    status = "OK" if meses_array == meses_esperados else "ERRO"
    
    if meses_array > indice_novembro:
        valor_novembro = array[indice_novembro]
        valor_outubro = array[indice_novembro - 1] if indice_novembro > 0 else 0
        print(f"  {status} {gerente}: {meses_array} meses | Outubro: {valor_outubro} | Novembro: {valor_novembro}")
    else:
        print(f"  {status} {gerente}: {meses_array} meses (FALTA NOVEMBRO)")

print("\n" + "=" * 60)
print("ADMISSOES POR GERENTE (NOVEMBRO):")
print("=" * 60)

for i, gerente in enumerate(dados['porGerenteEvolucao']['admissoes']['labels']):
    array = dados['porGerenteEvolucao']['admissoes']['dados'][i]
    meses_array = len(array)
    status = "OK" if meses_array == meses_esperados else "ERRO"
    
    if meses_array > indice_novembro:
        valor_novembro = array[indice_novembro]
        print(f"  {status} {gerente}: {meses_array} meses | Novembro: {valor_novembro}")
    else:
        print(f"  {status} {gerente}: {meses_array} meses (FALTA NOVEMBRO)")

print("\n" + "=" * 60)
print("DEMISSOES POR GERENTE (NOVEMBRO):")
print("=" * 60)

for i, gerente in enumerate(dados['porGerenteEvolucao']['demissoes']['labels']):
    array = dados['porGerenteEvolucao']['demissoes']['dados'][i]
    meses_array = len(array)
    status = "OK" if meses_array == meses_esperados else "ERRO"
    
    if meses_array > indice_novembro:
        valor_novembro = array[indice_novembro]
        print(f"  {status} {gerente}: {meses_array} meses | Novembro: {valor_novembro}")
    else:
        print(f"  {status} {gerente}: {meses_array} meses (FALTA NOVEMBRO)")

