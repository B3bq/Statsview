<?php
$server = 'localhost';
$login = 'root';
$pass = '';
$base = 'statsview';
$conn = mysqli_connect($server, $login, $pass, $base); //connect to the databa
$conn->set_charset("utf8mb4"); //coding utf

//getting varibles
$userID = $_COOKIE['user'];
$season = $_POST['season'];
$sport = $_POST['sport'];

if($season == 'season'){
    $tableLeague = $sport."_leagues_".$season;
    $tableTeams = $sport."_teams_".$season;
    //overall matches
    $sql = "SELECT SUM(count) FROM $tableLeague WHERE id_user = ?";
    $query = $conn->prepare($sql);
    $query->bind_param("s", $userID);
    $query->execute();
    $result = $query->get_result();
    $ovrCount = $result->fetch_assoc()['SUM(count)'];

    $gamesText = "<h1>You watched $ovrCount games!</h1>"; //info to website

    //top 5 leagues
    $sql = "SELECT $tableLeague.name, count, images.img FROM $tableLeague JOIN images ON $tableLeague.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
    $topLeagus = mysqli_query($conn, $sql);

    //table 
    $leagueTable = "<table class='topLeagues'>";
    $leagueTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

    $n = 1;

    while($row=mysqli_fetch_assoc($topLeagus)){
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mimeType = $finfo->buffer($row['img']); //taikng file type
        $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']); //code this to base64
        $leagueTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['count']."</td></tr>";
        $n++;
    }
    $leagueTable .= "</table>";

    //top 5 teams
    $sql = "SELECT $tableTeams.name, (home_count + away_count) AS total_count, images.img FROM $tableTeams JOIN images ON $tableTeams.img = images.id WHERE id_user = $userID ORDER BY total_count DESC LIMIT 5";
    $topTeams = mysqli_query($conn, $sql);

    //tabel
    $teamTable = "<table class='topTeams'>";
    $teamTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

    $n = 1;

    while($row=mysqli_fetch_assoc($topTeams)){
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mimeType = $finfo->buffer($row['img']);
        $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']);
        $teamTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['total_count']."</td></tr>";
        $n++;
    }
    $teamTable .= "</table>";

    //top home team
    $sql = "SELECT $tableTeams.name, home_count, images.img FROM $tableTeams JOIN images ON $tableTeams.img = images.id WHERE id_user = $userID ORDER BY home_count DESC LIMIT 1";
    $result = mysqli_query($conn, $sql);
    $topHome = mysqli_fetch_assoc($result);

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->buffer($topHome['img']); //taikng file type
    $base64 = 'data:'.$mimeType.';base64,'.base64_encode($topHome['img']); //code this to base64

    $homeFav = "<div class='fav'><h2>Home favourite</h2><img src='$base64'><h3>".$topHome['name']." (".$topHome['home_count']." matches)</h3></div>";

    //top away team
    $sql = "SELECT $tableTeams.name, away_count, images.img FROM $tableTeams JOIN images ON $tableTeams.img = images.id WHERE id_user = $userID ORDER BY away_count DESC LIMIT 1";
    $result = mysqli_query($conn, $sql);
    $topAway = mysqli_fetch_assoc($result);

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mimeType = $finfo->buffer($topAway['img']); //taikng file type
    $base64 = 'data:'.$mimeType.';base64,'.base64_encode($topAway['img']); //code this to base64

    $awayFav = "<div class='fav'><h2>You traveled with them most often</h2><img src='$base64'><h3>".$topAway['name']." (".$topAway['away_count']." matches)</h3></div>";

    //pack datas for json
    $data = [
        'summary' => $gamesText,
        'home' => $homeFav,
        'away' => $awayFav,
        'leagues' => $leagueTable,
        'teams' => $teamTable,
    ];

    //function to standardized coding
    function utf8ize($data) {
        if (is_array($data)) {
            foreach ($data as $key => $value) {
                $data[$key] = utf8ize($value);
            }
        } elseif (is_string($data)) {
            return mb_convert_encoding($data, "UTF-8", "auto");
        }
        return $data;
    }
    
    $data = utf8ize($data);

    header('Content-Type: application/json'); //answer type
    $json =  json_encode($data);
    if($json === false){ //checking
        echo json_last_error_msg();
    }else{
        echo $json;
    }
}else{
    switch ($sport){
        case "lol":
            //overall matches
            $sql = "SELECT SUM(count) FROM lol_leagues WHERE id_user = ?";
            $query = $conn->prepare($sql);
            $query->bind_param("s", $userID);
            $query->execute();
            $result = $query->get_result();
            $ovrCount = $result->fetch_assoc()['SUM(count)'];

            $gamesText = "<h1>You watched $ovrCount games!</h1>"; //info to website
        
            //top 5 leagues
            $sql = "SELECT lol_leagues.name, count, images.img FROM lol_leagues JOIN images ON lol_leagues.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topLeagus = mysqli_query($conn, $sql);

            //table 
            $leagueTable = "<table class='topLeagues'>";
            $leagueTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

            $n = 1;

            while($row=mysqli_fetch_assoc($topLeagus)){
                $finfo = new finfo(FILEINFO_MIME_TYPE);
                $mimeType = $finfo->buffer($row['img']); //taikng file type
                $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']); //code this to base64
                $leagueTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['count']."</td></tr>";
                $n++;
            }
            $leagueTable .= "</table>";
        
            //top 5 teams
            $sql = "SELECT lol_teams.name, (home_count + away_count) AS total_count, images.img FROM lol_teams JOIN images ON lol_teams.img = images.id WHERE id_user = $userID ORDER BY total_count DESC LIMIT 5";
            $topTeams = mysqli_query($conn, $sql);

            //tabel
            $teamTable = "<table class='topTeams'>";
            $teamTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

            $n = 1;

            while($row=mysqli_fetch_assoc($topTeams)){
                $finfo = new finfo(FILEINFO_MIME_TYPE);
                $mimeType = $finfo->buffer($row['img']);
                $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']);
                $teamTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['total_count']."</td></tr>";
                $n++;
            }
            $teamTable .= "</table>";
        
            //pack datas for json
            $data = [
                'summary' => $gamesText,
                'leagues' => $leagueTable,
                'teams' => $teamTable,
            ];

            //function to standardized coding
            function utf8ize($data) {
                if (is_array($data)) {
                    foreach ($data as $key => $value) {
                        $data[$key] = utf8ize($value);
                    }
                } elseif (is_string($data)) {
                    return mb_convert_encoding($data, "UTF-8", "auto");
                }
                return $data;
            }
            
            $data = utf8ize($data);

            header('Content-Type: application/json'); //answer type
            $json =  json_encode($data);
            if($json === false){ //checking
                echo json_last_error_msg();
            }else{
                echo $json;
            }

            break;
        case "cs":
            //overall matches
            $sql = "SELECT SUM(count) FROM cs_leagues WHERE id_user = ?";
            $query = $conn->prepare($sql);
            $query->bind_param("s", $userID);
            $query->execute();
            $result = $query->get_result();
            $ovrCount = $result->fetch_assoc()['SUM(count)'];

            $gamesText = "<h1>You watched $ovrCount games!</h1>"; //info to website
        
            //top 5 leagues
            $sql = "SELECT cs_leagues.name, count, images.img FROM cs_leagues JOIN images ON cs_leagues.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topLeagus = mysqli_query($conn, $sql);

            //table
            $leagueTable = "<table class='topLeagues'>";
            $leagueTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

            $n = 1;

            while($row=mysqli_fetch_assoc($topLeagus)){
                $finfo = new finfo(FILEINFO_MIME_TYPE);
                $mimeType = $finfo->buffer($row['img']); //taikng file type
                $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']); //code this to base64
                $leagueTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['count']."</td></tr>";
                $n++;
            }
            $leagueTable .= "</table>";
        
            //top 5 teams
            $sql = "SELECT cs_teams.name, (home_count + away_count) AS total_count, images.img FROM cs_teams JOIN images ON cs_teams.img = images.id WHERE id_user = $userID ORDER BY total_count DESC LIMIT 5";
            $topTeams = mysqli_query($conn, $sql);

            //tabel
            $teamTable = "<table class='topTeams'>";
            $teamTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";
 
            $n = 1;
 
            while($row=mysqli_fetch_assoc($topTeams)){
                $finfo = new finfo(FILEINFO_MIME_TYPE);
                $mimeType = $finfo->buffer($row['img']);
                $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']);
                $teamTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['total_count']."</td></tr>";
                $n++;
            }
            $teamTable .= "</table>";
         
            //pack datas for json
            $data = [
                'summary' => $gamesText,
                'leagues' => $leagueTable,
                'teams' => $teamTable,
            ];
 
             //function to standardized coding
             function utf8ize($data) {
                if (is_array($data)) {
                    foreach ($data as $key => $value) {
                        $data[$key] = utf8ize($value);
                    }
                } elseif (is_string($data)) {
                    return mb_convert_encoding($data, "UTF-8", "auto");
                }
                return $data;
             }
             
            $data = utf8ize($data);
 
            header('Content-Type: application/json'); //answer type
            $json =  json_encode($data);
            if($json === false){ //checking
                echo json_last_error_msg();
            }else{
                echo $json;
            }
        
            break;
        default:
            $tableLeague = $sport."_leagues_".$season;
            $tableTeams = $sport."_teams_".$season;
            //overall matches
            $sql = "SELECT SUM(count) FROM $tableLeague WHERE id_user = ?";
            $query = $conn->prepare($sql);
            $query->bind_param("s", $userID);
            $query->execute();
            $result = $query->get_result();
            $ovrCount = $result->fetch_assoc()['SUM(count)'];

            $gamesText = "<h1>You watched $ovrCount games!</h1>"; //info to website
        
            //top 5 leagues
            $sql = "SELECT $tableLeague.name, count, images.img FROM $tableLeague JOIN images ON $tableLeague.img = images.id WHERE id_user = $userID ORDER BY count DESC LIMIT 5";
            $topLeagus = mysqli_query($conn, $sql);
        
            //table 
            $leagueTable = "<table class='topLeagues'>";
            $leagueTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

            $n = 1;

            while($row=mysqli_fetch_assoc($topLeagus)){
                $finfo = new finfo(FILEINFO_MIME_TYPE);
                $mimeType = $finfo->buffer($row['img']); //taikng file type
                $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']); //code this to base64
                $leagueTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['count']."</td></tr>";
                $n++;
            }
            $leagueTable .= "</table>";

            //top 5 teams
            $sql = "SELECT $tableTeams.name, (home_count + away_count) AS total_count, images.img FROM $tableTeams JOIN images ON $tableTeams.img = images.id WHERE id_user = $userID ORDER BY total_count DESC LIMIT 5";
            $topTeams = mysqli_query($conn, $sql);

            //tabel
            $teamTable = "<table class='topTeams'>";
            $teamTable .= "<tr><th>on.</th><th colspan='2'>Name</th><th>Matches</th></tr>";

            $n = 1;

            while($row=mysqli_fetch_assoc($topTeams)){
                $finfo = new finfo(FILEINFO_MIME_TYPE);
                $mimeType = $finfo->buffer($row['img']);
                $base64 = 'data:'.$mimeType.';base64,'.base64_encode($row['img']);
                $teamTable .= "<tr><td>".$n."</td><td>".$row['name']."</td><td><img src='".$base64."'></td><td>".$row['total_count']."</td></tr>";
                $n++;
            }
            $teamTable .= "</table>";

            //top home team
            $sql = "SELECT $tableTeams.name, home_count, images.img FROM $tableTeams JOIN images ON $tableTeams.img = images.id WHERE id_user = $userID ORDER BY home_count DESC LIMIT 1";
            $result = mysqli_query($conn, $sql);
            $topHome = mysqli_fetch_assoc($result);

            $finfo = new finfo(FILEINFO_MIME_TYPE);
            $mimeType = $finfo->buffer($topHome['img']); //taikng file type
            $base64 = 'data:'.$mimeType.';base64,'.base64_encode($topHome['img']); //code this to base64

            $homeFav = "<div class='fav'><h2>Home favourite</h2><img src='$base64'><h3>".$topHome['name']." (".$topHome['home_count']." matches)</h3></div>";
        
            //top away team
            $sql = "SELECT $tableTeams.name, away_count, images.img FROM $tableTeams JOIN images ON $tableTeams.img = images.id WHERE id_user = $userID ORDER BY away_count DESC LIMIT 1";
            $result = mysqli_query($conn, $sql);
            $topAway = mysqli_fetch_assoc($result);
        
            $finfo = new finfo(FILEINFO_MIME_TYPE);
            $mimeType = $finfo->buffer($topAway['img']); //taikng file type
            $base64 = 'data:'.$mimeType.';base64,'.base64_encode($topAway['img']); //code this to base64

            $awayFav = "<div class='fav'><h2>You traveled with them most often</h2><img src='$base64'><h3>".$topAway['name']." (".$topAway['away_count']." matches)</h3></div>";

            //pack datas for json
            $data = [
                'summary' => $gamesText,
                'home' => $homeFav,
                'away' => $awayFav,
                'leagues' => $leagueTable,
                'teams' => $teamTable,
            ];

            //function to standardized coding
            function utf8ize($data) {
                if (is_array($data)) {
                    foreach ($data as $key => $value) {
                        $data[$key] = utf8ize($value);
                    }
                } elseif (is_string($data)) {
                    return mb_convert_encoding($data, "UTF-8", "auto");
                }
                return $data;
            }
            
            $data = utf8ize($data);

            header('Content-Type: application/json'); //answer type
            $json =  json_encode($data);
            if($json === false){ //checking
                echo json_last_error_msg();
            }else{
                echo $json;
            }

            break;
    }
}
?>