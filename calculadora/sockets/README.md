# Atividade SD - Comunicação de Baixo Nível com Sockets TCP
# Calculadora Distribuída

## 📝 Descrição do Projeto

Este projeto implementa um sistema de **Calculadora Distribuída** utilizando a API de **BSD Sockets** sobre o protocolo **TCP/IP**.

O sistema permite duas modalidades de cálculo:
1.  **Operações Básicas:** O cliente escolhe a operação e envia os operandos. O servidor processa e retorna.
2.  **Expressão Completa (Offloading):** O cliente envia uma expressão matemática complexa (ex: `(10+5)*2`) e o servidor realiza o *parsing* e o cálculo, retornando apenas o resultado final.


## Como Executar

### Pré-requisitos
* **Python 3** instalado.
* Não é necessária nenhuma biblioteca externa (usa apenas a standard lib `socket`).

### Passo 1: Iniciar o Servidor
Abra um terminal na pasta do projeto e execute:

```bash
python calculadora_server.py
```

### Passo 2: Executar o Cliente (Python)
Abra outro terminal na mesma pasta e execute o cliente:
```bash
python calculadora_client.py
```