<?php
// Mock what index.php does
require 'website/src/php/connect.php';

if (!$connection) {
    echo json_encode([
        "success" => false, 
        "status" => "error", 
        "message" => "Database connection error: " . ($connection_error ?? "Unknown error")
    ]);
} else {
    echo json_encode(["success" => true, "message" => "Connected"]);
}
echo "\n";
?>
