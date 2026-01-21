"""
Script para adicionar dezembro aos dados por gerente e por segmento
Usa os valores de novembro como referência inicial
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("ADICIONANDO DEZEMBRO AOS DADOS POR GERENTE E SEGMENTO")
print("=" * 60)

# Verifica se dezembro existe nos labels
if 'dezembro' not in dados['labels']:
    print("\nERRO: Dezembro nao encontrado nos labels!")
    print("Execute primeiro o processar_dados_final.py para adicionar dezembro.")
    exit(1)

indice_dezembro = dados['labels'].index('dezembro')
indice_novembro = dados['labels'].index('novembro')

print(f"\nIndice de novembro: {indice_novembro}")
print(f"Indice de dezembro: {indice_dezembro}")

# Adiciona dezembro aos colaboradores por gerente
print("\n1. Adicionando dezembro aos colaboradores por gerente...")
for i in range(len(dados['porGerenteEvolucao']['colaboradores']['dados'])):
    array = dados['porGerenteEvolucao']['colaboradores']['dados'][i]
    if len(array) <= indice_dezembro:
        # Usa o valor de novembro como referência
        valor_novembro = array[indice_novembro] if len(array) > indice_novembro else array[-1]
        while len(array) <= indice_dezembro:
            array.append(valor_novembro)
        print(f"  {dados['porGerenteEvolucao']['colaboradores']['labels'][i]}: {valor_novembro}")

# Adiciona dezembro às admissões por gerente
print("\n2. Adicionando dezembro às admissões por gerente...")
for i in range(len(dados['porGerenteEvolucao']['admissoes']['dados'])):
    array = dados['porGerenteEvolucao']['admissoes']['dados'][i]
    if len(array) <= indice_dezembro:
        valor_novembro = array[indice_novembro] if len(array) > indice_novembro else array[-1]
        while len(array) <= indice_dezembro:
            array.append(int(valor_novembro))
        print(f"  {dados['porGerenteEvolucao']['admissoes']['labels'][i]}: {int(valor_novembro)}")

# Adiciona dezembro às demissões por gerente
print("\n3. Adicionando dezembro às demissões por gerente...")
for i in range(len(dados['porGerenteEvolucao']['demissoes']['dados'])):
    array = dados['porGerenteEvolucao']['demissoes']['dados'][i]
    if len(array) <= indice_dezembro:
        valor_novembro = array[indice_novembro] if len(array) > indice_novembro else array[-1]
        while len(array) <= indice_dezembro:
            array.append(float(valor_novembro))
        print(f"  {dados['porGerenteEvolucao']['demissoes']['labels'][i]}: {float(valor_novembro)}")

# Adiciona dezembro aos segmentos
print("\n4. Adicionando dezembro aos dados por segmento...")
for i in range(len(dados['porSegmentoEvolucao']['colaboradores']['dados'])):
    array = dados['porSegmentoEvolucao']['colaboradores']['dados'][i]
    if len(array) <= indice_dezembro:
        valor_novembro = array[indice_novembro] if len(array) > indice_novembro else array[-1]
        while len(array) <= indice_dezembro:
            array.append(valor_novembro)
        print(f"  {dados['porSegmentoEvolucao']['colaboradores']['labels'][i]}: {valor_novembro}")

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("DEZEMBRO ADICIONADO COM SUCESSO!")
print("=" * 60)
print("\nNOTA: Os valores de dezembro foram inicializados com os valores de novembro.")
print("Atualize manualmente os valores corretos de dezembro se necessario.")

