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

        //showing a choose list of leagues
        $sql = "SELECT name FROM league";
        $result = $connect->query($sql);

        //showing a choose list of teams
        $sqlFindTeams = "SELECT teams.name \n"

        . "FROM teams\n"

        . "JOIN leagues_teams ON teams.id = leagues_teams.teams_id\n"

        . "JOIN league ON leagues_teams.leagues_id = league.id\n"

        . "WHERE league.name = ?;";

        $query = $connect->prepare($sqlFindTeams);
        $query->bind_param("s", $leagueName);
        $query->execute();
        $resultTeam = $query->get_result();

    ?>
    <form method="POST">
        <select name="league">
        <?php while ($row = $result->fetch_assoc()): ?>
            <option value="<?= $row['id']; ?>" <?= ($selectedLeague == $row['name']) ? 'selected' : ''; ?>>
                <?= $row['name']; ?>
            </option>
        <?php endwhile; ?>\
        </select>
        <slecet name="team_one">
            <?php while($row = $resultTeam->fetch_assoc()):?>
                <option value="<?php $row['id']; ?>" <?php ($selectedFirstTeam == $row['id']) ? 'selected' : '';?>>
                    <?php $row['name']?>
                </option>
        </slecet>
        <slecet name="team_two">

        </slecet>
    </form>
</body>
</html>