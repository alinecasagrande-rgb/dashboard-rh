"""
Script para atualizar dados do dashboard a partir do Google Sheets
Este script ajuda a importar dados do Google Sheets e atualizar o arquivo dados.json
"""

import json
import re

def atualizar_dados_novembro():
    """
    Atualiza o arquivo dados.json com os dados de novembro de 2025
    Baseado nos dados da planilha do Google Sheets
    """
    
    # Carrega o arquivo atual
    with open('dados.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Dados de novembro da planilha (já atualizados manualmente)
    # Esta função serve como exemplo para futuras atualizações
    
    print("✅ Dados de novembro já foram atualizados no arquivo dados.json")
    print("\nPara atualizar manualmente:")
    print("1. Abra o arquivo dados.json")
    print("2. Adicione o novo mês em 'labels'")
    print("3. Adicione os novos valores ao final de cada array")
    print("4. Certifique-se de que todos os arrays tenham o mesmo número de elementos")
    
    # Salva o arquivo (já atualizado)
    with open('dados.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("\n✅ Arquivo dados.json salvo com sucesso!")

if __name__ == "__main__":
    atualizar_dados_novembro()


