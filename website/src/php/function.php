<?php

//function CheckUser($login, $password){
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

    if($result->num_rows>0){ // if number of rows is bigger than 0 that league exist
        $sqlPassCheck = "SELECT password FROM users WHERE name = ? or mail = ?";
        $query = $connect->prepare($sqlPassCheck);
        $query->bind_param("ss", $login, $login);
        $query->execute();
        $result = $query->get_result();
        $databasePass = $result->fetch_assoc()['password']; // getting only values in password column

        if(password_verify($password, $databasePass)){ // checking password with hashed password in database
            
            // taking user id
            $sqlUserID = "SELECT id_users FROM users WHERE name = ? OR mail = ?";
            $query = $connect->prepare($sqlUserID);
            $query->bind_param("ss", $login, $login);
            $query->execute();
            $result = $query->get_result();
            $UserID = $result->fetch_assoc()['id_users'];

            setcookie("user", $UserID, time()+3600, '/', "", false, true); // setting cookie for an hour

            echo "OK"; // if true give OK result
        }
        else{
            echo "Incorrect password";
        }
    }
    else{
        echo "User not found";
    }
//}
?>