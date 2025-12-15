"""
Script para corrigir os valores de novembro na evolução por segmento
Calcula os valores corretos baseado nos dados de detalheSegmento
"""
import json

# Carrega dados atuais
with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("=" * 60)
print("CORRIGINDO EVOLUÇÃO POR SEGMENTO - NOVEMBRO")
print("=" * 60)

indice_novembro = len(dados['labels']) - 1  # Último índice (novembro)
print(f"\nÍndice de novembro: {indice_novembro}")
print(f"Mês: {dados['labels'][indice_novembro]}")

# Função para calcular total de um segmento a partir dos detalhes
def calcular_total_segmento(segmento_key, indice):
    """Calcula o total de um segmento somando os detalhes"""
    if segmento_key not in dados['detalheSegmento']:
        return None
    
    segmento = dados['detalheSegmento'][segmento_key]
    total = 0.0
    
    # Se não tem dados de novembro, usa outubro (último valor disponível)
    indice_usar = indice
    if len(segmento['dados']) > 0 and len(segmento['dados'][0]) <= indice:
        indice_usar = len(segmento['dados'][0]) - 1  # Usa outubro
    
    for array in segmento['dados']:
        if indice_usar < len(array):
            total += array[indice_usar]
    
    return total

# Calcula valores de novembro para cada segmento
print("\n1. Calculando valores de novembro para cada segmento...")

# ADMINISTRATIVO
admin_novembro = calcular_total_segmento('admin', indice_novembro)
if admin_novembro is None:
    # Se não tem dados de detalhe, mantém o valor atual
    admin_novembro = dados['porSegmentoEvolucao']['colaboradores']['dados'][0][indice_novembro]
    print(f"  ADMINISTRATIVO: {admin_novembro} (mantido - sem detalhes)")
else:
    print(f"  ADMINISTRATIVO: {admin_novembro}")

# CANAL PRIVADO
privado_novembro = calcular_total_segmento('privado', indice_novembro)
if privado_novembro is None:
    privado_novembro = dados['porSegmentoEvolucao']['colaboradores']['dados'][1][indice_novembro]
    print(f"  CANAL PRIVADO: {privado_novembro} (mantido - sem detalhes)")
else:
    print(f"  CANAL PRIVADO: {privado_novembro}")

# CANAL PUBLICO
publico_novembro = calcular_total_segmento('publico', indice_novembro)
if publico_novembro is None:
    publico_novembro = dados['porSegmentoEvolucao']['colaboradores']['dados'][2][indice_novembro]
    print(f"  CANAL PUBLICO: {publico_novembro} (mantido - sem detalhes)")
else:
    print(f"  CANAL PUBLICO: {publico_novembro}")

# TRANSPORTE
# Verifica se há dados de transporte nos detalhes
transporte_novembro = dados['porSegmentoEvolucao']['colaboradores']['dados'][3][indice_novembro]
print(f"  TRANSPORTE: {transporte_novembro} (mantido - sem detalhes disponíveis)")

# LOGISTICA
logistica_novembro = calcular_total_segmento('logistica', indice_novembro)
if logistica_novembro is None:
    logistica_novembro = dados['porSegmentoEvolucao']['colaboradores']['dados'][4][indice_novembro]
    print(f"  LOGISTICA: {logistica_novembro} (mantido - sem detalhes)")
else:
    print(f"  LOGISTICA: {logistica_novembro}")

# TOTAL (soma de todos os segmentos)
total_calculado = admin_novembro + privado_novembro + publico_novembro + transporte_novembro + logistica_novembro
print(f"  TOTAL CALCULADO: {total_calculado}")

# Verifica se os detalhes têm novembro
print("\n2. Verificando se detalheSegmento tem dados de novembro...")
for key, segmento in dados['detalheSegmento'].items():
    if segmento['dados']:
        meses_detalhe = len(segmento['dados'][0])
        print(f"  {key}: {meses_detalhe} meses (esperado: {len(dados['labels'])} meses)")
        if meses_detalhe < len(dados['labels']):
            print(f"    AVISO: Falta adicionar novembro aos detalhes de {key}")

