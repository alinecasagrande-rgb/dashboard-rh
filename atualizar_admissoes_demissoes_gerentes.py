"""
Script para atualizar valores de admissões e desligamentos por gerente em novembro
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("ATUALIZAR ADMISSOES E DESLIGAMENTOS POR GERENTE - NOVEMBRO")
print("=" * 60)

indice_novembro = len(dados['labels']) - 1
print(f"\nIndice de novembro: {indice_novembro}")
print(f"Mes: {dados['labels'][indice_novembro]}")

print("\n" + "=" * 60)
print("ADMISSOES POR GERENTE - VALORES ATUAIS DE NOVEMBRO:")
print("=" * 60)

gerentes_admissoes = dados['porGerenteEvolucao']['admissoes']['labels']
valores_admissoes_atuais = {}

for i, gerente in enumerate(gerentes_admissoes):
    valor_atual = dados['porGerenteEvolucao']['admissoes']['dados'][i][indice_novembro]
    valores_admissoes_atuais[gerente] = valor_atual
    print(f"  {i+1}. {gerente}: {valor_atual}")

print("\n" + "=" * 60)
print("DESLIGAMENTOS POR GERENTE - VALORES ATUAIS DE NOVEMBRO:")
print("=" * 60)

gerentes_demissoes = dados['porGerenteEvolucao']['demissoes']['labels']
valores_demissoes_atuais = {}

for i, gerente in enumerate(gerentes_demissoes):
    valor_atual = dados['porGerenteEvolucao']['demissoes']['dados'][i][indice_novembro]
    valores_demissoes_atuais[gerente] = valor_atual
    print(f"  {i+1}. {gerente}: {valor_atual}")

print("\n" + "=" * 60)
print("INSTRUCOES:")
print("=" * 60)
print("Digite os novos valores para cada gerente.")
print("Pressione ENTER para manter o valor atual.")
print("Digite 'sair' para finalizar sem alterar.")
print()

# Solicita novos valores de ADMISSOES
print("\n" + "=" * 60)
print("ATUALIZAR ADMISSOES:")
print("=" * 60)
novos_valores_admissoes = {}
for i, gerente in enumerate(gerentes_admissoes):
    valor_atual = valores_admissoes_atuais[gerente]
    resposta = input(f"{gerente} (atual: {valor_atual}): ").strip()
    
    if resposta.lower() == 'sair':
        print("\nOperacao cancelada.")
        exit(0)
    
    if resposta == '':
        novos_valores_admissoes[gerente] = valor_atual
        print(f"  Mantido: {valor_atual}")
    else:
        try:
            novo_valor = int(resposta)
            novos_valores_admissoes[gerente] = novo_valor
            print(f"  Atualizado: {valor_atual} -> {novo_valor}")
        except ValueError:
            print(f"  Valor invalido! Mantendo: {valor_atual}")
            novos_valores_admissoes[gerente] = valor_atual

# Solicita novos valores de DESLIGAMENTOS
print("\n" + "=" * 60)
print("ATUALIZAR DESLIGAMENTOS:")
print("=" * 60)
novos_valores_demissoes = {}
for i, gerente in enumerate(gerentes_demissoes):
    valor_atual = valores_demissoes_atuais[gerente]
    resposta = input(f"{gerente} (atual: {valor_atual}): ").strip()
    
    if resposta.lower() == 'sair':
        print("\nOperacao cancelada.")
        exit(0)
    
    if resposta == '':
        novos_valores_demissoes[gerente] = valor_atual
        print(f"  Mantido: {valor_atual}")
    else:
        try:
            novo_valor = float(resposta)
            novos_valores_demissoes[gerente] = novo_valor
            print(f"  Atualizado: {valor_atual} -> {novo_valor}")
        except ValueError:
            print(f"  Valor invalido! Mantendo: {valor_atual}")
            novos_valores_demissoes[gerente] = valor_atual

# Confirma alteracoes
print("\n" + "=" * 60)
print("RESUMO DAS ALTERACOES:")
print("=" * 60)

alteracoes = False

print("\nADMISSOES:")
for i, gerente in enumerate(gerentes_admissoes):
    valor_atual = valores_admissoes_atuais[gerente]
    novo_valor = novos_valores_admissoes[gerente]
    if valor_atual != novo_valor:
        print(f"  {gerente}: {valor_atual} -> {novo_valor}")
        alteracoes = True

print("\nDESLIGAMENTOS:")
for i, gerente in enumerate(gerentes_demissoes):
    valor_atual = valores_demissoes_atuais[gerente]
    novo_valor = novos_valores_demissoes[gerente]
    if valor_atual != novo_valor:
        print(f"  {gerente}: {valor_atual} -> {novo_valor}")
        alteracoes = True

if not alteracoes:
    print("  Nenhuma alteracao realizada.")
    exit(0)

# Confirma salvamento
print("\n" + "=" * 60)
confirmacao = input("Deseja salvar essas alteracoes? (S/N): ").strip().upper()

if confirmacao != 'S':
    print("Operacao cancelada.")
    exit(0)

# Atualiza os valores de ADMISSOES
for i, gerente in enumerate(gerentes_admissoes):
    dados['porGerenteEvolucao']['admissoes']['dados'][i][indice_novembro] = novos_valores_admissoes[gerente]

# Atualiza os valores de DESLIGAMENTOS
for i, gerente in enumerate(gerentes_demissoes):
    dados['porGerenteEvolucao']['demissoes']['dados'][i][indice_novembro] = novos_valores_demissoes[gerente]

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("DADOS ATUALIZADOS COM SUCESSO!")
print("=" * 60)
print("\nValores finais de novembro - ADMISSOES:")
for i, gerente in enumerate(gerentes_admissoes):
    valor = dados['porGerenteEvolucao']['admissoes']['dados'][i][indice_novembro]
    print(f"  {gerente}: {valor}")

print("\nValores finais de novembro - DESLIGAMENTOS:")
for i, gerente in enumerate(gerentes_demissoes):
    valor = dados['porGerenteEvolucao']['demissoes']['dados'][i][indice_novembro]
    print(f"  {gerente}: {valor}")

