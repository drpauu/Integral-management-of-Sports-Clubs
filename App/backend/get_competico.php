<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
header('Content-Type: application/json');

$host = 'localhost'; // or the appropriate hostname of your database server
$dbname = 'est_c4414773'; // Your database name
$user = 'est_c4414773'; // Your database username
$pass = 'dB.c4414773'; // Your database password
$dsn = "pgsql:host=$host;dbname=$dbname";

try {
    $pdo = new PDO($dsn, $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Ensure errors throw exceptions
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    $stmt = $pdo->query('SELECT nom, esport, categoria, any_celebracio FROM practica.Competició');
    $competitions = $stmt->fetchAll();

    echo json_encode($competitions);
} catch (PDOException $e) {
    http_response_code(500); // Set HTTP response code appropriately
    echo json_encode(['error' => $e->getMessage()]); // Provide error message in JSON format
}
?>
