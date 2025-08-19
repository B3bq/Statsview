<?php
require 'connect.php';

$src = $_POST['src'];
$userID = $_COOKIE['user'];

$sql = "UPDATE users SET photo = '$src' WHERE id_users = $userID";
mysqli_query($connection, $sql);

echo true;
?>