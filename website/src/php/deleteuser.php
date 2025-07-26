<?php
require 'connect.php';

$userID = $_COOKIE['user'];

$tables = [
    'basketball_leagues_season', 'basketball_leagues_year', 'basketball_teams_season', 'basketball_teams_year',
    'football_leagues_season', 'football_leagues_year', 'footabll_teams_season', 'footabll_teams_year',
    'cs_leagues', 'cs_teams',
    'lol_leagues', 'lol_teams',
    'users'
];

foreach ($tables as $table){
    $sql = "DELETE FROM $table WHERE id_user = $userID";
    mysqli_query($connection, $sql);
    //update broker to next id equal league or team name

}
?>