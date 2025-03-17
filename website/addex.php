<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $connect = mysqli_connect('localhost', 'root', '', 'stats');

        // checking a connection
        if ($connect->connect_error) {
            die("Błąd połączenia: " . $connect->connect_error);
        }

        $selectedLeague = $_POST['league'] ?? '';
        $selectedFirstTeam = $_POST['team_one'] ?? '';
        $selectedSecondTeam = $_POST['team_two'] ?? '';

        if(!empty($selectedLeague) && !empty($selectedFirstTeam) && !empty($selectedSecondTeam)){
                    // update league to the league tabel
                    $sqlUpdate = "UPDATE league SET count = count + 1 WHERE name = ?";
                    $query = $connect->prepare($sqlUpdate);
                    $query->bind_param("s", $selectedLeague);
                    $query->execute();

                    // apdate teams to the teams tabel
                    //first team
                    $sqlUpdate = "UPDATE teams SET homeCount = homeCount + 1 WHERE name = ?";
                    $query = $connect->prepare($sqlUpdate);
                    $query->bind_param("s", $selectedFirstTeam);
                    $query->execute();

                    //second team
                    $sqlUpdate = "UPDATE teams SET awayCount = awayCount + 1 WHERE name = ?";
                    $query = $connect->prepare($sqlUpdate);
                    $query->bind_param("s", $selectedSecondTeam);
                    $query->execute();

                    // add link between league table and teams table to the league_teams table
                    $sqlInsert = "INSERT IGNORE INTO leagues_teams VALUES (?, ?)"; // insert references to league_teams table
                    $sqlFindLeague = "SELECT id FROM league WHERE name = ?"; // searching id from table league
                    $sqlFindTeam = "SELECT id FROM teams WHERE name = ?"; // searching id from table teams
            
                    // taking id from league table
                    $query = $connect->prepare($sqlFindLeague);
                    $query->bind_param("s", $selectedLeague);
                    $query->execute();
                    $result = $query->get_result();
                    $id_league = $result->fetch_assoc()['id']; // id_league is a table assoc 

                    // taking ID teams
                    $teams = [$selectedFirstTeam, $selectedSecondTeam];
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
                }

            echo "<h1>Added teams {$teams[0]} and {$teams[1]} to the competition {$leagueName}</h1>";

    ?>
    <form method="POST">
        <select name="league">
                <?php
                    while ()
                ?>
        </select>
        <slecet name="team_one">

        </slecet>
        <slecet name="team_two">

        </slecet>
    </form>
</body>
</html>