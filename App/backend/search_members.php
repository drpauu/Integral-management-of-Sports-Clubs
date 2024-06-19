<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);
header('Content-Type: application/json');
include 'db_connection.php';

$searchQuery = $_GET['searchQuery'];
$query = "SELECT num_soci, nom, data_naixement, sexe, email FROM practica.membre WHERE nom ILIKE ? OR email ILIKE ?";
$stmt = $pdo->prepare($query);
$stmt->execute(["%{$searchQuery}%", "%{$searchQuery}%"]);
$members = $stmt->fetchAll();

echo json_encode($members);
?>
