"""
Servidor HTTP simples para executar o dashboard localmente
Execute este arquivo e abra http://localhost:8000 no navegador
"""
import http.server
import socketserver
import webbrowser
import os
import socket

PORT_INICIAL = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adiciona headers CORS para permitir carregamento de recursos
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def encontrar_porta_livre(porta_inicial=8000):
    """Encontra uma porta livre começando da porta inicial"""
    for porta in range(porta_inicial, porta_inicial + 10):
        try:
            # Tenta criar um socket para verificar se a porta está livre
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', porta))
                return porta
        except OSError:
            continue
    return None

def main():
    # Muda para o diretório do script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Encontra uma porta livre
    PORT = encontrar_porta_livre(PORT_INICIAL)
    
    if PORT is None:
        print("=" * 60)
        print("ERRO: Nao foi possivel encontrar uma porta livre!")
        print("=" * 60)
        print("\nTente fechar outros programas que possam estar usando as portas 8000-8010")
        print("Ou feche janelas anteriores do servidor que ainda estejam abertas.")
        input("\nPressione Enter para sair...")
        return
    
    if PORT != PORT_INICIAL:
        print(f"Porta {PORT_INICIAL} esta em uso. Usando porta {PORT}...")
    
    Handler = MyHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/index.html"
            print("=" * 60)
            print("Servidor HTTP Local Iniciado!")
            print("=" * 60)
            print(f"\nServidor rodando em: http://localhost:{PORT}")
            print(f"Dashboard disponivel em: {url}")
            print("\nPressione CTRL+C para parar o servidor")
            print("=" * 60)
            
            # Abre o navegador automaticamente
            try:
                webbrowser.open(url)
                print("\nNavegador aberto automaticamente!")
            except:
                print(f"\nAbra manualmente: {url}")
            
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n\nServidor encerrado.")
                httpd.shutdown()
    except OSError as e:
        print("=" * 60)
        print("ERRO ao iniciar o servidor!")
        print("=" * 60)
        print(f"\nErro: {e}")
        print("\nPossiveis solucoes:")
        print("1. Feche outras janelas do servidor que possam estar abertas")
        print("2. Reinicie o computador se o problema persistir")
        print("3. Verifique se outro programa esta usando a porta")
        input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()

