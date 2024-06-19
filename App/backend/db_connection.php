<?php
// Database credentials
$host = 'localhost'; // or the appropriate hostname of your database server
$dbname = 'est_c4414773'; // Nom de la teva base de dades
$user = 'est_c4414773'; // Usuari que has creat o 'postgres'
$pass = 'dB.c4414773'; // Contrasenya que has assignat

// Data Source Name
$dsn = "pgsql:host=$host;dbname=$dbname";

// Options for PDO
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES => false,
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
    $pdo->exec("SET NAMES 'UTF8'");

} catch (\PDOException $e) {
    // Handle connection error
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Now, you can include this file in other PHP scripts to use $pdo for database operations.
?>
