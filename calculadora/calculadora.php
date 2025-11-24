<?php
// [SERVER-SIDE] Calculadora remota via POST
// Este script atua como uma API REST simples, recebendo dados e retornando JSON.

// [DADOS] Função auxiliar para pegar dados do POST de forma segura
function getPostValue($key) {
    // Verifica se a chave existe no array superglobal $_POST
    return isset($_POST[$key]) ? floatval($_POST[$key]) : null;
}

// [REQ-RESP] Recebimento dos parâmetros enviados pelo Cliente HTTP
$oper1 = getPostValue('oper1');
$oper2 = getPostValue('oper2');
// A operação é um inteiro: 1:+, 2:-, 3:*, 4:/
$operacao = isset($_POST['operacao']) ? intval($_POST['operacao']) : null;

$resultado = null;
$erro = null;

// [LÓGICA] Validação básica dos dados de entrada
if ($oper1 === null || $oper2 === null || $operacao === null) {
    $erro = "Parâmetros inválidos. Envie 'oper1', 'oper2' e 'operacao' via POST.";
} else {
    // Processamento da regra de negócio (Cálculos)
    switch ($operacao) {
        case 1: // Soma
            $resultado = $oper1 + $oper2;
            break;
        case 2: // Subtração
            $resultado = $oper1 - $oper2;
            break;
        case 3: // Multiplicação
            $resultado = $oper1 * $oper2;
            break;
        case 4: // Divisão
            if ($oper2 == 0) {
                $erro = "Erro: divisão por zero.";
            } else {
                $resultado = $oper1 / $oper2;
            }
            break;
        default:
            $erro = "Operação inválida. Use 1 a 4.";
    }
}

// [PROTOCOLO] Define o cabeçalho HTTP para informar que a resposta é um JSON
header('Content-Type: application/json');

// [RESPOSTA] Serialização da resposta (Array PHP -> JSON String)
if ($erro) {
    // Retorna objeto de erro se algo falhou
    echo json_encode(["erro" => $erro]);
} else {
    // Retorna o resultado e os parâmetros originais (stateless)
    echo json_encode([
        "oper1" => $oper1,
        "oper2" => $oper2,
        "operacao" => $operacao,
        "resultado" => $resultado
    ]);
}
?>