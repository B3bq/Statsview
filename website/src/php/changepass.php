<?php
$server = 'localhost';
$login = 'root';
$password = '';
$base = 'statsview';

$conn = mysqli_connect($server, $login, $password, $base);

$mailCookie = $_COOKIE['mail'];

$pass = $_POST['password'];
// hash password
$hash = password_hash($pass, PASSWORD_BCRYPT);
$hash = preg_replace('/^\$2y\$/', '\$2b\$', $hash);


$sql = "UPDATE users SET password = ? WHERE mail = ?";
$query = $conn->prepare($sql);
$query->bind_param("ss", $hash, $mailCookie);
$query->execute();

if ($query){
    echo "ok";
}else{
    echo 'error';
}
?>