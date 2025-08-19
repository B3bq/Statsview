<?php
require 'connect.php';

$userID = $_COOKIE['user'];

$sql = "SELECT photo FROM users WHERE id_users = ?";
$query = $connection->prepare($sql);
$query->bind_param("s", $userID);
$query->execute();
$result = $query->get_result();
$photo = $result->fetch_assoc()['photo'];

echo $photo;
?>