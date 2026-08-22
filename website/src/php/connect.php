<?php
$databaseUrl = getenv('DATABASE_URL') ?: getenv('MYSQL_URL') ?: getenv('CLEARDB_DATABASE_URL') ?: getenv('JAWSDB_URL');

if ($databaseUrl) {
    $parsed = parse_url($databaseUrl);

    if (is_array($parsed) && !empty($parsed['host'])) {
        $server = $parsed['host'];
        $login = $parsed['user'] ?? 'root';
        $password = $parsed['pass'] ?? '';
        $base = ltrim($parsed['path'] ?? '/', '/');
        $port = $parsed['port'] ?? 3306;
    }
}

if (empty($server)) {
    $server = getenv('DB_HOST') ?: 'localhost';
}
if (empty($login)) {
    $login = getenv('DB_USER') ?: 'root';
}
if (!isset($password)) {
    $password = getenv('DB_PASSWORD') ?: '';
}
if (empty($base)) {
    $base = getenv('DB_NAME') ?: 'statsview';
}
if (empty($port)) {
    $port = getenv('DB_PORT') ?: 3306;
}

try {
    mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
    $connection = mysqli_connect($server, $login, $password, $base, (int)$port);
    $connection_error = null;
} catch (mysqli_sql_exception $e) {
    $connection = false;
    $connection_error = $e->getMessage();
}