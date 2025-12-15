"""
Script para atualizar valores de colaboradores por gerente em novembro
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("ATUALIZAR COLABORADORES POR GERENTE - NOVEMBRO")
print("=" * 60)

indice_novembro = len(dados['labels']) - 1
print(f"\nIndice de novembro: {indice_novembro}")
print(f"Mes: {dados['labels'][indice_novembro]}")

print("\n" + "=" * 60)
print("VALORES ATUAIS DE NOVEMBRO:")
print("=" * 60)

gerentes = dados['porGerenteEvolucao']['colaboradores']['labels']
valores_atuais = {}

for i, gerente in enumerate(gerentes):
    valor_atual = dados['porGerenteEvolucao']['colaboradores']['dados'][i][indice_novembro]
    valores_atuais[gerente] = valor_atual
    print(f"  {i+1}. {gerente}: {valor_atual}")

print("\n" + "=" * 60)
print("INSTRUCOES:")
print("=" * 60)
print("Digite os novos valores para cada gerente.")
print("Pressione ENTER para manter o valor atual.")
print("Digite 'sair' para finalizar sem alterar.")
print()

# Solicita novos valores
novos_valores = {}
for i, gerente in enumerate(gerentes):
    valor_atual = valores_atuais[gerente]
    resposta = input(f"{gerente} (atual: {valor_atual}): ").strip()
    
    if resposta.lower() == 'sair':
        print("\nOperacao cancelada.")
        exit(0)
    
    if resposta == '':
        # Mantem o valor atual
        novos_valores[gerente] = valor_atual
        print(f"  Mantido: {valor_atual}")
    else:
        try:
            novo_valor = float(resposta)
            novos_valores[gerente] = novo_valor
            print(f"  Atualizado: {valor_atual} -> {novo_valor}")
        except ValueError:
            print(f"  Valor invalido! Mantendo: {valor_atual}")
            novos_valores[gerente] = valor_atual

# Confirma alteracoes
print("\n" + "=" * 60)
print("RESUMO DAS ALTERACOES:")
print("=" * 60)

alteracoes = False
for i, gerente in enumerate(gerentes):
    valor_atual = valores_atuais[gerente]
    novo_valor = novos_valores[gerente]
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

# Atualiza os valores
for i, gerente in enumerate(gerentes):
    dados['porGerenteEvolucao']['colaboradores']['dados'][i][indice_novembro] = novos_valores[gerente]

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("DADOS ATUALIZADOS COM SUCESSO!")
print("=" * 60)
print("\nValores finais de novembro:")
for i, gerente in enumerate(gerentes):
    valor = dados['porGerenteEvolucao']['colaboradores']['dados'][i][indice_novembro]
    print(f"  {gerente}: {valor}")

