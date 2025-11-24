# Atividade SD - Invocação Remota (HTTP) e Tolerância a Falhas
# Calculadora Distribuída com Retry

## Descrição do Projeto

Este projeto implementa um sistema de **Calculadora Distribuída** utilizando o modelo arquitetural Cliente-Servidor sobre o protocolo **HTTP**.

O sistema permite duas modalidades de cálculo:
1.  **Operações Básicas:** O cliente escolhe a operação e envia os operandos. O servidor processa e retorna.
2.  **Expressão Completa (Offloading):** O cliente envia uma expressão matemática complexa (ex: `(10+5)*2`) e o servidor realiza o *parsing* e o cálculo, retornando apenas o resultado final.

## Funcionalidades Implementadas

* **Política de Retry:** Implementa um mecanismo de "Wait & Retry". Se o servidor retornar um erro de família 500 ou se houver falha de conexão, o cliente aguarda 2 segundos e tenta novamente até 3 vezes.
* **Tratamento de Erros:** Diferencia erros de cliente (família 400, que não fará retry) de erros de servidor/rede (que fará retry).

---

## Como Executar

### Pré-requisitos
1.  **Python 3** instalado.
2.  **Biblioteca `requests`** instalada:
    ```bash
    pip install requests
    ```
3.  **PHP** instalado.

### Passo 1: Subir o Servidor (PHP)
Abra um terminal na pasta onde está o arquivo `calculadora.php` e inicie o servidor embutido do PHP na porta 8000:

```bash
php -S localhost:8000
```

### Passo 2: Executar o Cliente (Python)
Abra outro terminal na mesma pasta e execute o cliente:
```bash
python calculadora_client.py
```