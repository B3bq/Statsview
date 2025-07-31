<?php
require 'c:/xampp/htdocs/statsview/website/src/php/connect.php'; //connection

//getting a data from user
$sport = $_POST['sport'];
$league = $_POST['league'];
$teamOne = strtolower($_POST['team_one']);
$teamTwo = strtolower($_POST['team_two']);

$userID = $_COOKIE['user']; //getting user id


switch($sport){
    case "lol":
        //checking if exist a league
        $sqlCheck = "SELECT * FROM lol_leagues WHERE name = ? AND id_user = ?"; // declerated a query
        $query = $connection->prepare($sqlCheck); // prepare to execute
        $query->bind_param("ss", $league, $userID); // insert a data
        $query->execute(); // executing
        $result = $query->get_result(); // getting a result to varible

        // LEAGUE
        if($result->num_rows > 0){ // if number of rows is bigger than 0 that league exist
            // if a league is exist then count +1
            $sqlUpdate = "UPDATE lol_leagues SET count = count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $league, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $league);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 1;
            }

            // if a league isn't exist then add the league
            $sqlInsert = "INSERT INTO lol_leagues (id, id_user, name, count, img) VALUES (NULL, $userID, '$league', 1, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        // TEAM ONE

        //checking if exist a team
        $sqlCheck = "SELECT * FROM lol_teams WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck); //preparation of the query
        $query->bind_param("ss", $teamOne, $userID); //insert varible to the query
        $query->execute(); //execute the query
        $result = $query->get_result(); //geting result of query

        if($result->num_rows > 0){
            // if a team is exist then home_count +1
            $sqlUpdate = "UPDATE lol_teams SET home_count = home_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamOne, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and home_count +1
            $sqlInsert = "INSERT INTO lol_teams (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamOne', 1, 0, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        // TEAM TWO

        //checking if exist a team
        $sqlCheck = "SELECT * FROM lol_teams WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck);
        $query->bind_param("ss", $teamTwo, $userID);
        $query->execute();
        $result = $query->get_result();

        if($result->num_rows > 0){
            // if a team is exist then away_count +1
            $sqlUpdate = "UPDATE lol_teams SET away_count = away_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamTwo, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and away_count +1
            $sqlInsert = "INSERT INTO lol_teams (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamTwo', 0, 1, $img)";
            mysqli_query($connection, $sqlInsert); //execute query
        }

        // insert references to leagues_teamas table
        $sqlInsert = "INSERT IGNORE INTO lol_broker VALUES (?, ?)";
        $sqlFindLeague = "SELECT id FROM lol_leagues WHERE name = ?"; // searching id from table league
        $sqlFindTeam = "SELECT id FROM lol_teams WHERE name = ?"; // searching id from table teams

        // taking id from league table
        $query = $connection->prepare($sqlFindLeague);
        $query->bind_param("s", $league);
        $query->execute();
        $result = $query->get_result();
        $id_league = $result->fetch_assoc()['id']; // id_league is a table assoc 

        // taking ID teams
        $teams = [$teamOne, $teamTwo];
        $id_teams = [];

        // taking id for teams from teams table
        $query = $connection->prepare($sqlFindTeam);
        foreach ($teams as $team){
            $query->bind_param("s", $team);
            $query->execute();
            $result = $query->get_result();
            $id_teams[] = $result->fetch_assoc()['id'];
        }

        // insert teams to leagues_teams tabel
        $query = $connection->prepare($sqlInsert);
        // foreach needs a tables assoc
        foreach ($id_teams as $id_team){
            $query->bind_param("ii", $id_league, $id_team);
            $query->execute();
        }
        break;
    case "cs":
        //checking if exist a league
        $sqlCheck = "SELECT * FROM cs_leagues WHERE name = ? AND id_user = ?"; // declerated a query
        $query = $connection->prepare($sqlCheck); // prepare to execute
        $query->bind_param("ss", $league, $userID); // insert a data
        $query->execute(); // executing
        $result = $query->get_result(); // getting a result to varible

        // LEAGUE
        if($result->num_rows > 0){ // if number of rows is bigger than 0 that league exist
            // if a league is exist then count +1
            $sqlUpdate = "UPDATE cs_leagues SET count = count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $league, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $league);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a league isn't exist then add the league
            $sqlInsert = "INSERT INTO cs_leagues (id, id_user, name, count, img) VALUES (NULL, $userID, '$league', 1, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        // TEAM ONE

        //checking if exist a team
        $sqlCheck = "SELECT * FROM cs_teams WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck); //preparation of the query
        $query->bind_param("ss", $teamOne, $userID); //insert varible to the query
        $query->execute(); //execute the query
        $result = $query->get_result(); //geting result of query

        if($result->num_rows > 0){
            // if a team is exist then home_count +1
            $sqlUpdate = "UPDATE cs_teams SET home_count = home_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamOne, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and home_count +1
            $sqlInsert = "INSERT INTO cs_teams (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamOne', 1, 0, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        // TEAM TWO

        //checking if exist a team
        $sqlCheck = "SELECT * FROM cs_teams WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck);
        $query->bind_param("ss", $teamTwo, $userID);
        $query->execute();
        $result = $query->get_result();

        if($result->num_rows > 0){
            // if a team is exist then away_count +1
            $sqlUpdate = "UPDATE cs_teams SET away_count = away_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamTwo, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();
            
            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and away_count +1
            $sqlInsert = "INSERT INTO cs_teams (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamTwo', 0, 1, $img)";
            mysqli_query($connection, $sqlInsert); //execute query
        }

        // insert references to leagues_teamas table
        $sqlInsert = "INSERT IGNORE INTO cs_broker VALUES (?, ?)";
        $sqlFindLeague = "SELECT id FROM cs_leagues WHERE name = ?"; // searching id from table league
        $sqlFindTeam = "SELECT id FROM cs_teams WHERE name = ?"; // searching id from table teams

        // taking id from league table
        $query = $connection->prepare($sqlFindLeague);
        $query->bind_param("s", $league);
        $query->execute();
        $result = $query->get_result();
        $id_league = $result->fetch_assoc()['id']; // id_league is a table assoc 

        // taking ID teams
        $teams = [$teamOne, $teamTwo];
        $id_teams = [];

        // taking id for teams from teams table
        $query = $connection->prepare($sqlFindTeam);
        foreach ($teams as $team){
            $query->bind_param("s", $team);
            $query->execute();
            $result = $query->get_result();
            $id_teams[] = $result->fetch_assoc()['id'];
        }

        // insert teams to leagues_teams tabel
        $query = $connection->prepare($sqlInsert);
        // foreach needs a tables assoc
        foreach ($id_teams as $id_team){
            $query->bind_param("ii", $id_league, $id_team);
            $query->execute();
        }
        break;
    default:
        //season tabels
        $tabelLeagueS = strtolower($sport).'_leagues_season';
        $tabelTeamsS = strtolower($sport).'_teams_season';
        $tabelBrokerS = strtolower($sport).'_broker_season';

        //year tabels
        $tabelLeagueY = strtolower($sport).'_leagues_year';
        $tabelTeamsY = strtolower($sport).'_teams_year';
        $tabelBrokerY = strtolower($sport).'_broker_year';

        //checking if exist a league in year
        $sqlCheck = "SELECT * FROM {$tabelLeagueY} WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck);
        $query->bind_param("ss", $league, $userID);
        $query->execute();
        $result = $query->get_result();

        if($result->num_rows > 0){
            $sqlUpdate = "UPDATE {$tabelLeagueY} SET count = count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $league, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $league);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 1;
            }

            // if a league isn't exist then add the league
            $sqlInsert = "INSERT INTO {$tabelLeagueY} (id, id_user, name, count, img) VALUES (NULL, $userID, '$league', 1, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        //checking if exist a league in season
        $sqlCheck = "SELECT * FROM {$tabelLeagueS} WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck);
        $query->bind_param("ss", $league, $userID);
        $query->execute();
        $result = $query->get_result();

        if($result->num_rows > 0){
            $sqlUpdate = "UPDATE {$tabelLeagueS} SET count = count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $league, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $league);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 1;
            }

            // if a league isn't exist then add the league
            $sqlInsert = "INSERT INTO {$tabelLeagueS} (id, id_user, name, count, img) VALUES (NULL, $userID, '$league', 1, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        // TEAM ONE

        //checking if exist a team in year
        $sqlCheck = "SELECT * FROM {$tabelTeamsY} WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck); //preparation of the query
        $query->bind_param("ss", $teamOne, $userID); //insert varible to the query
        $query->execute(); //execute the query
        $result = $query->get_result(); //geting result of query

        if($result->num_rows > 0){
            // if a team is exist then home_count +1
            $sqlUpdate = "UPDATE {$tabelTeamsY} SET home_count = home_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamOne, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and home_count +1
            $sqlInsert = "INSERT INTO {$tabelTeamsY} (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamOne', 1, 0, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        //checking if exist a team in season
        $sqlCheck = "SELECT * FROM {$tabelTeamsS} WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck); //preparation of the query
        $query->bind_param("ss", $teamOne, $userID); //insert varible to the query
        $query->execute(); //execute the query
        $result = $query->get_result(); //geting result of query

        if($result->num_rows > 0){
            // if a team is exist then home_count +1
            $sqlUpdate = "UPDATE {$tabelTeamsS} SET home_count = home_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamOne, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and home_count +1
            $sqlInsert = "INSERT INTO {$tabelTeamsS} (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamOne', 1, 0, $img)";
            mysqli_query($connection, $sqlInsert);
        }

        // TEAM TWO

        //checking if exist a team in year
        $sqlCheck = "SELECT * FROM {$tabelTeamsY} WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck);
        $query->bind_param("ss", $teamTwo, $userID);
        $query->execute();
        $result = $query->get_result();

        if($result->num_rows > 0){
            // if a team is exist then away_count +1
            $sqlUpdate = "UPDATE {$tabelTeamsY} SET away_count = away_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamTwo, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and away_count +1
            $sqlInsert = "INSERT INTO {$tabelTeamsY} (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamTwo', 0, 1, $img)";
            mysqli_query($connection, $sqlInsert); //execute query
        }

        //checking if exist a team in season
        $sqlCheck = "SELECT * FROM {$tabelTeamsS} WHERE name = ? AND id_user = ?";
        $query = $connection->prepare($sqlCheck);
        $query->bind_param("ss", $teamTwo, $userID);
        $query->execute();
        $result = $query->get_result();

        if($result->num_rows > 0){
            // if a team is exist then away_count +1
            $sqlUpdate = "UPDATE {$tabelTeamsS} SET away_count = away_count + 1 WHERE name = ? AND id_user = ?";
            $query = $connection->prepare($sqlUpdate);
            $query->bind_param("ss", $teamTwo, $userID);
            $query->execute();
        }else{
            $sqlImgSearch = "SELECT id FROM images WHERE name = ?";
            $query = $connection->prepare($sqlImgSearch);
            $query->bind_param("s", $teamOne);
            $query->execute();
            $result = $query->get_result();

            if($result->num_rows > 0){
                $img = $result->fetch_assoc()['id'];
            }else{
                $img = 2;
            }

            // if a team isn't exist then add the team and away_count +1
            $sqlInsert = "INSERT INTO {$tabelTeamsS} (id, id_user, name, home_count, away_count, img) VALUES (NULL, $userID, '$teamTwo', 0, 1, $img)";
            mysqli_query($connection, $sqlInsert); //execute query
        }

        //BROKER YEAR

        // insert references to leagues_teamas table
        $sqlInsert = "INSERT IGNORE INTO {$tabelBrokerY} VALUES (?, ?)";
        $sqlFindLeague = "SELECT id FROM {$tabelLeagueY} WHERE name = ?"; // searching id from table league
        $sqlFindTeam = "SELECT id FROM {$tabelTeamsY} WHERE name = ?"; // searching id from table teams

        // taking id from league table
        $query = $connection->prepare($sqlFindLeague);
        $query->bind_param("s", $league);
        $query->execute();
        $result = $query->get_result();
        $id_league = $result->fetch_assoc()['id']; // id_league is a table assoc 

        // taking ID teams
        $teams = [$teamOne, $teamTwo];
        $id_teams = [];

        // taking id for teams from teams table
        $query = $connection->prepare($sqlFindTeam);
        foreach ($teams as $team){
            $query->bind_param("s", $team);
            $query->execute();
            $result = $query->get_result();
            $id_teams[] = $result->fetch_assoc()['id'];
        }

        // insert teams to leagues_teams tabel
        $query = $connection->prepare($sqlInsert);
        // foreach needs a tables assoc
        foreach ($id_teams as $id_team){
            $query->bind_param("ii", $id_league, $id_team);
            $query->execute();
        }

        //BROKER SEASON

        // insert references to leagues_teamas table
        $sqlInsert = "INSERT IGNORE INTO {$tabelBrokerS} VALUES (?, ?)";
        $sqlFindLeague = "SELECT id FROM {$tabelLeagueS} WHERE name = ?"; // searching id from table league
        $sqlFindTeam = "SELECT id FROM {$tabelTeamsS} WHERE name = ?"; // searching id from table teams

        // taking id from league table
        $query = $connection->prepare($sqlFindLeague);
        $query->bind_param("s", $league);
        $query->execute();
        $result = $query->get_result();
        $id_league = $result->fetch_assoc()['id']; // id_league is a table assoc 

        // taking ID teams
        $teams = [$teamOne, $teamTwo];
        $id_teams = [];

        // taking id for teams from teams table
        $query = $connection->prepare($sqlFindTeam);
        foreach ($teams as $team){
            $query->bind_param("s", $team);
            $query->execute();
            $result = $query->get_result();
            $id_teams[] = $result->fetch_assoc()['id'];
        }

        // insert teams to leagues_teams tabel
        $query = $connection->prepare($sqlInsert);
        // foreach needs a tables assoc
        foreach ($id_teams as $id_team){
            $query->bind_param("ii", $id_league, $id_team);
            $query->execute();
        }
        break;
}
mysqli_close($connection);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statsview</title>
    <link rel="stylesheet" href="src/sass/style.css">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

    <script type="module" src="src/js/script.js" defer></script>
    <script src="src/js/functions.js"></script>
</head>
<body>
    <header>
        <!--logo-->
        <a href="index.html" title="Back to home page">
            <img src="src/img/logo.svg" alt="logo" width="64px" height="64px">
        </a>
        <nav>
            <button id="js-toggle-menu">
                <img width="46" height="46" src="src/img/burger-bar.png" alt="Toggle menu" id="menu">
            </button>

            <ul id="js-toggleable-menu">
                <li><a href="" title="" id="option1"></a></li>
                <li><a href="index.html#about" title="About the project" id="option2">About</a></li>
                <li><a href="download.html" title="">Dowland app</a></li>
                <li><a href="login.html" title="Log in site" id="logout">Log in</a></li>
            </ul>
        </nav>
    </header>
    <main class="added">
        <h1>Added teams <span><?php echo $teamOne;?></span> and <span><?php echo $teamTwo;?></span> to the competition <span><?php echo $league;?></span></h1>
        <button onclick="goBack()">Go Back</button>
    </main>
    <footer>
        <a href="https://github.com/B3bq" target="_blank" >
            <img src="src/img/github-brands.svg" alt="github">
        </a>
        <a href="mailto:" title="E-mail">mail</a>

        <p>© 2025 studio</p>
    </footer>
</body>
</html>