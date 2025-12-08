"""
Script para corrigir a duplicação de novembro nos dados por gerente
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("CORRIGINDO DUPLICACAO DE NOVEMBRO NOS GERENTES")
print("=" * 60)

# Verifica quantos meses deveriam ter
meses_esperados = len(dados['labels'])  # 11 meses

print(f"\nMeses esperados: {meses_esperados}")
print(f"Meses disponiveis: {dados['labels']}")

# Corrige colaboradores por gerente
print("\n1. Corrigindo colaboradores por gerente...")
for i in range(len(dados['porGerenteEvolucao']['colaboradores']['dados'])):
    array = dados['porGerenteEvolucao']['colaboradores']['dados'][i]
    if len(array) > meses_esperados:
        # Remove valores duplicados, mantendo apenas os primeiros meses_esperados
        dados['porGerenteEvolucao']['colaboradores']['dados'][i] = array[:meses_esperados]
        print(f"  {dados['porGerenteEvolucao']['colaboradores']['labels'][i]}: {len(array)} -> {len(dados['porGerenteEvolucao']['colaboradores']['dados'][i])} meses")

# Corrige admissões por gerente
print("\n2. Corrigindo admissões por gerente...")
for i in range(len(dados['porGerenteEvolucao']['admissoes']['dados'])):
    array = dados['porGerenteEvolucao']['admissoes']['dados'][i]
    if len(array) > meses_esperados:
        dados['porGerenteEvolucao']['admissoes']['dados'][i] = array[:meses_esperados]
        print(f"  {dados['porGerenteEvolucao']['admissoes']['labels'][i]}: {len(array)} -> {len(dados['porGerenteEvolucao']['admissoes']['dados'][i])} meses")

# Corrige demissões por gerente
print("\n3. Corrigindo demissões por gerente...")
for i in range(len(dados['porGerenteEvolucao']['demissoes']['dados'])):
    array = dados['porGerenteEvolucao']['demissoes']['dados'][i]
    if len(array) > meses_esperados:
        dados['porGerenteEvolucao']['demissoes']['dados'][i] = array[:meses_esperados]
        print(f"  {dados['porGerenteEvolucao']['demissoes']['labels'][i]}: {len(array)} -> {len(dados['porGerenteEvolucao']['demissoes']['dados'][i])} meses")

# Corrige segmentos também
print("\n4. Corrigindo dados por segmento...")
for i in range(len(dados['porSegmentoEvolucao']['colaboradores']['dados'])):
    array = dados['porSegmentoEvolucao']['colaboradores']['dados'][i]
    if len(array) > meses_esperados:
        dados['porSegmentoEvolucao']['colaboradores']['dados'][i] = array[:meses_esperados]
        print(f"  {dados['porSegmentoEvolucao']['colaboradores']['labels'][i]}: {len(array)} -> {len(dados['porSegmentoEvolucao']['colaboradores']['dados'][i])} meses")

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("CORRECAO CONCLUIDA!")
print("=" * 60)
print("\nVerificacao final:")
print(f"  Colaboradores por gerente: {len(dados['porGerenteEvolucao']['colaboradores']['dados'][0])} meses")
print(f"  Admissoes por gerente: {len(dados['porGerenteEvolucao']['admissoes']['dados'][0])} meses")
print(f"  Demissoes por gerente: {len(dados['porGerenteEvolucao']['demissoes']['dados'][0])} meses")


