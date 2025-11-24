# Atividade SD - Middleware e RMI (Python/Pyro4)

## Descrição do Projeto

Este projeto implementa uma **Calculadora Distribuída** utilizando o conceito de **RMI (Remote Method Invocation)**.

O sistema permite duas modalidades de cálculo:
1.  **Operações Básicas:** O cliente escolhe a operação e envia os operandos. O servidor processa e retorna.
2.  **Expressão Completa (Offloading):** O cliente envia uma expressão matemática complexa (ex: `(10+5)*2`) e o servidor realiza o *parsing* e o cálculo, retornando apenas o resultado final.

## Como Executar

### Pré-requisitos
1.  **Python 3** instalado.
2.  **Biblioteca `Pyro4`** instalada:
    ```bash
    pip install Pyro4
    ```
### Passo 1: Iniciar o Name Server
Abra um terminal e digite:

```bash
python -m Pyro4.naming
```
Este serviço deve ficar rodando para permitir que cliente e servidor se encontrem.
Aguarde a mensagem: NS running on localhost:9090

### Passo 2: Iniciar o Servidor
Abra outro terminal na mesma pasta e inicie o servidor:

```bash
python calculadora_server.py
```
### Passo 3: Iniciar o Cliente
Abra mais um terminal na mesma pasta e inicie o cliente:

```bash
python calculadora_client.py
```