<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
use Dotenv\Dotenv;

require_once 'c:/xampp/htdocs/statsview/website/vendor/autoload.php';

$to = $_POST['mail'];

$mail = new PHPMailer(true);
$dotenv = Dotenv::createImmutable('c:/xampp/htdocs/statsview/website');
$dotenv->load();

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
    $mail->Subject = 'Reset password';

    $mail->Body = '
        <html lang="en" style="font-size: 87.5%; box-sizing: border-box;">
            <body style="display: flex; flex-direction: column;">
                <main style="box-shadow: 0px 2px 2px 2px;">
                    <header style="display: flex; flex-direction: column; align-items: center; background-color: #2ECC71;">
                        <h2 style="margin-bottom: 0;">Reset your password</h2>
                        <p style="margin-bottom: 20px;">Use this link to reset your password</p>
                    </header>
                    <section style=" display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 20px 0px 20px 0px;">
                        <p style=" display: flex; flex-direction: column; align-items: center; justify-content: center; width: 500px; height: 100px; background-color: #e8e8e8; border-radius: 25px; font-size: 25px">
                            <a href="192.168.1.12/statsview/website/changepass.html">CHANGE PASSWORD</a>
                        </p>
                    </section>
                    <footer style="display: flex; flex-direction: column; align-items: center;">
                        <p style="margin-bottom: 0;">If this is not you, ignore the message</p>
                        <p style="margin-bottom: 20px;">Do not reply to this mail, this is an automatically generated message</p>
                    </footer>
                </main>
            </body>
            </html>
        ';
    $mail->send();
    echo 'sent';
}catch(Exception $e){
    echo "Error: {$mail->ErrorInfo}";
}
?>
