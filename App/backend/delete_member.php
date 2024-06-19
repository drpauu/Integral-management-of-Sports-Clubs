<?php
include 'db_connection.php';
header('Content-Type: application/json');

$data = json_decode(file_get_contents("php://input"), true);
$num_soci = $data['num_soci'];

try {
    // Begin transaction
    $pdo->beginTransaction();

    // Delete dependent records from membre_equip
    $stmt1 = $pdo->prepare("DELETE FROM practica.membre_equip WHERE num_soci = ?");
    $stmt1->execute([$num_soci]);

    // Delete the member record from membre
    $stmt2 = $pdo->prepare("DELETE FROM practica.membre WHERE num_soci = ?");
    $stmt2->execute([$num_soci]);

    // Commit transaction
    $pdo->commit();

    echo json_encode(['success' => true, 'message' => 'Membre eliminat amb èxit']);
} catch (PDOException $e) {
    // Roll back transaction if there's an error
    $pdo->rollback();
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
