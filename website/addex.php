<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Statsview</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
            <?php
                $server = "localhost";
                $login = "root";
                $password = "";
                $base = "stats";


                $connect = mysqli_connect($server, $login, $password, $base); //connecting to database

                //shoing a choose list of leagues
                $sql = "SELECT name FROM league";
                $result = $connect->query($sql);

                $leagueName = $_GET['league'] ?? '';

                if($result->num_rows > 0){
                    echo "<form method='GET'>";
                    echo "<select name='league' onchange='this.form.submit()'>"; // onchange give a value to varible $leagueName
                    while($row = mysqli_fetch_assoc($result)){
                        $selected = ($leagueName == $row['name']) ? "selected" : "";
                        echo "<option value='".$row['name']."'$selected>".$row['name']."</option>";
                    }
                    echo "</select>";
                    echo "</form>";
                }else{
                    echo "<h1>You don't have any teams to choose</h1>";
                }

                // taking a league id
                $queryID = "SELECT id FROM league WHERE name = ?";
                $query = $connect->prepare($queryID);
                $query->bind_param("s", $leagueName);
                $query->execute();
                $idLeagueTake = $query->get_result();

                //showing a choose list of teams
                $sqlFindTeams = "SELECT teams.name \n"

                        . "FROM teams\n"

                        . "JOIN leagues_teams ON teams.id = leagues_teams.teams_id\n"

                        . "JOIN league ON leagues_teams.leagues_id = league.id\n"

                        . "WHERE league.name = ?;";

                $query = $connect->prepare($sqlFindTeams);
                $query->bind_param("s", $leagueName);
                $query->execute();
                $result = $query->get_result();


                // choosing a first team
                $firstTeamName = $_GET['teamOne'] ?? '';

                if($result->num_rows > 0){
                    echo "<form method='GET'>";
                    echo "<select name='teamOne'>";
                    while($row = mysqli_fetch_assoc($result)){
                        $selected = ($firstTeamName == $row['name']) ? "selected" : "";
                        echo "<option value='".$row['name']."'$selected>".$row['name']."</option>";
                    }
                    echo "</select>";
                    echo "</form>";
                }else{
                    echo "<h1>You don't have any teams to choose</h1>";
                }

                // choosing a second team
                $secondTeamName = $_GET['teamTwo'] ?? '';


                $sqlFindTeams = "SELECT teams.name \n"

                        . "FROM teams\n"

                        . "JOIN leagues_teams ON teams.id = leagues_teams.teams_id\n"

                        . "JOIN league ON leagues_teams.leagues_id = league.id\n"

                        . "WHERE league.name = ?;";

                $query = $connect->prepare($sqlFindTeams);
                $query->bind_param("s", $leagueName);
                $query->execute();
                $result = $query->get_result();

                if($result->num_rows > 0){
                    echo "<form method='GET'>";
                    echo "<select name='teamTwo'>";
                    while($row = mysqli_fetch_assoc($result)){
                        $selected = ($secondTeamName == $row['name']) ? "selected" : "";
                        echo "<option value='".$row['name']."'$selected>".$row['name']."</option>";
                    }
                    echo "</select>";
                    echo "</form>";
                }

                // entering datas to the database
                // if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['save'])){
                //     $selectedLeague = $_POST['selectedLeague'] ?? '';
                //     $selectedFirstTeam = $_POST['selectedFirstTeam'] ?? '';
                //     $selectedSecondTeam = $_POST['selectedSecondTeam'] ?? '';

                //     if(!empty($selectedLeague) && !empty($selectedFirstTeam) && !empty($selectedSecondTeam)){
                //         // update league to the league tabel
                //         $sqlUpdate = "UPDATE league SET count = count + 1 WHERE name = ?";
                //         $query = $connect->prepare($sqlUpdate);
                //         $query->bind_param("s", $selectedLeague);
                //         $query->execute();

                //         // apdate teams to the teams tabel
                //         //first team
                //         $sqlUpdate = "UPDATE teams SET homeCount = homeCount + 1 WHERE name = ?";
                //         $query = $connect->prepare($sqlUpdate);
                //         $query->bind_param("s", $selectedFirstTeam);
                //         $query->execute();

                //         //second team
                //         $sqlUpdate = "UPDATE teams SET awayCount = awayCount + 1 WHERE name = ?";
                //         $query = $connect->prepare($sqlUpdate);
                //         $query->bind_param("s", $selectedSecondTeam);
                //         $query->execute();

                //         // add link between league table and teams table to the league_teams table
                //         // insert references to league_teams table
                //         $sqlInsert = "INSERT IGNORE INTO leagues_teams VALUES (?, ?)";
                //         $sqlFindLeague = "SELECT id FROM league WHERE name = ?"; // searching id from table league
                //         $sqlFindTeam = "SELECT id FROM teams WHERE name = ?"; // searching id from table teams
                
                //         // taking id from league table
                //         $query = $connect->prepare($sqlFindLeague);
                //         $query->bind_param("s", $selectedLeague);
                //         $query->execute();
                //         $result = $query->get_result();
                //         $id_league = $result->fetch_assoc()['id']; // id_league is a table assoc 

                //         // taking ID teams
                //         $teams = [$selectedFirstTeam, $selectedSecondTeam];
                //         $id_teams = [];

                //         // taking id for teams from teams table
                //         $query = $connect->prepare($sqlFindTeam);
                //         foreach ($teams as $team){
                //             $query->bind_param("s", $team);
                //             $query->execute();
                //             $result = $query->get_result();
                //             $id_teams[] = $result->fetch_assoc()['id'];
                //         }

                //         // insert teams to leagues_teams tabel
                //         $query = $connect->prepare($sqlInsert);
                //         // foreach needs a tables assoc
                //         foreach ($id_teams as $id_team){
                //             $query->bind_param("ii", $id_league, $id_team);
                //             $query->execute();
                //         }
                //     }
                // }

                // second form for save the data to database
                if(!empty($leagueName)){
                    echo "<form action='script.php' method='POST'>";
                    echo "<input type='hidden' name='league' value='$leagueName'>";
                    echo "<input type='hidden' name='team_one' value='$firstTeamName'>";
                    echo "<input type='hidden' name='team_two' value='$secondTeamName'>";
                    echo "<input type='submit' name='save' value='ADD'>";
                    echo "</form>";
                }


                //echo "<h1>Added teams {$teams[0]} and {$teams[1]} to the competition {$leagueName}</h1>";


                mysqli_close($connect);
                ?>
    </div>
</body>
</html>