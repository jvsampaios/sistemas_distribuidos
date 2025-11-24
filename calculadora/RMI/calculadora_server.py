import Pyro4

@Pyro4.expose # define que esta classe e seus métodos podem ser acessados remotamente.
class Calculadora(object):
    
    def __init__(self):
        self.chamadas = 0

    def soma(self, a, b):
        print(f"[Log] Método soma chamado.")
        self._incrementa_contador()
        return a + b

    def subtrai(self, a, b):
        print("[Log] Método subtrai chamado.")
        self._incrementa_contador()
        return a - b

    def multiplica(self, a, b):
        print("[Log] Método multiplica chamado.")
        self._incrementa_contador()
        return a * b

    def divide(self, a, b):
        print("[Log] Método divide chamado.")
        self._incrementa_contador()
        if b == 0:
            raise ValueError("Divisão por zero não permitida!")
        return a / b

    def _incrementa_contador(self):
        self.chamadas += 1
        print(f"[Log] Total de requisições atendidas: {self.chamadas}")

    # Cálculo de expressão completa no servidor
    def calcula_expressao(self, expressao):
        print(f"[Log] Calculando expressão: {expressao}")
        try:
            # Em RMI, o processamento pesado fica no servidor. O cliente envia a string, processamos e devolvemos o float. Com eval igual nas outras questões
            return float(eval(expressao))
        except Exception as e:
            return f"Erro ao calcular: {str(e)}"

def main():
    # Cria o Daemon
    daemon = Pyro4.Daemon() 
    
    # Localiza o Name Server
    ns = Pyro4.locateNS() 
    
    # Instancia o objeto real
    obj_calculadora = Calculadora()
    
    # Registra o objeto no Daemon para que ele possa receber chamadas
    uri = daemon.register(obj_calculadora)
    
    # Registra o objeto no Name Server com um nome amigável
    ns.register("calculadora", uri)
    
    print("[*] Servidor RMI pronto. Aguardando chamadas de objetos remotos...")
    
    # Loop infinito aguardando requisições
    daemon.requestLoop()

if __name__ == "__main__":
    main()