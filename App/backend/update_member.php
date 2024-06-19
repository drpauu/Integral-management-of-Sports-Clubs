// update_member.php
<?php
include 'db_connection.php';

$num_soci = $_POST['num_soci'];
$nom = $_POST['nom'];
$data_naixement = $_POST['data_naixement'];
$sexe = $_POST['sexe'];
$email = $_POST['email'];

$query = "UPDATE practica.membre SET nom=?, data_naixement=?, sexe=?, email=? WHERE num_soci=?";
$stmt = $pdo->prepare($query);
$result = $stmt->execute([$nom, $data_naixement, $sexe, $email, $num_soci]);

echo json_encode(['success' => $result]);
