<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
use Dotenv\Dotenv;

require 'c:/xampp/htdocs/statsview/website/vendor/autoload.php';

$to = $_GET['mail'] ?? '';
$from = $_GET['from'] ?? '';

$mail = new PHPMailer(true);
$dotenv = Dotenv::createImmutable('c:/xampp/htdocs/statsview/website');
$dotenv->load();

$code = rand(1000, 9999);

try{
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;

    $mail->Username = $_ENV['EMAIL_LOGIN'];
    $mail->Password = $_ENV['EMAIL_PASSWORD'];
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
    $mail->Port = 465;

    $mail->setFrom($_ENV['EMAIL_LOGIN'], 'Statsview');

    $mail->addAddress($to);

    $mail->isHTML(true);
    $mail->Subject = 'Verification E-mail';

    if($from == 'account'){
        $mail->Body = '
        <html lang="en" style="font-size: 87.5%; box-sizing: border-box;">
        <body style="display: flex; flex-direction: column;">
            <main style="box-shadow: 0px 2px 2px 2px;">
                <header style="display: flex; flex-direction: column; align-items: center; background-color: #2ECC71;">
                    <h1>Verify Your E-Mail Address</h1>
                    <p style="margin-bottom: 20px;">Use this code to verificate your e-mail address.</p>
                </header>
                <h2 style="display: flex; flex-direction: column; align-items: center;">Your verification code</h2>
                <section style=" display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 20px 0px 20px 0px;">
                    <p style=" display: flex; flex-direction: column; align-items: center; justify-content: center; width: 500px; height: 100px; background-color: #e8e8e8; border-radius: 25px; font-size: 50px">'.$code.'</p>
                </section>
                <footer style="display: flex; flex-direction: column; align-items: center;">
                    <p style="margin-bottom: 0;">If this is not you, ignore the message</p>
                    <p style="margin-bottom: 20px;">Do not reply to this mail, this is an automatically generated message</p>
                </footer>
            </main>
        </body>
        </html>';
    }else{
        $mail->Body = '
        <html lang="en" style="font-size: 87.5%; box-sizing: border-box;">
        <body style="display: flex; flex-direction: column;">
            <main style="box-shadow: 0px 2px 2px 2px;">
                <header style="display: flex; flex-direction: column; align-items: center; background-color: #2ECC71;">
                    <h2 style="margin-bottom: 0;">THANKS FOR SIGNING UP:</h2>
                    <h1>Verify Your E-Mail Address</h1>
                    <p style="margin-bottom: 20px;">Use this code to verificate your e-mail address.</p>
                </header>
                <h2 style="display: flex; flex-direction: column; align-items: center;">Your verification code</h2>
                <section style=" display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 20px 0px 20px 0px;">
                    <p style=" display: flex; flex-direction: column; align-items: center; justify-content: center; width: 500px; height: 100px; background-color: #e8e8e8; border-radius: 25px; font-size: 50px">'.$code.'</p>
                </section>
                <footer style="display: flex; flex-direction: column; align-items: center;">
                    <p style="margin-bottom: 0;">If this is not you, ignore the message</p>
                    <p style="margin-bottom: 20px;">Do not reply to this mail, this is an automatically generated message</p>
                </footer>
            </main>
        </body>
        </html>';
    }

    $mail->send();
}catch(Exception $e){
    echo "Error: {$mail->ErrorInfo}";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statsview</title>
    <link rel="stylesheet" href="src/sass/style.css">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

    <script type="module" src="src/js/script.js" defer></script>
</head>
<body>
    <header>
        <!--logo-->
        <a href="index.html" title="Back to home page">
            <img src="" alt="logo">
        </a>
        <nav>
            <button id="js-toggle-menu">
                <img width="46" height="46" src="src/img/burger-bar.png" alt="Toggle menu" id="menu">
            </button>

            <ul id="js-toggleable-menu">
                <li><a href="" title="" id="option1"></a></li>
                <li><a href="#about" title="About the project" id="option2">About</a></li>
                <li><a href="" title="">Dowland app</a></li>
                <li><a href="login.html" title="Log in site" id="logout">Log in</a></li>
            </ul>
        </nav>
    </header>
    <main class="verification">
        <h1>Enter your verification code</h1>
        <section class="verification__code" contenteditable="true" spellcheck="false">
            <input type="text" maxlength="1" class="code">
            <input type="text" maxlength="1" class="code">
            <input type="text" maxlength="1" class="code">
            <input type="text" maxlength="1" class="code">
        </section>
        <button>Verify</button>
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