<?php
header('Content-Type: application/json');
include 'db_connection.php';

$response = ['success' => false];

try {
    $num_soci = $_POST['num_soci'] ?? '';
    $nom = $_POST['nom'] ?? '';
    $data_naixement = $_POST['data_naixement'] ?? '';
    $sexe = $_POST['sexe'] ?? '';
    $email = $_POST['email'] ?? '';

    $query = "INSERT INTO practica.membre (num_soci, nom, data_naixement, sexe, email) VALUES (?, ?, ?, ?, ?)";
    $stmt = $pdo->prepare($query);
    $stmt->execute([$num_soci, $nom, $data_naixement, $sexe, $email]);
    
    $response['success'] = true;
} catch (PDOException $e) {
    $response['error'] = $e->getMessage();
}

echo json_encode($response);
