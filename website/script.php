<?php
$server = "localhost";
$login = "root";
$password = "";
$base = "stats";

$connect = mysqli_connect($server, $login, $password, $base); //connecting to database

//getting a data from user
$league = $_POST['league'];
$teamOne = $_POST['team_one'];
$teamTwo = $_POST['team_two'];

//checking if exist a league
$sqlCheck = "SELECT * FROM league WHERE name = ?"; // declerated a query
$query = $connect->prepare($sqlCheck); // prepare to execute
$query->bind_param("s", $league); // insert a data
$query->execute(); // executing
$result = $query->get_result(); // getting a result to varible

// LEAGUE
if($result->num_rows > 0){ // if number of rows is bigger than 0 that league exist
    // if a league is exist then count +1
    $sqlUpdate = "UPDATE league SET count = count + 1 WHERE name = ?";
    $query = $connect->prepare($sqlUpdate);
    $query->bind_param("s", $league);
    $query->execute();
}else{
    // if a league isn't exist then add the league
    $sqlInsert = "INSERT INTO league VALUES (' ', '$league', 1, ' ')";
    mysqli_query($connect, $sqlInsert);
}

// TEAM ONE

//checking if exist a team
$sqlCheck = "SELECT * FROM teams WHERE name = ?";
$query = $connect->prepare($sqlCheck); //preparation of the query
$query->bind_param("s", $teamOne); //insert varible to the query
$query->execute(); //execute the query
$result = $query->get_result(); //geting result of query

if($result->num_rows > 0){
    // if a team is exist then homeCount +1
    $sqlUpdate = "UPDATE teams SET homeCount = homeCount + 1 WHERE name = ?";
    $query = $connect->prepare($sqlUpdate);
    $query->bind_param("s", $teamOne);
    $query->execute();
}else{
    // if a team isn't exist then add the team and homeCount +1
    $sqlInsert = "INSERT INTO teams VALUES (' ', '$teamOne', 1, 0, ' ')";
    mysqli_query($connect, $sqlInsert);
}

// TEAM TWO

//checking if exist a team
$sqlCheck = "SELECT * FROM teams WHERE name = ?";
$query = $connect->prepare($sqlCheck);
$query->bind_param("s", $teamTwo);
$query->execute();
$result = $query->get_result();

if($result->num_rows > 0){
    // if a team is exist then awayCount +1
    $sqlUpdate = "UPDATE teams SET awayCount = awayCount + 1 WHERE name = ?";
    $query = $connect->prepare($sqlUpdate);
    $query->bind_param("s", $teamTwo);
    $query->execute();
}else{
    // if a team isn't exist then add the team and awayCount +1
    $sqlInsert = "INSERT INTO teams VALUES (' ', '$teamTwo', 0, 1, ' ')";
    mysqli_query($connect, $sqlInsert); //execute query
}

// insert references to leagues_teamas table
$sqlInsert = "INSERT IGNORE INTO leagues_teams VALUES (?, ?)";
$sqlFindLeague = "SELECT id FROM league WHERE name = ?"; // searching id from table league
$sqlFindTeam = "SELECT id FROM teams WHERE name = ?"; // searching id from table teams

// taking id from league table
$query = $connect->prepare($sqlFindLeague);
$query->bind_param("s", $league);
$query->execute();
$result = $query->get_result();
$id_league = $result->fetch_assoc()['id']; // id_league is a table assoc 

// taking ID teams
$teams = [$teamOne, $teamTwo];
$id_teams = [];

// taking id for teams from teams table
$query = $connect->prepare($sqlFindTeam);
foreach ($teams as $team){
    $query->bind_param("s", $team);
    $query->execute();
    $result = $query->get_result();
    $id_teams[] = $result->fetch_assoc()['id'];
}

// insert teams to leagues_teams tabel
$query = $connect->prepare($sqlInsert);
// foreach needs a tables assoc
foreach ($id_teams as $id_team){
    $query->bind_param("ii", $id_league, $id_team);
    $query->execute();
}

echo "<h1>Added teams {$teams[0]} and {$teams[1]} to the competition {$league}</h1>";

mysqli_close($connect);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statsview</title>
    <link rel="stylesheet" href="src/sass/style.css">
</head>
<body>
    <div class="container">
        <a href="index.html"><button>Go back</button></a>
    </div>
</body>
</html>