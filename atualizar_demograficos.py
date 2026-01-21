"""
Script para atualizar dados demográficos (gênero e faixa etária)
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("ATUALIZAR DADOS DEMOGRAFICOS")
print("=" * 60)

print("\n" + "=" * 60)
print("VALORES ATUAIS:")
print("=" * 60)

print("\nGENERO (Homens e Mulheres):")
print(f"  MASCULINO: {dados['demographics']['gender']['data'][0]}")
print(f"  FEMININO: {dados['demographics']['gender']['data'][1]}")
print(f"  TOTAL: {dados['demographics']['gender']['data'][0] + dados['demographics']['gender']['data'][1]}")

print("\nFAIXA ETARIA:")
print(f"  Menores de 18 anos: {dados['demographics']['ageRange']['data'][0]}")
print(f"  18 a 30 anos: {dados['demographics']['ageRange']['data'][1]}")
print(f"  31 a 40 anos: {dados['demographics']['ageRange']['data'][2]}")
print(f"  41 a 50 anos: {dados['demographics']['ageRange']['data'][3]}")
print(f"  Maiores de 50 anos: {dados['demographics']['ageRange']['data'][4]}")
total_faixa = sum(dados['demographics']['ageRange']['data'])
print(f"  TOTAL: {total_faixa}")

print("\n" + "=" * 60)
print("INSTRUCOES:")
print("=" * 60)
print("Digite os novos valores.")
print("Pressione ENTER para manter o valor atual.")
print("Digite 'sair' para finalizar sem alterar.")
print()

# Atualiza GENERO
print("\n" + "=" * 60)
print("ATUALIZAR GENERO:")
print("=" * 60)

resposta_masculino = input(f"MASCULINO (atual: {dados['demographics']['gender']['data'][0]}): ").strip()
if resposta_masculino.lower() == 'sair':
    print("Operacao cancelada.")
    exit(0)
if resposta_masculino:
    try:
        dados['demographics']['gender']['data'][0] = float(resposta_masculino)
        print(f"  Atualizado: {dados['demographics']['gender']['data'][0]}")
    except ValueError:
        print(f"  Valor invalido! Mantendo: {dados['demographics']['gender']['data'][0]}")

resposta_feminino = input(f"FEMININO (atual: {dados['demographics']['gender']['data'][1]}): ").strip()
if resposta_feminino.lower() == 'sair':
    print("Operacao cancelada.")
    exit(0)
if resposta_feminino:
    try:
        dados['demographics']['gender']['data'][1] = float(resposta_feminino)
        print(f"  Atualizado: {dados['demographics']['gender']['data'][1]}")
    except ValueError:
        print(f"  Valor invalido! Mantendo: {dados['demographics']['gender']['data'][1]}")

# Atualiza FAIXA ETARIA
print("\n" + "=" * 60)
print("ATUALIZAR FAIXA ETARIA:")
print("=" * 60)

faixas = [
    "Menores de 18 anos",
    "18 a 30 anos",
    "31 a 40 anos",
    "41 a 50 anos",
    "Maiores de 50 anos"
]

novos_valores_faixa = []
for i, faixa in enumerate(faixas):
    valor_atual = dados['demographics']['ageRange']['data'][i]
    resposta = input(f"{faixa} (atual: {valor_atual}): ").strip()
    
    if resposta.lower() == 'sair':
        print("Operacao cancelada.")
        exit(0)
    
    if resposta:
        try:
            novo_valor = float(resposta)
            novos_valores_faixa.append(novo_valor)
            print(f"  Atualizado: {valor_atual} -> {novo_valor}")
        except ValueError:
            novos_valores_faixa.append(valor_atual)
            print(f"  Valor invalido! Mantendo: {valor_atual}")
    else:
        novos_valores_faixa.append(valor_atual)
        print(f"  Mantido: {valor_atual}")

# Atualiza os valores
for i in range(len(faixas)):
    dados['demographics']['ageRange']['data'][i] = novos_valores_faixa[i]

# Confirma alteracoes
print("\n" + "=" * 60)
print("RESUMO DAS ALTERACOES:")
print("=" * 60)

print("\nGENERO:")
print(f"  MASCULINO: {dados['demographics']['gender']['data'][0]}")
print(f"  FEMININO: {dados['demographics']['gender']['data'][1]}")
print(f"  TOTAL: {dados['demographics']['gender']['data'][0] + dados['demographics']['gender']['data'][1]}")

print("\nFAIXA ETARIA:")
for i, faixa in enumerate(faixas):
    print(f"  {faixa}: {dados['demographics']['ageRange']['data'][i]}")
print(f"  TOTAL: {sum(dados['demographics']['ageRange']['data'])}")

# Verifica consistencia
total_genero = dados['demographics']['gender']['data'][0] + dados['demographics']['gender']['data'][1]
total_faixa = sum(dados['demographics']['ageRange']['data'])

if abs(total_genero - total_faixa) > 0.1:
    print(f"\nAVISO: Total por genero ({total_genero}) diferente do total por faixa etaria ({total_faixa})")
    print(f"  Diferenca: {abs(total_genero - total_faixa)}")

# Confirma salvamento
print("\n" + "=" * 60)
confirmacao = input("Deseja salvar essas alteracoes? (S/N): ").strip().upper()

if confirmacao != 'S':
    print("Operacao cancelada.")
    exit(0)

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("DADOS ATUALIZADOS COM SUCESSO!")
print("=" * 60)

