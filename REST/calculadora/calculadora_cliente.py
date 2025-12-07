import requests

BASE_URL = "https://calculadora-fxpc.onrender.com"

def listar_operacoes():
    print("Consultando Operações")
    try:
        response = requests.get(f"{BASE_URL}/operations")
        if response.status_code == 200:
            print(f"Operações: {response.json()}")
        else:
            print(f"Erro: {response.status_code}")
    except Exception as e:
        print(f"Erro de conexão: {e}")

def calcular(operacao, x, y):
    print(f"\n{operacao} ({x}, {y})")
    url = f"{BASE_URL}/operation/{operacao}/{x}/{y}"
    
    try:
        print(f"URL Chamada: {url}")
        response = requests.post(url)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            dados = response.json()
            resultado = dados.get('result') 
            print(f"Resultado: {resultado}")
        else:
            print(f"Erro ({response.status_code}): {response.text}")
            
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    listar_operacoes()
    calcular("soma", 4, 4)
    calcular("subtracao", 10, 2)
    calcular("multiplicacao", 4, 4)
    calcular("divisao", 10, 2)