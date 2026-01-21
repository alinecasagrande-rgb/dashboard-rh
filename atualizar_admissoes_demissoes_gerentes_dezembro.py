"""
Script para atualizar valores de admissões e demissões por gerente para dezembro
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

idx = 11  # Índice de dezembro

print("=" * 60)
print("ATUALIZAR ADMISSOES E DEMISSOES POR GERENTE - DEZEMBRO")
print("=" * 60)

# Valores corretos de dezembro (baseado na planilha)
# Total admissoes: 18
# Total demissoes: 28

print("\nValores atuais de dezembro:")
print("\nADMISSOES:")
gerentes_admissoes = dados['porGerenteEvolucao']['admissoes']['labels']
total_atual_admissoes = 0
for i, gerente in enumerate(gerentes_admissoes):
    valor = dados['porGerenteEvolucao']['admissoes']['dados'][i][idx]
    total_atual_admissoes += valor
    print(f"  {gerente}: {valor}")

print(f"\nTotal atual: {total_atual_admissoes} (esperado: 18)")

print("\nDEMISSOES:")
gerentes_demissoes = dados['porGerenteEvolucao']['demissoes']['labels']
total_atual_demissoes = 0
for i, gerente in enumerate(gerentes_demissoes):
    valor = dados['porGerenteEvolucao']['demissoes']['dados'][i][idx]
    total_atual_demissoes += valor
    print(f"  {gerente}: {valor}")

print(f"\nTotal atual: {total_atual_demissoes} (esperado: 28)")

print("\n" + "=" * 60)
print("Por favor, forneca os valores corretos de dezembro:")
print("=" * 60)

# Valores corretos - você pode atualizar aqui
# Baseado nos dados da planilha, vou propor valores que somem 18 e 28
# Mas o usuário deve fornecer os valores corretos

print("\nADMISSOES POR GERENTE (total deve ser 18):")
admissoes_corretas = {}
for i, gerente in enumerate(gerentes_admissoes):
    valor_atual = dados['porGerenteEvolucao']['admissoes']['dados'][i][idx]
    try:
        novo_valor = int(input(f"{gerente} (atual: {valor_atual}): "))
        admissoes_corretas[gerente] = novo_valor
    except (ValueError, KeyboardInterrupt):
        print(f"  Mantendo valor atual: {valor_atual}")
        admissoes_corretas[gerente] = valor_atual

total_admissoes = sum(admissoes_corretas.values())
print(f"\nTotal admissoes: {total_admissoes} (esperado: 18)")

print("\nDEMISSOES POR GERENTE (total deve ser 28):")
demissoes_corretas = {}
for i, gerente in enumerate(gerentes_demissoes):
    valor_atual = dados['porGerenteEvolucao']['demissoes']['dados'][i][idx]
    try:
        novo_valor = float(input(f"{gerente} (atual: {valor_atual}): "))
        demissoes_corretas[gerente] = novo_valor
    except (ValueError, KeyboardInterrupt):
        print(f"  Mantendo valor atual: {valor_atual}")
        demissoes_corretas[gerente] = valor_atual

total_demissoes = sum(demissoes_corretas.values())
print(f"\nTotal demissoes: {total_demissoes} (esperado: 28)")

# Atualiza os valores
print("\n" + "=" * 60)
print("ATUALIZANDO VALORES...")
print("=" * 60)

for i, gerente in enumerate(gerentes_admissoes):
    novo_valor = admissoes_corretas[gerente]
    valor_antigo = dados['porGerenteEvolucao']['admissoes']['dados'][i][idx]
    dados['porGerenteEvolucao']['admissoes']['dados'][i][idx] = novo_valor
    if novo_valor != valor_antigo:
        print(f"  {gerente} (admissoes): {valor_antigo} -> {novo_valor}")

for i, gerente in enumerate(gerentes_demissoes):
    novo_valor = demissoes_corretas[gerente]
    valor_antigo = dados['porGerenteEvolucao']['demissoes']['dados'][i][idx]
    dados['porGerenteEvolucao']['demissoes']['dados'][i][idx] = novo_valor
    if novo_valor != valor_antigo:
        print(f"  {gerente} (demissoes): {valor_antigo} -> {novo_valor}")

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("VALORES ATUALIZADOS COM SUCESSO!")
print("=" * 60)

