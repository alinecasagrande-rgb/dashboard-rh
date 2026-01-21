"""
Script para ajustar valores de admissões e demissões por gerente para dezembro
Ajusta proporcionalmente para que os totais sejam 18 e 28
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

idx = 11  # Índice de dezembro

print("=" * 60)
print("AJUSTAR ADMISSOES E DEMISSOES POR GERENTE - DEZEMBRO")
print("=" * 60)

# ADMISSOES
print("\n1. AJUSTANDO ADMISSOES (total deve ser 18):")
print("-" * 60)
gerentes_admissoes = dados['porGerenteEvolucao']['admissoes']['labels']
valores_atuais_admissoes = []
total_atual_admissoes = 0

for i, gerente in enumerate(gerentes_admissoes):
    valor = dados['porGerenteEvolucao']['admissoes']['dados'][i][idx]
    valores_atuais_admissoes.append(valor)
    total_atual_admissoes += valor
    print(f"  {gerente}: {valor}")

print(f"\nTotal atual: {total_atual_admissoes} (esperado: 18)")

# Ajusta proporcionalmente
fator_admissoes = 18 / total_atual_admissoes if total_atual_admissoes > 0 else 1
print(f"Fator de ajuste: {fator_admissoes:.4f}")

valores_ajustados_admissoes = []
soma_ajustada_admissoes = 0

for valor in valores_atuais_admissoes:
    ajustado = round(valor * fator_admissoes)
    valores_ajustados_admissoes.append(ajustado)
    soma_ajustada_admissoes += ajustado

# Ajusta diferença
diferenca_admissoes = 18 - soma_ajustada_admissoes
if diferenca_admissoes != 0:
    # Ajusta o maior valor
    idx_maior = valores_atuais_admissoes.index(max(valores_atuais_admissoes))
    valores_ajustados_admissoes[idx_maior] += diferenca_admissoes

print("\nValores ajustados:")
for i, gerente in enumerate(gerentes_admissoes):
    valor_antigo = valores_atuais_admissoes[i]
    valor_novo = valores_ajustados_admissoes[i]
    dados['porGerenteEvolucao']['admissoes']['dados'][i][idx] = valor_novo
    if valor_novo != valor_antigo:
        print(f"  {gerente}: {valor_antigo} -> {valor_novo}")

total_final_admissoes = sum(valores_ajustados_admissoes)
print(f"\nTotal final admissoes: {total_final_admissoes}")

# DEMISSOES
print("\n" + "=" * 60)
print("2. AJUSTANDO DEMISSOES (total deve ser 28):")
print("-" * 60)
gerentes_demissoes = dados['porGerenteEvolucao']['demissoes']['labels']
valores_atuais_demissoes = []
total_atual_demissoes = 0

for i, gerente in enumerate(gerentes_demissoes):
    valor = dados['porGerenteEvolucao']['demissoes']['dados'][i][idx]
    valores_atuais_demissoes.append(valor)
    total_atual_demissoes += valor
    print(f"  {gerente}: {valor}")

print(f"\nTotal atual: {total_atual_demissoes} (esperado: 28)")

# Ajusta proporcionalmente
fator_demissoes = 28 / total_atual_demissoes if total_atual_demissoes > 0 else 1
print(f"Fator de ajuste: {fator_demissoes:.4f}")

valores_ajustados_demissoes = []
soma_ajustada_demissoes = 0

for valor in valores_atuais_demissoes:
    ajustado = round(valor * fator_demissoes)
    valores_ajustados_demissoes.append(ajustado)
    soma_ajustada_demissoes += ajustado

# Ajusta diferença
diferenca_demissoes = 28 - soma_ajustada_demissoes
if diferenca_demissoes != 0:
    # Ajusta o maior valor
    idx_maior = valores_atuais_demissoes.index(max(valores_atuais_demissoes))
    valores_ajustados_demissoes[idx_maior] += diferenca_demissoes

print("\nValores ajustados:")
for i, gerente in enumerate(gerentes_demissoes):
    valor_antigo = valores_atuais_demissoes[i]
    valor_novo = valores_ajustados_demissoes[i]
    dados['porGerenteEvolucao']['demissoes']['dados'][i][idx] = float(valor_novo)
    if valor_novo != valor_antigo:
        print(f"  {gerente}: {valor_antigo} -> {valor_novo}")

total_final_demissoes = sum(valores_ajustados_demissoes)
print(f"\nTotal final demissoes: {total_final_demissoes}")

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("VALORES AJUSTADOS!")
print("=" * 60)
print("\nNOTA: Os valores foram ajustados proporcionalmente.")
print("Se voce tiver os valores corretos especificos, pode atualizar manualmente no dados.json")

