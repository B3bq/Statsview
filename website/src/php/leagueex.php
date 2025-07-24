<?php
$server = 'localhost';
$login = 'root';
$password = '';
$base = 'statsview';

$connection = mysqli_connect($server, $login, $password, $base);

$sport = $_POST['sport'];
$season = $_POST['season'];

$tableLeague = $sport."_leagues";
$tableTeam = $sport."_teams";
$tableBroker = $sport."_broker";

if($season == 'season'){
    $tableLeague .= "_season";
    $tableTeam .= "_season";
    $tableBroker .="_season";

    $sql = "SELECT name FROM $tableLeague ORDER BY name ASC";
    $leaguesNames = mysqli_query($connection, $sql);

    if($leaguesNames->num_rows > 0){
        while($row = mysqli_fetch_assoc($leaguesNames)){
            $selectLeague .= "<option value='".$row['name']."'>".$row['name']."</option>";
        }
    }

    $data = [
        'leagues' => $selectLeague,
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
    switch($sport){
        case 'lol':
            $sql = "SELECT name FROM $tableLeague ORDER BY name ASC";
            $leaguesNames = mysqli_query($connection, $sql);

            if($leaguesNames->num_rows > 0){
                $selectLeague = "<select id='league'>";
                while($row = mysqli_fetch_assoc($leaguesNames)){
                $selectLeague .= "<option value='".$row['name']."'>".$row['name']."</option>";
                }
                $selectLeague .= "</select>";
            }

            $data = [
                'leagues' => $selectLeague,
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
        case 'cs':
            $sql = "SELECT name FROM $tableLeague ORDER BY name ASC";
            $leaguesNames = mysqli_query($connection, $sql);

            if($leaguesNames->num_rows > 0){
                $selectLeague = "<select id='league'>";
                while($row = mysqli_fetch_assoc($leaguesNames)){
                $selectLeague .= "<option value='".$row['name']."'>".$row['name']."</option>";
                }
                $selectLeague .= "</select>";
            }

            $data = [
                'leagues' => $selectLeague,
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
            $tableLeague .= "_year";
            $tableTeam .= "_year";
            $tableBroker .="_year";
            
            $sql = "SELECT name FROM $tableLeague ORDER BY name ASC";
            $leaguesNames = mysqli_query($connection, $sql);

            if($leaguesNames->num_rows > 0){
                $selectLeague = "<select id='league'>";
                while($row = mysqli_fetch_assoc($leaguesNames)){
                $selectLeague .= "<option value='".$row['name']."'>".$row['name']."</option>";
                }
                $selectLeague .= "</select>";
            }

            $data = [
                'leagues' => $selectLeague,
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