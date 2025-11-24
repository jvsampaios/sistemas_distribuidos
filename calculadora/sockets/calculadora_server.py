import socket

def main():
    HOST = '0.0.0.0'
    PORT = 9090

    # Cria o socket com IPv4 e tipo TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Vincula o socket ao endereço IP e porta especificados
    server_socket.bind((HOST, PORT))
    
    # Coloca o servidor em modo de escuta, permitindo até 5 conexões na fila
    server_socket.listen(5)
    
    print(f"[*] Servidor ouvindo em {HOST}:{PORT}")

    while True:
        try:
            # Bloqueia e aguarda uma conexão. Retorna um novo objeto socket e o endereço
            client_socket, addr = server_socket.accept()
            print(f"[+] Nova conexão de {addr}")

            # Recebe até 1024 bytes do cliente e decodifica de bytes para string
            dados_recebidos = client_socket.recv(1024).decode('utf-8').strip()
            
            partes = dados_recebidos.split(';')
            op_code = int(partes[0])
            resultado = ""

            if 1 <= op_code <= 4:
                
                op1 = float(partes[1])
                op2 = float(partes[2])
                
                if op_code == 1: resultado = str(op1 + op2)
                elif op_code == 2: resultado = str(op1 - op2)
                elif op_code == 3: resultado = str(op1 * op2)
                elif op_code == 4: resultado = str(op1 / op2) if op2 != 0 else "Erro: Divisão por Zero"
            
            elif op_code == 5:
                expressao = partes[1]
                try:
                    resultado = str(eval(expressao)) # eval() resolve strings matemáticas automaticamente
                except:
                    resultado = "Erro na Expressão"

            print(f"Processado: {dados_recebidos} -> Resultado: {resultado}")

            # Codifica a string de resultado para bytes e envia de volta ao cliente
            client_socket.send(resultado.encode('utf-8'))
            
            # Fecha a conexão
            client_socket.close()

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()