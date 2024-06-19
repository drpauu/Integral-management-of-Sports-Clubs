<?php
header('Content-Type: application/json');
include 'db_connection.php';

// Ensure there is a teamId parameter in the request
if (!isset($_GET['teamId']) || empty($_GET['teamId'])) {
    http_response_code(400);
    echo json_encode(['error' => 'Team ID is required']);
    exit;
}

$teamId = $_GET['teamId'];

try {
    $query = "SELECT m.num_soci, m.nom, m.data_naixement, m.sexe, m.email
              FROM practica.Membre m
              JOIN practica.Membre_Equip me ON m.num_soci = me.num_soci
              WHERE me.nom_equip = ?";
    $stmt = $pdo->prepare($query);
    $stmt->execute([$teamId]);
    $members = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo json_encode($members);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'Database error: ' . $e->getMessage()]);
}
?>
