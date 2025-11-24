import requests
import time
import sys

URL_SERVIDOR = "http://localhost:8000/calculadora.php"

# Política de Retry.

def enviar_requisicao_com_retry(payload):
    
    # Tenta enviar a requisição até 3 vezes em caso de falha, aguardando 2 segundos entre elas. 
    
    max_tentativas = 3
    wait_time = 2

    for tentativa in range(1, max_tentativas + 1):
        try:
            print(f"   -> [HTTP] Conectando... (Tentativa {tentativa})")
            
            # Abre conexão TCP, faz handshake SSL, monta o cabeçalho HTTP POST, serializa o 'payload' e envia.
           
            response = requests.post(URL_SERVIDOR, data=payload, timeout=5)
            
            # Verifica o código de status HTTP
            if response.status_code == 200:
                # Lê o corpo da resposta e faz a desserialização de JSON para Dicionário Python
                dados = response.json()
                
                if "erro" in dados:
                    return f"Erro do Servidor: {dados['erro']}"
                return dados['resultado']
            
            # Erros 5xx (Servidor) merecem Retry. Erros 4xx (Cliente) não.
            elif 500 <= response.status_code < 600:
                print(f"   -> Servidor instável: {response.status_code}")
            else:
                return f"Erro HTTP {response.status_code}: {response.text}"

        except requests.exceptions.RequestException as e:
            # Captura erros de rede (DNS, Timeout, Connection Refused)
            print(f"   -> Erro de Rede {e}")

        # Espera antes de tentar de novo
        if tentativa < max_tentativas:
            print(f"   -> Aguardando {wait_time}segundos para nova tentativa...")
            time.sleep(wait_time)

    return "Falha: Servidor inacessível após várias tentativas."

def menu():
    while True:
        print("\n=== CALCULADORA HTTP ===")
        print("1. Operação Básica (+, -, *, /)")
        print("2. Calcular Expressão (Processamento no Servidor)")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == '0':
            print("Encerrando cliente.")
            sys.exit()

        elif opcao == '1':
            try:
                op = input("Operação (+, -, *, /): ")
                
                mapa = {'+': 1, '-': 2, '*': 3, '/': 4}

                if op not in mapa:
                    print(f"A operação '{op}' não é válida. Tente novamente.")
                    continue
                    
                op_id = mapa.get(op)

                n1 = float(input("Número 1: "))
                n2 = float(input("Número 2: "))

                if op_id:
                    # Monta o Dicionário
                    payload = {'oper1': n1, 'oper2': n2, 'operacao': op_id}
                    
                    # Envia a resposta para o servidor
                    res = enviar_requisicao_com_retry(payload)
                    print(f"\n✅ Resultado: {res}")
                else:
                    print("Você deve digitar apenas números. Tente novamente.")
            except ValueError:
                print("Por favor, digite apenas números.")

        elif opcao == '2':
            # Cálculo inteiramente no Servidor
            expr = input("Digite a expressão (ex: (10+5)*2 ): ")
            
            # Monta Dicionário
            payload = {'operacao': 5, 'expressao': expr}
            
            print("   -> Enviando expressão para cálculo remoto...")
            res = enviar_requisicao_com_retry(payload)
            print(f"\n Resultado: {res}")

if __name__ == "__main__":
    menu()