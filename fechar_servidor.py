"""
Script para fechar servidores Python que possam estar rodando na porta 8000
"""
import subprocess
import sys

def fechar_servidores_porta(porta=8000):
    """Fecha processos Python usando a porta especificada"""
    try:
        # Windows: encontra processos usando a porta
        resultado = subprocess.run(
            ['netstat', '-ano'],
            capture_output=True,
            text=True,
            shell=True
        )
        
        linhas = resultado.stdout.split('\n')
        processos_fechados = []
        
        for linha in linhas:
            if f':{porta}' in linha and 'LISTENING' in linha:
                partes = linha.split()
                if len(partes) > 4:
                    pid = partes[-1]
                    try:
                        # Tenta fechar o processo
                        subprocess.run(['taskkill', '/F', '/PID', pid], 
                                      capture_output=True, shell=True)
                        processos_fechados.append(pid)
                    except:
                        pass
        
        if processos_fechados:
            print(f"Fechados {len(processos_fechados)} processo(s) usando a porta {porta}")
            return True
        else:
            print(f"Nenhum processo encontrado usando a porta {porta}")
            return False
            
    except Exception as e:
        print(f"Erro ao verificar processos: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Fechando servidores anteriores...")
    print("=" * 60)
    
    # Tenta fechar processos nas portas 8000-8010
    for porta in range(8000, 8011):
        fechar_servidores_porta(porta)
    
    print("\n" + "=" * 60)
    print("Concluido! Agora voce pode executar o servidor novamente.")
    print("=" * 60)
    input("\nPressione Enter para sair...")


