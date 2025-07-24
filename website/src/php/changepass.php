<?php
require 'connect.php'; //connection to database

$pass = $_POST['password']; //it gives a js code
// hash password
$hash = password_hash($pass, PASSWORD_BCRYPT);
$hash = preg_replace('/^\$2y\$/', '\$2b\$', $hash);

if(isset($_COOKIE['mail'])){ //this sector is for reset password by mail
    $mailCookie = $_COOKIE['mail']; //taking mail from cookie
    $sql = "UPDATE users SET password = ? WHERE mail = ?";
    $query = $connection->prepare($sql);
    $query->bind_param("ss", $hash, $mailCookie);
    $query->execute();
}else{ //this sector is for reset password from account panel
    $userID = $_COOKIE['user']; //taking user id from cookie
    $sql = "UPDATE users SET password = ? WHERE id_users = ?";
    $query = $connection->prepare($sql);
    $query->bind_param("ss", $hash, $userID);
    $query->execute();
}

if ($query){
    echo "ok";
}else{
    echo 'error';
}
?>