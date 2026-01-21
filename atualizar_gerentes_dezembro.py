"""
Script para atualizar valores de colaboradores por gerente para dezembro
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("ATUALIZAR COLABORADORES POR GERENTE - DEZEMBRO")
print("=" * 60)

idx = 11  # Índice de dezembro
gerentes = dados['porGerenteEvolucao']['colaboradores']['labels']

print("\nValores atuais de dezembro:")
total_atual = 0
for i, gerente in enumerate(gerentes):
    valor = dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx]
    total_atual += valor
    print(f"  {gerente}: {valor}")

print(f"\nTotal atual: {total_atual}")
print(f"Total esperado: 605")
print(f"Diferença: {605 - total_atual}")

print("\n" + "=" * 60)
print("Por favor, forneca os valores corretos de dezembro para cada gerente:")
print("=" * 60)

# Valores corretos - você pode atualizar aqui
valores_corretos = {}

for i, gerente in enumerate(gerentes):
    valor_atual = dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx]
    try:
        novo_valor = float(input(f"\n{gerente} (atual: {valor_atual}): "))
        valores_corretos[gerente] = novo_valor
    except (ValueError, KeyboardInterrupt):
        print(f"  Mantendo valor atual: {valor_atual}")
        valores_corretos[gerente] = valor_atual

# Atualiza os valores
print("\n" + "=" * 60)
print("ATUALIZANDO VALORES...")
print("=" * 60)

total_novo = 0
for i, gerente in enumerate(gerentes):
    novo_valor = valores_corretos[gerente]
    valor_antigo = dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx]
    dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx] = novo_valor
    total_novo += novo_valor
    if novo_valor != valor_antigo:
        print(f"  {gerente}: {valor_antigo} -> {novo_valor}")

print(f"\nTotal novo: {total_novo}")
print(f"Total esperado: 605")

if total_novo != 605:
    print(f"\n⚠️  ATENCAO: O total ({total_novo}) nao corresponde ao esperado (605)")
    resposta = input("Deseja continuar mesmo assim? (s/n): ")
    if resposta.lower() != 's':
        print("Operacao cancelada.")
        exit(1)

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("VALORES ATUALIZADOS COM SUCESSO!")
print("=" * 60)

