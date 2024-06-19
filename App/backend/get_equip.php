<?php
header('Content-Type: application/json');
include 'db_connection.php';

try {
    $query = "SELECT e.nom, e.esport FROM practica.Equip e";
    $stmt = $pdo->query($query);
    $teams = $stmt->fetchAll(PDO::FETCH_ASSOC);
    echo json_encode($teams);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'Database error: ' . $e->getMessage()]);
}
?>
