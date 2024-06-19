<?php
header('Content-Type: application/json');
include 'db_connection.php';

$page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
$limit = isset($_GET['limit']) ? (int)$_GET['limit'] : 10;
$offset = ($page - 1) * $limit;

try {
    // Constructing SQL query to fetch competitions, excluding 'categoria'
    $stmt = $pdo->prepare("SELECT c.nom, c.esport, c.any_celebracio, COUNT(*) OVER() AS full_count FROM practica.Competició c JOIN practica.Esport e ON c.esport = e.nom LIMIT :limit OFFSET :offset");
    $stmt->bindParam(':limit', $limit, PDO::PARAM_INT);
    $stmt->bindParam(':offset', $offset, PDO::PARAM_INT);
    $stmt->execute();

    $competitions = $stmt->fetchAll(PDO::FETCH_ASSOC);
    $totalCompetitions = count($competitions) > 0 ? (int)$competitions[0]['full_count'] : 0;

    echo json_encode(['competitions' => $competitions, 'totalCompetitions' => $totalCompetitions]);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(['error' => 'Database error: ' . $e->getMessage()]);
}
?>
