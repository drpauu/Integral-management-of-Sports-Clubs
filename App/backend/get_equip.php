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
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);

    // SQL Query to fetch team details and their members
    $sql = 'SELECT e.nom AS team_name, e.esport AS sport, e.categoria AS category, array_agg(m.nom) AS members
            FROM practica.Equip e
            LEFT JOIN practica.Membre_Equip me ON e.nom = me.nom_equip
            LEFT JOIN practica.Membre m ON me.num_soci = m.num_soci
            GROUP BY e.nom, e.esport, e.categoria';

    $stmt = $pdo->query($sql);
    $teams_with_members = $stmt->fetchAll();

    echo json_encode($teams_with_members);
} catch (PDOException $e) {
    http_response_code(500); // Set HTTP response code appropriately
    echo json_encode(['error' => $e->getMessage()]); // Provide error message in JSON format
}
?>
