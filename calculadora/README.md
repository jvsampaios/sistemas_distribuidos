# AT03 - Invocação Remota e Comunicação Indireta

O objetivo central da atividade foi desenvolver uma **Calculadora Distribuída** capaz de realizar operações básicas e processamento de expressões complexas.

## Equipe

* **João Victor Sampaio da Silva** - Matrícula: 584236
* **José Carlos Wolff Rodrigues Júnior** - Matrícula: 485129
* **Luis Fernando Lima da Silva** - Matrícula: 539080
* **Matheus Teixeira Guimarães** - Matrícula: 584236

## Estrutura

O projeto está modularizado em três diretórios principais, cada um representando uma tecnologia de comunicação diferente:

### 1. `sockets/`
Implementação utilizando a API de **BSD Sockets** pura.

### 2. `RMI/`
Implementação utilizando **Pyro4** (Python Remote Objects) para abstração de rede.

### 3. `HTTP/`
Implementação de um cliente HTTP consumindo uma API REST.

## Como Executar

Cada pasta possui seu próprio `README.md` com instruções detalhadas de execução. De forma resumida:

1.  **Para Sockets:** Acesse `sockets/` e rode o servidor e cliente Python.
3.  **Para HTTP:** Acesse `http/`, suba o servidor PHP (`php -S`) e rode o cliente Python.
2.  **Para RMI:** Acesse `rmi/`, inicie o Name Server (`pyro4-ns`), depois o servidor e por fim o cliente.