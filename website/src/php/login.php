<?php
require 'connect.php'; //connecting to database

// getting a user login data
$login = $_POST['login'];
$password = $_POST['password'];
$sqlCheck = "SELECT mail, name FROM users WHERE mail = ? OR name = ?";
$query = $connection->prepare($sqlCheck); // prepare to execute
$query->bind_param("ss", $login, $login); // insert a data
$query->execute(); // executing
$result = $query->get_result(); // getting a result to varible

$lang = $_POST['lang'] ?? '';

if($result->num_rows>0){ // if number of rows is bigger than 0 that league exist
    $sqlPassCheck = "SELECT password FROM users WHERE name = ? or mail = ?";
    $query = $connection->prepare($sqlPassCheck);
    $query->bind_param("ss", $login, $login);
    $query->execute();
    $result = $query->get_result();
    $databasePass = $result->fetch_assoc()['password']; // getting only values in password column
    
    if(password_verify($password, $databasePass)){ // checking password with hashed password in database
        // taking user id
        $sqlUserID = "SELECT id_users FROM users WHERE name = ? OR mail = ?";
        $query = $connection->prepare($sqlUserID);
        $query->bind_param("ss", $login, $login);
        $query->execute();
        $result = $query->get_result();
        $UserID = $result->fetch_assoc()['id_users'];
        
        // taking user name
        $sqlUserName = "SELECT name FROM users WHERE name = ? OR mail = ?";
        $query = $connection->prepare($sqlUserName);
        $query->bind_param("ss", $login, $login);
        $query->execute();
        $result = $query->get_result();
        $UserName = $result->fetch_assoc()['name'];
            
        if(isset($_COOKIE['user']) && $_COOKIE['name']){
            // blank run: no action is taken here
        }else{
            setcookie("user", $UserID, time()+3600, '/'); // setting cookie for an hour    
            setcookie("name", $UserName, time()+3600, '/');
        }
        echo "OK"; // if true give OK result
    }
    else{
        if($lang == 'pl'){
            echo "Niepoprawne hasło";
        }else{
            echo "Incorrect password";
        }
    }
}
else{
    if($lang == 'pl'){
        echo "Nie znaleziono użytkownika";
    }else{
        echo "User not found";
    }
}
?>