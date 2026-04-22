<?php
$server = getenv('DB_HOST') ?: 'localhost';
$login = getenv('DB_USER') ?: 'root';
$password = getenv('DB_PASSWORD') ?: '';
$base = getenv('DB_NAME') ?: 'statsview';
$port = getenv('DB_PORT') ?: 3306;

try {
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
    $connection = mysqli_connect($server, $login, $password, $base, $port);
}
catch (mysqli_sql_exception $e) {
    $connection = false;
    $connection_error = $e->getMessage();
}