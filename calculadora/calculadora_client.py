import socket

# Configurações do Cliente
SERVER_IP = '127.0.0.1' # Localhost
SERVER_PORT = 5000

def enviar_requisicao(payload_string):
    """
    Função auxiliar que abre conexão, envia dados e fecha.
    Implementa o modelo 'Short-lived connection'.
    """
    try:
        # [COMUNICAÇÃO] Cria o socket do cliente
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # [COMUNICAÇÃO] Tenta conectar ao servidor no IP e Porta especificados
        client_socket.connect((SERVER_IP, SERVER_PORT))
        
        # [COMUNICAÇÃO] Envia a string completa (payload) convertida em bytes
        client_socket.sendall(payload_string.encode())
        
        # [COMUNICAÇÃO] Aguarda e lê a resposta do servidor (buffer de 1024 bytes)
        resposta = client_socket.recv(1024).decode()
        
        # [COMUNICAÇÃO] Fecha a conexão
        client_socket.close()
        
        return resposta
    except ConnectionRefusedError:
        return "Erro: Não foi possível conectar ao servidor."

def menu():
    print("\n--- 🐍 Calculadora Distribuída Python ---")
    print("1. Operação Simples (+, -, *, /)")
    print("2. Expressão Completa (Cálculo no Servidor)")
    print("3. Expressão Decomposta (Cálculo via Chamadas RPC)")
    print("0. Sair")
    return input("Opção: ")

def main():
    while True:
        opcao = menu()
        
        if opcao == '0': 
            break
            
        elif opcao == '1':
            # Modo Clássico
            n1 = input("Numero 1: ")
            n2 = input("Numero 2: ")
            print("1:+, 2:-, 3:*, 4:/")
            op = input("Operação: ")
            
            # Monta o pacote: OP \n N1 \n N2
            payload = f"{op}\n{n1}\n{n2}"
            print(f"Resultado: {enviar_requisicao(payload)}")

        elif opcao == '2':
            # Abordagem 1: Server-Side Processing
            # O cliente é 'burro', só repassa a string. Economiza processamento local.
            expr = input("Digite a expressão (ex: (10+5)*2 ): ")
            
            # Protocolo: 5 \n EXPRESSAO
            payload = f"5\n{expr}"
            print(f"Resultado (Processado Remotamente): {enviar_requisicao(payload)}")

        elif opcao == '3':
            # Abordagem 2: Client-Side Decomposition
            # O cliente é 'inteligente'. Ele entende a conta e usa o servidor apenas como calculadora básica.
            # Vantagem: Distribui a carga de interpretação.
            entrada = input("Digite uma conta simples (ex: 10 + 20): ")
            
            try:
                partes = entrada.split() # Separa por espaço
                n1 = partes[0]
                simbolo = partes[1]
                n2 = partes[2]
                
                mapa_ops = {'+': '1', '-': '2', '*': '3', '/': '4'}
                op_code = mapa_ops.get(simbolo)
                
                if op_code:
                    print(f"Cliente: Entendi que você quer {simbolo}. Enviando comando RPC...")
                    payload = f"{op_code}\n{n1}\n{n2}"
                    print(f"Resultado (Orquestrado pelo Cliente): {enviar_requisicao(payload)}")
                else:
                    print("Operador não suportado nesta abordagem simples.")
            except:
                print("Erro de parsing no cliente. Use o formato '10 + 10' com espaços.")

if __name__ == "__main__":
    main()