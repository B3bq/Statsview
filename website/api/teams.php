<?php

class Teams
{
    private $db;

    public function __construct($conn)
    {
        $this->db = $conn;
    }

    public function showTeams()
    {
        $data = json_decode(file_get_contents("php://input"), true);
        $sport = $data['sport'] ?? null;
        $league = $data['league'] ?? null;

        if (!$sport) {
            http_response_code(400);
            echo json_encode(["error" => "Missing sport"]);
            return;
        }

        switch ($sport) {
            case "League of legends":
                $tableLeague = "lol_leagues";
                $tableTeam = "lol_teams";
                $tableBroker = "lol_broker";
                $result = $this->takeTeams($league, $tableLeague, $tableTeam, $tableBroker);
                break;
            case "Counter Strike":
                $tableLeague = "cs_leagues";
                $tableTeam = "cs_teams";
                $tableBroker = "cs_broker";
                $result = $this->takeTeams($league, $tableLeague, $tableTeam, $tableBroker);
                break;
            default:
                $tableLeague = strtolower($sport) . "_league_season";
                $tableTeam = strtolower($sport) . "_teams_season";
                $tableBroker = strtolower($sport) . "_broker_season";

                $result = $this->takeTeams($league, $tableLeague, $tableTeam, $tableBroker);
                if ($result && $result->num_rows === 0) {
                    $tableLeague = strtolower($sport) . "_league_year";
                    $tableTeam = strtolower($sport) . "_teams_year";
                    $tableBroker = strtolower($sport) . "_broker_year";
                    $result = $this->takeTeams($league, $tableLeague, $tableTeam, $tableBroker);
                }
        }

        $teamsNames = [];

        if ($result) {
            while ($row = $result->fetch_assoc()) {
                $teamsNames[] = $row['name'];
            }
        }

        echo json_encode(["status" => "ok", "data" => $teamsNames]);
    }

    private function takeTeams($league, $tableLeague, $tableTeam, $tableBroker)
    {
        try {
            $sql = "SELECT DISTINCT $tableTeam.name FROM $tableTeam JOIN  $tableBroker ON $tableTeam.id = $tableBroker.id_team JOIN $tableLeague ON $tableBroker.id_league = $tableLeague.id WHERE $tableLeague.name = '$league' ORDER BY $tableTeam.name ASC";
            $query = $this->db->prepare($sql);
            if (!$query)
                return false;
            $query->execute();
            $result = $query->get_result();
            return $result;
        } catch (\Exception $e) {
            http_response_code(500);
            echo json_encode(["status" => "error", "message" => $e->getMessage()]);
            exit;
        }
    }

    public function topTeams()
    {
        $data = json_decode(file_get_contents("php://input"), true);
        $sport = $data['sport'] ?? null;
        $userID = $data['user'] ?? null;
        $season = $data['season'] ?? null;

        if (!$sport) {
            http_response_code(400);
            echo json_encode(["error" => "Missing sport"]);
            return;
        }

        switch ($sport) {
            case "League of legends":
                $tableTeam = "lol_teams";
                break;
            case "Counter Strike":
                $tableTeam = "cs_teams";
                break;
            default:
                if ($season == 'season') {
                    $tableTeam = strtolower($sport) . "_teams_season";
                }
                else {
                    $tableTeam = strtolower($sport) . "_teams_year";
                }
        }
        $sql = "SELECT $tableTeam.name, (home_count+away_count) AS total_count, images.img FROM $tableTeam JOIN images ON $tableTeam.img = images.id WHERE id_user = ? ORDER BY total_count LIMIT 5";
        $query = $this->db->prepare($sql);
        $query->bind_param("i", $userID);
        $query->execute();
        $result = $query->get_result();

        $topTeams = [];

        while ($row = $result->fetch_assoc()) {
            $topTeams[] = $row;
        }

        echo json_encode(["status" => "ok", "data" => $topTeams]);
    }

    public function homeTeam()
    {
        $data = json_decode(file_get_contents("php://input"), true);
        $sport = $data['sport'] ?? null;
        $userID = $data['user'] ?? null;
        $season = $data['season'] ?? null;

        if (!$sport) {
            http_response_code(400);
            echo json_encode(["error" => "Missing sport"]);
            return;
        }

        switch ($sport) {
            case "League of legends":
                $tableTeam = "lol_teams";
                break;
            case "Counter Strike":
                $tableTeam = "cs_teams";
                break;
            default:
                if ($season == 'season') {
                    $tableTeam = strtolower($sport) . "_teams_season";
                }
                else {
                    $tableTeam = strtolower($sport) . "_teams_year";
                }
        }
        $sql = "SELECT $tableTeam.name, home_count, images.img FROM $tableTeam JOIN images ON $tableTeam.img = images.id WHERE id_user = ? ORDER BY home_count DESC LIMIT 1";
        $query = $this->db->prepare($sql);
        $query->bind_param("i", $userID);
        $query->execute();
        $result = $query->get_result()->fetch_assoc();

        echo json_encode(["status" => "ok", "data" => $result]);
    }

    public function awayTeam()
    {
        $data = json_decode(file_get_contents("php://input"), true);
        $sport = $data['sport'] ?? null;
        $userID = $data['user'] ?? null;
        $season = $data['season'] ?? null;

        if (!$sport) {
            http_response_code(400);
            echo json_encode(["error" => "Missing sport"]);
            return;
        }

        switch ($sport) {
            case "League of legends":
                $tableTeam = "lol_teams";
                break;
            case "Counter Strike":
                $tableTeam = "cs_teams";
                break;
            default:
                if ($season == 'season') {
                    $tableTeam = strtolower($sport) . "_teams_season";
                }
                else {
                    $tableTeam = strtolower($sport) . "_teams_year";
                }
        }
        $sql = "SELECT $tableTeam.name, away_count, images.img FROM $tableTeam JOIN images ON $tableTeam.img = images.id WHERE id_user = ? ORDER BY away_count DESC LIMIT 1";
        $query = $this->db->prepare($sql);
        $query->bind_param("i", $userID);
        $query->execute();
        $result = $query->get_result()->fetch_assoc();

        echo json_encode(["status" => "ok", "data" => $result]);
    }
}
