"""
Script para arredondar valores de colaboradores por gerente para dezembro
Mantém a soma total em 605
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

idx = 11  # Índice de dezembro
gerentes = dados['porGerenteEvolucao']['colaboradores']['labels']

print("=" * 60)
print("ARREDONDAR COLABORADORES POR GERENTE - DEZEMBRO")
print("=" * 60)

print("\nValores atuais (com decimais):")
valores_atuais = []
total_atual = 0
for i, gerente in enumerate(gerentes):
    valor = dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx]
    valores_atuais.append(valor)
    total_atual += valor
    print(f"  {gerente}: {valor}")

print(f"\nTotal atual: {total_atual}")

# Arredonda para inteiros
print("\n" + "=" * 60)
print("ARREDONDANDO PARA INTEIROS...")
print("=" * 60)

valores_arredondados = []
soma_arredondada = 0

# Primeiro arredonda todos
for valor in valores_atuais:
    arredondado = round(valor)
    valores_arredondados.append(arredondado)
    soma_arredondada += arredondado

# Ajusta a diferença
diferenca = 605 - soma_arredondada
print(f"Soma arredondada: {soma_arredondada}")
print(f"Diferença a ajustar: {diferenca}")

# Ajusta o valor que teve maior diferença no arredondamento
if diferenca != 0:
    diferencas = [abs(valores_arredondados[i] - valores_atuais[i]) for i in range(len(valores_atuais))]
    # Ajusta o que teve maior diferença (ou menor, dependendo do sinal)
    if diferenca > 0:
        # Adiciona a diferença ao que teve maior arredondamento para baixo
        idx_ajustar = max(range(len(diferencas)), key=lambda i: valores_atuais[i] - valores_arredondados[i] if valores_atuais[i] > valores_arredondados[i] else -999)
    else:
        # Subtrai a diferença do que teve maior arredondamento para cima
        idx_ajustar = max(range(len(diferencas)), key=lambda i: valores_arredondados[i] - valores_atuais[i] if valores_arredondados[i] > valores_atuais[i] else -999)
    
    valores_arredondados[idx_ajustar] += diferenca
    print(f"Ajustando {gerentes[idx_ajustar]}: {valores_arredondados[idx_ajustar] - diferenca} -> {valores_arredondados[idx_ajustar]}")

# Atualiza os valores
total_final = 0
for i, gerente in enumerate(gerentes):
    valor_antigo = valores_atuais[i]
    valor_novo = valores_arredondados[i]
    dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx] = float(valor_novo)
    total_final += valor_novo
    if abs(valor_novo - valor_antigo) > 0.01:
        print(f"  {gerente}: {valor_antigo} -> {valor_novo}")

print(f"\nTotal final: {total_final}")

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("VALORES ARREDONDADOS!")
print("=" * 60)

