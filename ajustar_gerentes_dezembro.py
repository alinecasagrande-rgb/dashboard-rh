"""
Script para ajustar valores de colaboradores por gerente para dezembro
Ajusta proporcionalmente para que a soma seja 605
"""
import json

# Carrega dados
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("AJUSTAR COLABORADORES POR GERENTE - DEZEMBRO")
print("=" * 60)

idx = 11  # Índice de dezembro
gerentes = dados['porGerenteEvolucao']['colaboradores']['labels']

print("\nValores atuais de dezembro:")
valores_atuais = []
total_atual = 0
for i, gerente in enumerate(gerentes):
    valor = dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx]
    valores_atuais.append(valor)
    total_atual += valor
    print(f"  {gerente}: {valor}")

print(f"\nTotal atual: {total_atual}")
print(f"Total esperado: 605")
print(f"Fator de ajuste: {605 / total_atual:.4f}")

# Ajusta proporcionalmente
print("\n" + "=" * 60)
print("AJUSTANDO VALORES PROPORCIONALMENTE...")
print("=" * 60)

fator = 605 / total_atual
total_novo = 0

for i, gerente in enumerate(gerentes):
    valor_antigo = valores_atuais[i]
    valor_novo = round(valor_antigo * fator, 1)
    dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx] = valor_novo
    total_novo += valor_novo
    if abs(valor_novo - valor_antigo) > 0.01:
        print(f"  {gerente}: {valor_antigo} -> {valor_novo}")

# Ajusta o último valor para garantir que a soma seja exatamente 605
if abs(total_novo - 605) > 0.01:
    diferenca = 605 - total_novo
    # Ajusta o maior valor
    idx_maior = valores_atuais.index(max(valores_atuais))
    valor_ajustado = dados['porGerenteEvolucao']['colaboradores']['dados'][idx_maior][idx] + diferenca
    dados['porGerenteEvolucao']['colaboradores']['dados'][idx_maior][idx] = valor_ajustado
    print(f"\n  Ajuste final em {gerentes[idx_maior]}: {dados['porGerenteEvolucao']['colaboradores']['dados'][idx_maior][idx] - diferenca} -> {valor_ajustado}")

# Verifica total final
total_final = sum(dados['porGerenteEvolucao']['colaboradores']['dados'][i][idx] for i in range(len(gerentes)))
print(f"\nTotal final: {total_final}")

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("VALORES AJUSTADOS!")
print("=" * 60)
print("\nNOTA: Os valores foram ajustados proporcionalmente.")
print("Se voce tiver os valores corretos, pode atualizar manualmente no dados.json")

