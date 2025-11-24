import Pyro4
import sys

def main():
    # criação do Proxy.
    calculadora_remota = Pyro4.Proxy("PYRONAME:calculadora")

    print("--- Cliente RMI (Pyro4) ---")
    
    try:
        
        while True:
            print("\nEscolha:")
            print("1. Operações Básicas")
            print("2. Expressão Matemática")
            print("0. Sair")
            opcao = input(">> ")

            if opcao == '0': break

            if opcao == '1':
                op = input("Operação (+, -, *, /): ")
                if op not in ['+', '-', '*', '/']:
                    print(f"A operação '{op}' não é válida. Tente novamente.")
                    continue
                try:
                    a = float(input("Valor A: "))
                    b = float(input("Valor B: "))
                except ValueError:
                    print("Você deve digitar apenas números. Tente novamente.")
                    continue
                
                resultado = 0
                # Chamada transparente. O código parece local, mas roda no servidor.
                if op == '+':
                    resultado = calculadora_remota.soma(a, b)
                elif op == '-':
                    resultado = calculadora_remota.subtrai(a, b)
                elif op == '*':
                    resultado = calculadora_remota.multiplica(a, b)
                elif op == '/':
                    try:
                        resultado = calculadora_remota.divide(a, b)
                    except Exception as e:
                        # O Pyro repassa as exceções do servidor para o cliente
                        print(f"Erro remoto capturado: {e}")
                        continue
                
                print(f"Resultado do Servidor: {resultado}")

            elif opcao == '2':
                expr = input("Digite a expressão (ex: (5+5)*2): ")
                
                # Enviamos a string complexa para ser processada remotamente
                res = calculadora_remota.calcula_expressao(expr)
                print(f"Resultado da Expressão: {res}")

    except Pyro4.errors.CommunicationError:
        print("[Erro] Não foi possível conectar ao servidor RMI (ou ao Name Server).")
        print("Verifique se executou: 'python -m Pyro4.naming'")
    except Exception as e:
        print(f"[Erro Genérico] {e}")

if __name__ == "__main__":
    main()