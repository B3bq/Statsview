<?php

class Leagues{
    private $db;

    public function __construct($conn){
        $this->db = $conn;
    }

    public function showLeagues(){
        $data = json_decode(file_get_contents('php://input'), true);
        $sport  = $data['sport']  ?? null;

        if (!$sport) {
            http_response_code(400);
            echo json_encode(["error" => "Missing sport"]);
            return;
        }

        switch($sport){
            case "League of Legends":
                $tableLeague = "lol_leagues";
                $result = $this->takeLeagues($tableLeague);
                break;
            case "Counter Strike":
                $tableLeague = "cs_leagues";
                $result = $this->takeLeagues($tableLeague);
                break;
            default:
                $tableLeague = strtolower($sport)."_leagues_season";
                $result = $this->takeLeagues($tableLeague);
                
                if($result->num_rows === 0){
                    $tableLeague = strtolower($sport)."_leagues_year";
                    $result = $this->takeLeagues($tableLeague);
                }
        }

        $allLeagues = [];

        while ($row = $result->fetch_assoc()) {
            $allLeagues[] = $row['name'];
        }

        echo json_encode(["status" => "ok", "data" => $allLeagues]);
    }

    private function takeLeagues($tableLeague){
        $sql = "SELECT name FROM $tableLeague ORDER BY name ASC";
        $query = $this->db->prepare($sql);
        $query->execute();
        $result = $query->get_result();
        return $result;
    }
    
    public function topLeagues(){
        $data = json_decode(file_get_contents("php://input"), true);
        $sport = $data['sport'] ?? null;
        $userID = $data['user'] ?? null;
        $season = $data['season'] ?? null;

        if (!$sport) {
            http_response_code(400);
            echo json_encode(["error" => "Missing sport"]);
            return;
        }

        switch($sport){
            case "League of Legends":
                $tableLeague = "lol_leagues";
                break;
            case "Counter Strike":
                $tableLeague = "cs_leagues";
                break;
            default:
                if($season == "season"){
                    $tableLeague = strtolower($sport)."_leagues_season";
                }else{
                    $tableLeague = strtolower($sport)."_leagues_year";
                }
        }
        $sql = "SELECT $tableLeague.name, count, images.img FROM $tableLeague JOIN images ON $tableLeague.img = images.id WHERE id_user = ? ORDER BY count DESC LIMIT 5";
        $query = $this->db->prepare($sql);
        $query->bind_param("i", $userID);
        $query->execute();
        $result = $query->get_result();

        $topLeagues = [];

        while($row = $result->fetch_assoc()){
            $topLeagues[] = $row;
        }

        echo json_encode(["status" => "ok", "data" => $topLeagues]);
    }
}
?>