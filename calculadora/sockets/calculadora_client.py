import socket

def enviar_requisicao(mensagem):

    HOST = '127.0.0.1' 
    PORT = 9090       

    try:
        # Cria um socket TCP
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Inicia o handshake TCP para conectar ao servidor
        client_socket.connect((HOST, PORT))
        
        # Envia a mensagem convertida em bytes
        client_socket.send(mensagem.encode('utf-8'))
        
        # Aguarda e recebe a resposta do servidor
        resposta = client_socket.recv(1024)
        
        # Fecha a conexão
        client_socket.close()
        
        return resposta.decode('utf-8')
    except ConnectionRefusedError:
        return "Erro: Não foi possível conectar ao servidor."

def main():
    while True:
        print("\n--- Calculadora Distribuída (Python) ---")
        print("1. Operação Básica (Decomposta no Cliente)")
        print("2. Expressão Completa (Calculada no Servidor)")
        print("0. Sair")
        opcao = input("Opção: ")

        if opcao == '0': break

        if opcao == '1':
            # Cliente decompõe a lógica e pede operação específica
            print("Digite no formato: VALOR1 OPERADOR VALOR2 (ex: 10 + 20)")
            entrada = input(">> ").split()
            
            if len(entrada) < 3:
                print("Formato inválido.")
                continue

            v1 = entrada[0]
            operador = entrada[1]
            v2 = entrada[2]

            op_code = 0
            
            if operador == '+': op_code = 1
            elif operador == '-': op_code = 2
            elif operador == '*': op_code = 3
            elif operador == '/': op_code = 4
            else:
                print("Operador desconhecido")
                continue

            # Monta o protocolo
            payload = f"{op_code};{v1};{v2}"
            print(f"[Log] Cliente processou e vai solicitar operação {op_code} ao servidor...")
            
            res = enviar_requisicao(payload)
            print(f"Resultado recebido: {res}")

        elif opcao == '2':
            # Servidor processa tudo
            expressao = input("Digite a expressão (ex: (10+5)*2 ): ")
            
            # Monta o protocolo
            payload = f"5;{expressao}"
            print("[Log] Enviando expressão crua para o servidor processar...")
            
            res = enviar_requisicao(payload)
            print(f"Resultado recebido: {res}")

if __name__ == "__main__":
    main()