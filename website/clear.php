<?php
require "src/php/connect.php";

$date = date("m.d");

$tablesYear = [
    'basketball_broker_year', 'basketball_leagues_year', 'basketball_teams_year',
    'football_broker_year', 'football_leagues_year', 'football_teams_year',
    'handball_broker_year', 'handball_leagues_year', 'handball_teams_year',
    'volleyball_broker_year', 'volleyball_leagues_year', 'volleyball_teams_year',
    'cs_broker', 'cs_leagues', 'cs_teams',
    'lol_broker', 'lol_leagues', 'lol_teams'
];

$tablesSeason = [
    'basketball_broker_season', 'basketball_leagues_season', 'basketball_teams_season',
    'football_broker_season', 'football_leagues_season', 'football_teams_season',
    'handball_broker_season', 'handball_leagues_season', 'handball_teams_season',
    'volleyball_broker_season', 'volleyball_leagues_season', 'volleyball_teams_season'
];

if ($date == '07.19'){
    foreach ($tablesSeason as $table) {
        $sql = "DELETE FROM {$table}";
        mysqli_query($connection, $sql);
    }
}elseif ($date == "02.14"){
    foreach ($tablesYear as $table) {
        $sql = "DELETE FROM {$table}";
        mysqli_query($connection, $sql);
    }
}

?>