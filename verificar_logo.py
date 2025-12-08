"""
Script para verificar e configurar o logo
"""
import os
import glob

print("=" * 60)
print("VERIFICANDO LOGO DA EMPRESA")
print("=" * 60)

# Procura por arquivos de logo
formatos = ['logo.*', 'Logo.*', 'LOGO.*']
arquivos_logo = []

for formato in formatos:
    arquivos = glob.glob(formato)
    arquivos_logo.extend(arquivos)

if arquivos_logo:
    print(f"\nArquivos de logo encontrados:")
    for arquivo in arquivos_logo:
        tamanho = os.path.getsize(arquivo) / 1024  # KB
        print(f"  - {arquivo} ({tamanho:.2f} KB)")
    
    # Verifica se precisa renomear
    if 'logo.png' not in arquivos_logo:
        primeiro_logo = arquivos_logo[0]
        print(f"\nArquivo encontrado: {primeiro_logo}")
        print(f"Renomeando para: logo.png")
        
        try:
            os.rename(primeiro_logo, 'logo.png')
            print("Logo renomeado com sucesso!")
        except Exception as e:
            print(f"Erro ao renomear: {e}")
            print(f"\nSolucao manual:")
            print(f"1. Renomeie o arquivo '{primeiro_logo}' para 'logo.png'")
            print(f"2. Ou atualize o index.html para usar '{primeiro_logo}'")
    else:
        print("\nLogo ja esta configurado corretamente (logo.png)")
else:
    print("\nNenhum arquivo de logo encontrado!")
    print("\nPara adicionar o logo:")
    print("1. Coloque o arquivo do logo na pasta do projeto")
    print("2. Nomeie como: logo.png, logo.jpg ou logo.svg")
    print("3. Tamanho recomendado: 200x200 pixels")

print("\n" + "=" * 60)


