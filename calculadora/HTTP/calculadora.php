<?php

header('Content-Type: application/json');

// Função auxiliar para pegar dados do POST

function getPost($key) { return isset($_POST[$key]) ? $_POST[$key] : null; }

// Recebe os dados
$opCode = getPost('operacao');
$oper1  = getPost('oper1');
$oper2  = getPost('oper2');
$expr   = getPost('expressao');

$resultado = null;
$erro = null;

// Calcula a string completa no servidor

if ($opCode == 5 && $expr != null) {
    try {
        // Validação dos caracteres permitidos
        if (preg_match('/^[0-9\+\-\*\/\.\(\)\ ]+$/', $expr)) {
            $p = eval('return '.$expr.';');
            $resultado = $p;
        } else {
            $erro = "Caracteres inválidos na expressão.";
        }
    } catch (Throwable $t) {
        $erro = "Erro de sintaxe na expressão.";
    }
    // Operações aritméticas simples (+,-,/,*)
} elseif ($opCode >= 1 && $opCode <= 4 && $oper1 !== null && $oper2 !== null) {
    $n1 = floatval($oper1);
    $n2 = floatval($oper2);
    
    switch ($opCode) {
        case 1: $resultado = $n1 + $n2; break;
        case 2: $resultado = $n1 - $n2; break;
        case 3: $resultado = $n1 * $n2; break;
        case 4: 
            if ($n2 == 0) $erro = "Divisão por zero";
            else $resultado = $n1 / $n2; 
            break;
    }
} else {
    $erro = "Parâmetros insuficientes ou operação inválida.";
}

// Retorno da resposta
if ($erro) echo json_encode(["erro" => $erro]);
else echo json_encode(["resultado" => $resultado]);
?>