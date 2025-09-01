<?php
if (isset($_GET['code'])) {
    $code = $_GET['code'];
    echo "Recibí el code: " . htmlspecialchars($code);

    // Aquí deberías hacer el intercambio del code por el access_token
    // usando cURL o file_get_contents.
} else {
    echo "No se recibió ningún code";
}
?>
