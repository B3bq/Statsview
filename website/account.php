<?php
require 'c:/xampp/htdocs/statsview/website/src/php/connect.php';

$userID = $_COOKIE['user']; //get user id from cookie

//taking e-mail
$sql = "SELECT mail FROM users WHERE id_users = ?";
$query = $connection->prepare($sql);
$query->bind_param("s", $userID);
$query->execute();
$result = $query->get_result();
$mail = $result->fetch_assoc()['mail'];

//taking name
$sql = "SELECT name FROM users WHERE id_users = ?";
$query = $connection->prepare($sql);
$query->bind_param("s", $userID);
$query->execute();
$result = $query->get_result();
$name = $result->fetch_assoc()['name'];

//taking profile photo
$sql = "SELECT photo FROM users WHERE id_users = ?";
$query = $connection->prepare($sql);
$query->bind_param("s", $userID);
$query->execute();
$result = $query->get_result();
$photo = $result->fetch_assoc()['photo'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statsview</title>
    <link rel="stylesheet" href="src/sass/style.css">
    <link rel="shortcut icon" href="src/img/logo.svg" type="image/x-icon">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

    <script type="module" src="src/js/script.js" defer></script>
    <script type="module" src="src/js/photo.js" defer></script>
    <script src="src/js/functions.js"></script>
</head>
<body>
    <header>
        <a href="index.html" title="Back to home page">
            <img src="src/img/logo.svg" alt="logo" width="64px" height="64px">
        </a>
        <nav>
            <button id="js-toggle-menu">
                <img width="46" height="46" src="src/img/burger-bar.png" alt="Toggle menu" id="menu">
            </button>

            <ul id="js-toggleable-menu">
                <li><a href="" title="" id="option1"></a></li>
                <li><a href="index.html#about" title="About the project" id="option2">About</a></li>
                <li><a href="download.html" title="">Dowland app</a></li>
                <li><a href="login.html" title="Log in site" id="logout">Log in</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="personal">
        <header>
            <img src="<?php echo $photo?>" alt="profile" id='profil'>
            <button id='showPhotos'><img src="src/img/circle.png" alt="change profile photo"></button>
            <div id="photos" class="personal__photos">
                <img src="src/img/user.png" name='profil' alt="profil1">
                <img src="src/img/tennis-player.png" name='profil' alt="profil2">
                <img src="src/img/basket.png" name='profil' alt="profil3">
                <img src="src/img/soccer-player2.png" name='profil' alt="profil4">
                <img src="src/img/panda.png" name='profil' alt="profil5">
                <img src="src/img/soccer-player.png" name='profil' alt="profil6">
                <img src="src/img/handball.png" name='profil' alt="profil7">
                <img src="src/img/athlete.png" name='profil' alt="profil8">
                <div>
                    <img src="src/img/cancel.png" alt="cancel" id="cancelProfile">
                    <img src="src/img/check.png" alt="agree" onclick='update()'>
                </div>
            </div>
            <div contenteditable="false" spellcheck="false" id='userName'><?php echo $name?></div>
            <button onclick="resetValue('userName')" type="button" id="cancel" class="cancel" hidden><img src="src/img/cancel.png" alt="cancel"></button>
            <button onclick="changeName()" type="button" id="confirm" class="confirm" hidden><img src="src/img/check.png" alt="confirm"></button>
            <img src="src/img/circle.png" alt="change name" id="edit" onclick="enableEditing()">
        </header>
            <section class="personal__mail">
                <input type="text"  id="input1" disabled value="<?php echo $mail?>">
                <button onclick="resetValue('input1')" type="button" id="cancel1" class="cancel" hidden><img src="src/img/cancel.png" alt="cancel"></button>
                <p id="response" hidden></p>
                <button onclick="changeMail('account')" type="button" id="confirm1" class="confirm" hidden><img src="src/img/check.png" alt="confirm"></button>
                <button onclick="enableInput('input1','confirm1', 'cancel1', 'change1')" id="change1"><img src="src/img/pencil.png" alt="pencil"></button>
            </section>
            <section class="personal__pass">
                <input type="password" id="input2" disabled value="password">
                <button onclick="enableInput('input2', 'confirm2', 'cancel2', 'change2', 'repeat', 'show')" id="change2"><img src="src/img/pencil.png" alt="pencil"></button>
                <input type="password" id="repeat" class="repeat" hidden value="password">
                <img src="src/img/hide.png" alt="hide eye" id="show" hidden onclick="showPassword('show', 'input2', 'repeat')">
                <button onclick="resetValue('input2')" type="button" id="cancel2" class="personal__pass-cancel" hidden><img src="src/img/cancel.png" alt="cancel"></button>
                <button onclick="passChange()" type="button" id="confirm2" class="personal__pass-confirm" hidden><img src="src/img/check.png" alt="confirm"></button>
                <p id="info" hidden></p>
            </section>
        </section>
    </main>
    <footer>
        <a href="https://github.com/B3bq" target="_blank" >
            <img src="src/img/github-brands.svg" alt="github">
        </a>
        <a href="mailto:" title="E-mail">mail</a>

        <p>© 2025 studio</p>
    </footer>
</body>
</html>