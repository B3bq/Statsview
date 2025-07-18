<?php
    $server = 'localhost';
    $login = 'root';
    $pass = '';
    $base = 'statsview';
    $conn = mysqli_connect($server, $login, $pass, $base); //connect to the databa
    $userID = $_COOKIE['user'];
    $season = $_POST['season'];
    $sport = $_POST['sport'];

    switch ($sport){
        case "lol":
            //overall matches
            $sql = "SELECT SUM(count) FROM lol_leagues WHERE id_user = ?";
            $query = $conn->prepare($sql);
            $query->bind_param("s", $userID);
            $query->execute();
            $result = $query->get_result();
            $ovrCount = $result->fetch_assoc()['SUM(count)'];

            $gamesText = "<h1>You watched $ovrCount games!</h1>";
        
            //top 5 leagues
            $sql = "SELECT lol_leagues.name, count, images.img FROM lol_leagues JOIN images ON lol_leagues.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topLeagus = mysqli_query($conn, $sql);

            $leagueTable = "<table class='topLeagues'>";
            $leagueTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

            $n = 1;

            while($row=mysqli_fetch_assoc($topLeagus)){
                $leagueTable .= "<tr><td>".$n."</td><td><img src='".$row['name']."'></td><td>".$row['img']."</td><td>".$row['count']."</td></tr>";
                $n++;
            }
            $leagueTable .= "</table>";
        
            //top 5 teams
            $sql = "SELECT lol_teams.name, (home_count + away_count) AS total_count, images.img FROM lol_teams JOIN images ON lol_teams.img = images.id WHERE id_user = $userID ORDER BY total_count DESC LIMIT 5";
            $topTeams = mysqli_query($conn, $sql);

            $teamTable = "<table class='topTeams'>";
            $teamTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

            $n = 1;

            while($row=mysqli_fetch_assoc($topTeams)){
                $teamTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$row['name']."'></td><td>".$row['total_count']."</td></tr>";
                $n++;
            }
            $teamTable .= "</table>";
        
            $data = [
                'summary' => $gamesText,
                'leagues' => $leagueTable,
                'teams' => $teamTable,
            ];

            echo json_encode($data);

            break;
        case "cs":
            //overall matches
            $sql = "SELECT SUM(count) FROM cs_leagues WHERE id_user = ?";
            $query = $conn->prepare($sql);
            $query->bind_param("s", $userID);
            $query->excute();
            $result = $query->get_result();
            $ovrCount = $result->fetch_assoc()['sum(count)'];
        
            //top 5 leagues
            $sql = "SELECT cs_leagues.name, count, images.img FROM cs_leagues JOIN images ON cs_leagues.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topLeagus = mysqli_query($conn, $sql);
        
            //top 5 teams
            $sql = "SELECT cs_teams.name, (home_count + away_count) AS total_count, images.img FROM cs_teams JOIN images ON cs_teams.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topTeams = mysqli_query($conn, $sql);
        
            break;
        default:
            $tableLeague = $sport."_leagues_".$season;
            $tableTeams = $sport."_teams_".$season;
            //overall matches
            $sql = "SELECT SUM(count) FROM $tabelLeague WHERE id_user = ?";
            $query = $conn->prepare($sql);
            $query->bind_param("s", $userID);
            $query->excute();
            $result = $query->get_result();
            $ovrCount = $result->fetch_assoc()['sum(count)'];
        
            //top 5 leagues
            $sql = "SELECT $tabelLeague.name, count, images.img FROM $tabelLeague JOIN images ON $tabelLeague.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topLeagus = mysqli_query($conn, $sql);
        
            //top 5 teams
            $sql = "SELECT $tabelTeams.name, (home_count + away_count) AS total_count, images.img FROM $tabelTeams JOIN images ON $tabelTeams.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topTeams = mysqli_query($conn, $sql);
            //top home team
            $sql = "SELECT $tabelTeams.name, home_count, images.img FROM $tabelTeams JOIN ON $tabelTeams.img = images.id WHERE id_user = $userID ORDER BY home_count DESC LIMIT 1";
            $result = mysqli_query($conn, $sql);
            $topHome = mysqli_fetch_assoc($result);
        
            //top away team
            $sql = "SELECT $tabelTeams.name, away_count, images.img FROM $tabelTeams JOIN ON $tabelTeams.img = images.id WHERE id_user = $userID ORDER BY home_count DESC LIMIT 1";
            $result = mysqli_query($conn, $sql);
            $topAway = mysqli_fetch_assoc($result);
        
            break;
    }
?>