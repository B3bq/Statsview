<?php
$server = "localhost";
$login = "root";
$password = "";
$base = "statsview";

$connect = mysqli_connect($server, $login, $password, $base); //connecting to database

// getting a user login data
$login = $_POST['login'];
$password = $_POST['password'];
$sqlCheck = "SELECT mail, name FROM users WHERE mail = ? OR name = ?";
$query = $connect->prepare($sqlCheck); // prepare to execute
$query->bind_param("ss", $login, $login); // insert a data
$query->execute(); // executing
$result = $query->get_result(); // getting a result to varible

if($result->num_rows>0){
    // taking user id
    $sqlUserID = "SELECT id_users FROM users WHERE name = ? OR mail = ?";
    $query = $connect->prepare($sqlUserID);
    $query->bind_param("ss", $login, $login);
    $query->execute();
    $result = $query->get_result();
    $UserID = $result->fetch_assoc()['id_users'];
    
    // taking user name
    $sqlUserName = "SELECT name FROM users WHERE name = ? OR mail = ?";
    $query = $connect->prepare($sqlUserName);
    $query->bind_param("ss", $login, $login);
    $query->execute();
    $result = $query->get_result();
    $UserName = $result->fetch_assoc()['name'];

    // setting cookies for seven days
    setcookie("user", $UserID, time()+(7*24*60*60), '/');
    setcookie("name", $UserName, time()+(7*24*60*60), '/');
    echo "Alles klar";
}
?>