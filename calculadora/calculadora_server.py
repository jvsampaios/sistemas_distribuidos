import socket

# Configurações do Servidor
HOST = '0.0.0.0'  # Escuta em todas as interfaces de rede
PORT = 5000       # Porta arbitrária acima de 1024

def calcular_expressao(expr):
    try:
        # CUIDADO: eval() é perigoso em produção (injeção de código), 
        # mas aceitável para este exercício acadêmico.
        return str(eval(expr))
    except Exception as e:
        return "Erro na expressão"

def iniciar_servidor():
    # [COMUNICAÇÃO] Cria o socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # [COMUNICAÇÃO] Vincula o socket ao endereço IP e porta definidos
    server_socket.bind((HOST, PORT))
    
    # [COMUNICAÇÃO] Coloca o servidor em modo de escuta (fila de até 5 conexões pendentes)
    server_socket.listen(5)
    
    print(f"👨‍🏫 Servidor rodando em {HOST}:{PORT}")

    while True:
        try:
            # [COMUNICAÇÃO] Bloqueia e aguarda uma nova conexão. Retorna um novo socket (conn) e o endereço do cliente (addr)
            conn, addr = server_socket.accept()
            print(f"Nova conexão de: {addr}")

            with conn: # Garante que o socket feche ao sair do bloco
                # PROTOCOLO:
                # 1. Recebe OpCode (1-4 basicas, 5 expressao)
                # 2. Se 1-4: Recebe Oper1 e Oper2
                # 3. Se 5: Recebe String da expressão
                
                # [COMUNICAÇÃO] Recebe até 1024 bytes e decodifica de bytes para string
                data = conn.recv(1024).decode().strip()
                if not data: break
                
                # Separamos os dados por quebra de linha (nosso delimitador de protocolo)
                linhas = data.split('\n')
                op_code = int(linhas[0])
                resultado = ""

                if 1 <= op_code <= 4:
                    # Operações básicas
                    oper1 = float(linhas[1])
                    oper2 = float(linhas[2])
                    
                    if op_code == 1: resultado = str(oper1 + oper2)
                    elif op_code == 2: resultado = str(oper1 - oper2)
                    elif op_code == 3: resultado = str(oper1 * oper2)
                    elif op_code == 4: resultado = str(oper1 / oper2 if oper2 != 0 else "Erro Div/0")
                
                elif op_code == 5:
                    # Abordagem 1: O servidor recebe a expressão bruta e se vira para calcular
                    expressao = linhas[1]
                    print(f"Processando expressão no server: {expressao}")
                    resultado = calcular_expressao(expressao)

                print(f"Enviando resultado: {resultado}")
                
                # [COMUNICAÇÃO] Envia a resposta de volta ao cliente (codificando string para bytes)
                conn.sendall(resultado.encode())
                
        except Exception as e:
            print(f"Erro no processamento: {e}")

if __name__ == "__main__":
    iniciar_servidor()