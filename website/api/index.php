<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

// Pobieranie globalnego połączenia do bazy (z pliku website na Dockerze)
require_once '../src/php/connect.php';

$action = $_GET['action'] ?? '';

if ($action === 'system.ping') {
    echo json_encode(["message" => "Statsview API is running"]);
    exit;
}

// Router dla Auth (auth.php -> klasa User)
if (strpos($action, 'Auth.') === 0) {
    require_once 'auth.php';
    $user = new User($connection);
    
    if ($action === 'Auth.userName') $user->userName();
    elseif ($action === 'Auth.userChecking') $user->userChecking();
    elseif ($action === 'Auth.userAdd') $user->userAdd();
    exit;
}

// Router dla Insert (insert.php -> klasa Insert)
if (strpos($action, 'Insert.') === 0) {
    require_once 'insert.php';
    $insert = new Insert($connection);
    
    if ($action === 'Insert.insertData') $insert->insertData();
    exit;
}

// Router dla Leagues (leagues.php -> klasa Leagues)
if (strpos($action, 'Leagues.') === 0) {
    require_once 'leagues.php';
    $leagues = new Leagues($connection);
    
    if ($action === 'Leagues.showLeagues') $leagues->showLeagues();
    elseif ($action === 'Leagues.topLeagues') $leagues->topLeagues();
    exit;
}

// Router dla Teams (teams.php -> klasa Teams)
if (strpos($action, 'Teams.') === 0) {
    require_once 'teams.php';
    $teams = new Teams($connection);
    
    if ($action === 'Teams.showTeams') $teams->showTeams();
    elseif ($action === 'Teams.topTeams') $teams->topTeams();
    elseif ($action === 'Teams.homeTeam') $teams->homeTeam();
    elseif ($action === 'Teams.awayTeam') $teams->awayTeam();
    exit;
}

echo json_encode(["success" => false, "text" => "Endpoint not found"]);
?>
