<?php
$server = 'localhost';
$login = 'root';
$password = '';
$base = 'base';

$conn = mysqli_connect($server, $login, $password, $base);

$userID = $_COOKIE['user'];
$name = $_POST['name'];

//update name in database
$sql = "UPDATE users SET name = ? WHERE id_users = ?";
$query = $conn->prepare($sql);
$query->bind_param("ss", $name, $userID);
$query->execute();

//update cookie with name
setcookie("name", $name, time()+3600, '/');
setcookie("user", $userID, time()+3600, '/'); //only for this two cookies will be in the same expire time

echo 'changed';
?>