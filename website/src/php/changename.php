<?php
require 'connect.php'; //connection to database

$userID = $_COOKIE['user'];
$name = $_POST['name'];

//update name in database
$sql = "UPDATE users SET name = ? WHERE id_users = ?";
$query = $connection->prepare($sql);
$query->bind_param("ss", $name, $userID);
$query->execute();

//update cookie with name
setcookie("name", $name, time()+3600, '/');
setcookie("user", $userID, time()+3600, '/'); //only for this two cookies will be in the same expire time

echo 'changed';
?>