<?php
$server = 'localhost';
$login = 'root';
$password = '';
$base = 'statsview';

$conn = mysqli_connect($server, $login, $password, $base);

session_start();

//parametrs are given by js
$mail = $_POST['mail'] ?? '';
$from = $_POST['from'] ?? '';
$userCode = $_POST['userCode'] ?? '';

$expectedCode = $_SESSION['code'] ?? ''; //teke this from session, which is maked by verification

if($userCode == $expectedCode){
    if($from == 'account'){
        //chnging e-mail in account
        $userID = $_COOKIE['user'];
        $sql = "UPDATE users SET mail = ? WHERE id_users = ?";
        $query = $conn->prepare($sql);
        $query->bind_param("ss", $mail, $userID);
        $query->execute();
        echo 'ok';
    }else{
        //add new user
        $name = $_POST['name'];
        $pass = $_POST['pass'];
        $hash = password_hash($pass, PASSWORD_BCRYPT);
        $hash = preg_replace('/^\$2y\$/', '\$2b\$', $hash);
        $sql = "INSERT INTO users(id_users, mail, name, password) VALUES (NULL, ?, ?, ?)";
        $query = $conn->prepare($sql);
        $query->bind_param("sss", $mail, $name, $hash);
        echo 'ok';
    }
}else{
    echo 'Invalid code';
}
?>