<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
use Dotenv\Dotenv;

require_once __DIR__ . '/../../vendor/autoload.php';

$to = $_POST['mail'];

$mail = new PHPMailer(true);
$dotenv = Dotenv::createImmutable(__DIR__ . '/../../');
$dotenv->safeLoad();

$apiKey = $_ENV['BREVO_API_KEY'] ?? getenv('BREVO_API_KEY');
$senderEmail = $_ENV['EMAIL_LOGIN'] ?? getenv('EMAIL_LOGIN');

$body = '
        <html lang="en" style="font-size: 87.5%; box-sizing: border-box;">
            <body style="display: flex; flex-direction: column;">
                <main style="box-shadow: 0px 2px 2px 2px;">
                    <header style="display: flex; flex-direction: column; align-items: center; background-color: #2ECC71;">
                        <h2 style="margin-bottom: 0;">Reset your password</h2>
                        <p style="margin-bottom: 20px;">Use this link to reset your password</p>
                    </header>
                    <section style=" display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 20px 0px 20px 0px;">
                        <p style=" display: flex; flex-direction: column; align-items: center; justify-content: center; width: 500px; height: 100px; background-color: #e8e8e8; border-radius: 25px; font-size: 25px">
                            <a href="https://statsview-pccg.onrender.com/changepass.html">CHANGE PASSWORD</a>
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

$data = [
    "sender" => [
        "name" => "Statsview",
        "email" => $senderEmail
    ],
    "to" => [
        ["email" => $to]
    ],
    "subject" => 'Reset password',
    "htmlContent" => $body
];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.brevo.com/v3/smtp/email');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'accept: application/json',
    'api-key: ' . $apiKey,
    'content-type: application/json'
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpCode >= 200 && $httpCode < 300) {
    echo 'sent';
}
else {
    echo "Error: HTTP Code $httpCode Response: $response";
}
?>
