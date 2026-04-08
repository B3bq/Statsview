<?php
$server = getenv('DB_HOST') ?: 'localhost';
$login = getenv('DB_USER') ?: 'root';
$password = getenv('DB_PASSWORD') ?: '';
$base = getenv('DB_NAME') ?: 'statsview';
$port = getenv('DB_PORT') ?: 3306;

$connection = mysqli_connect($server, $login, $password, $base, $port);
?>