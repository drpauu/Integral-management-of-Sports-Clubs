<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
header('Content-Type: application/json');

$host = 'localhost'; // or the appropriate hostname of your database server
$dbname = 'est_c4414773'; // Nom de la teva base de dades
$user = 'est_c4414773'; // Usuari que has creat o 'postgres'
$pass = 'dB.c4414773'; // Contrasenya que has assignat
$dsn = "pgsql:host=$host;dbname=$dbname";

try {
    $pdo = new PDO($dsn, $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Make sure errors throw exceptions
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    $stmt = $pdo->query('SELECT num_soci, nom, data_naixement, sexe, email FROM practica.membre');
    $members = $stmt->fetchAll();

    echo json_encode($members);
} catch (PDOException $e) {
    http_response_code(500); // Set HTTP response code appropriately
    echo json_encode(['error' => $e->getMessage()]); // Provide error message in JSON format
}
?>
