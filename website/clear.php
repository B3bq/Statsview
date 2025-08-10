<?php
require "src/php/connect.php";

$date = date("m.d");

$tablesYear = [
    'basketball_leagues_year', 'basketball_teams_year',
    'football_leagues_year', 'football_teams_year',
    'cs_leagues', 'cs_teams',
    'lol_leagues', 'lol_teams'
];

$tablesSeason = [
    'basketball_leagues_season', 'basketball_teams_season',
    'football_leagues_season', 'football_teams_season'
];

if ($date == '07.19'){
    foreach ($tablesSeason as $table) {
        $sql = "DELETE FROM {$table}";
        mysqli_query($connection, $sql);
    }
}elseif ($date == "01.05"){
    foreach ($tablesYear as $table) {
        $sql = "DELETE FROM {$table}";
        mysqli_query($connection, $sql);
    }
}

?>