# Verifica o total geral de colaboradores
total_geral = dados['colaboradores']['totais'][indice_novembro]
print(f"\n3. Verificação de consistência:")
print(f"  Total calculado por segmento: {total_calculado}")
print(f"  Total geral (colaboradores.totais): {total_geral}")

# Se houver divergência, ajusta proporcionalmente os segmentos
if abs(total_calculado - total_geral) > 0.1:
    print(f"  DIVERGENCIA: Diferenca de {abs(total_calculado - total_geral)}")
    print(f"  Ajustando segmentos proporcionalmente...")
    
    # Fator de ajuste proporcional
    fator_ajuste = total_geral / total_calculado if total_calculado > 0 else 1.0
    
    admin_novembro = round(admin_novembro * fator_ajuste, 1)
    privado_novembro = round(privado_novembro * fator_ajuste, 1)
    publico_novembro = round(publico_novembro * fator_ajuste, 1)
    transporte_novembro = round(transporte_novembro * fator_ajuste, 1)
    logistica_novembro = round(logistica_novembro * fator_ajuste, 1)
    
    print(f"  Fator de ajuste: {fator_ajuste:.4f}")
    print(f"  ADMINISTRATIVO: {admin_novembro}")
    print(f"  CANAL PRIVADO: {privado_novembro}")
    print(f"  CANAL PUBLICO: {publico_novembro}")
    print(f"  TRANSPORTE: {transporte_novembro}")
    print(f"  LOGISTICA: {logistica_novembro}")
    print(f"  TOTAL AJUSTADO: {admin_novembro + privado_novembro + publico_novembro + transporte_novembro + logistica_novembro}")
else:
    print(f"  Valores consistentes!")

# Atualiza os valores de novembro na evolução por segmento
print("\n4. Atualizando valores de novembro na evolução por segmento...")

# ADMINISTRATIVO (índice 0)
dados['porSegmentoEvolucao']['colaboradores']['dados'][0][indice_novembro] = admin_novembro
print(f"  ADMINISTRATIVO: {dados['porSegmentoEvolucao']['colaboradores']['dados'][0][indice_novembro]}")

# CANAL PRIVADO (índice 1)
dados['porSegmentoEvolucao']['colaboradores']['dados'][1][indice_novembro] = privado_novembro
print(f"  CANAL PRIVADO: {dados['porSegmentoEvolucao']['colaboradores']['dados'][1][indice_novembro]}")

# CANAL PUBLICO (índice 2)
dados['porSegmentoEvolucao']['colaboradores']['dados'][2][indice_novembro] = publico_novembro
print(f"  CANAL PUBLICO: {dados['porSegmentoEvolucao']['colaboradores']['dados'][2][indice_novembro]}")

# TRANSPORTE (índice 3)
dados['porSegmentoEvolucao']['colaboradores']['dados'][3][indice_novembro] = transporte_novembro
print(f"  TRANSPORTE: {dados['porSegmentoEvolucao']['colaboradores']['dados'][3][indice_novembro]}")

# LOGISTICA (índice 4)
dados['porSegmentoEvolucao']['colaboradores']['dados'][4][indice_novembro] = logistica_novembro
print(f"  LOGISTICA: {dados['porSegmentoEvolucao']['colaboradores']['dados'][4][indice_novembro]}")

# TOTAL (índice 5) - usa o total geral
dados['porSegmentoEvolucao']['colaboradores']['dados'][5][indice_novembro] = total_geral
print(f"  TOTAL: {dados['porSegmentoEvolucao']['colaboradores']['dados'][5][indice_novembro]}")

# Salva o arquivo
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 60)
print("CORREÇÃO CONCLUÍDA!")
print("=" * 60)
print("\nValores finais de novembro por segmento:")
for i, label in enumerate(dados['porSegmentoEvolucao']['colaboradores']['labels']):
    valor = dados['porSegmentoEvolucao']['colaboradores']['dados'][i][indice_novembro]
    print(f"  {label}: {valor}")

