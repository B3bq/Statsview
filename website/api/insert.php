<?php

class Insert
{
    private $db;

    public function __construct($conn)
    {
        $this->db = $conn;
    }

    public function insertData()
    {
        $data = json_decode(file_get_contents("php://input"), true);
        $sport = $data['sport'];
        $league = $data['league'];
        $firstTeam = $data['first'];
        $secondTeam = $data['second'];
        $userID = $data['user'];

        if (!$sport || !$league || !$firstTeam || !$secondTeam || !$userID) {
            http_response_code(400);
            echo json_encode(["error" => "Invalid data"]);
            exit;
        }

        switch ($sport) {
            case "League of Legends":
                $tabelLeagues = "lol_leagues";
                $tabelTeams = "lol_teams";
                $tabelBroker = "lol_broker";

                $this->addData($league, $firstTeam, $secondTeam, $userID, $tabelLeagues, $tabelTeams, $tabelBroker);
                break;
            case "Counter Strike":
                $tabelLeagues = "cs_leagues";
                $tabelTeams = "cs_teams";
                $tabelBroker = "cs_broker";

                $this->addData($league, $firstTeam, $secondTeam, $userID, $tabelLeagues, $tabelTeams, $tabelBroker);
                break;
            default:
                $seasonLeague = strtolower($sport) . "_leagues_season";
                $seasonTeam = strtolower($sport) . "_teams_season";
                $seasonBroker = strtolower($sport) . "_broker_season";

                $yearLeague = strtolower($sport) . "_leagues_year";
                $yearTeam = strtolower($sport) . "_teams_year";
                $yearBroker = strtolower($sport) . "_broker_year";

                $this->addData($league, $firstTeam, $secondTeam, $userID, $seasonLeague, $seasonTeam, $seasonBroker);
                $this->addData($league, $firstTeam, $secondTeam, $userID, $yearLeague, $yearTeam, $yearBroker);
        }
    }

    private function addData(string $league, string $firstTeam, string $secondTeam, string $userID, string $tabelLeagues, string $tabelTeams, string $tabelBroker)
    {
        $this->db->begin_transaction();
        $sqlLeagueCheck = "SELECT * FROM $tabelLeagues WHERE name = ? AND id_user = ?";
        $sqlLeagueCheck = $this->db->prepare($sqlLeagueCheck);
        $sqlLeagueCheck->bind_param("ss", $league, $userID);
        $sqlLeagueCheck->execute();
        $result = $sqlLeagueCheck->get_result();

        if ($result->num_rows > 0) {
            $sqlUpdateLeague = "UPDATE $tabelLeagues SET count = count + 1 WHERE name = ? AND id_user = ?";
            $query = $this->db->prepare($sqlUpdateLeague);
            $query->bind_param("ss", $league, $userID);
            $query->execute();
        }
        else {
            $img = $this->imgSearch($league, "league");

            $sqlInsertLeague = "INSERT INTO $tabelLeagues (id, id_user, name, count, img) VALUES (NULL, ?, ?, 1, ?)";
            $query = $this->db->prepare($sqlInsertLeague);
            $query->bind_param("isi", $userID, $league, $img);
            $query->execute();
        }

        $sqlFirstTeamCheck = "SELECT * FROM $tabelTeams WHERE name = ? AND id_user = ?";
        $sqlFirstTeamCheck = $this->db->prepare($sqlFirstTeamCheck);
        $sqlFirstTeamCheck->bind_param("ss", $firstTeam, $userID);
        $sqlFirstTeamCheck->execute();
        $result = $sqlFirstTeamCheck->get_result();

        if ($result->num_rows > 0) {
            $sqlUpdateFirst = "UPDATE $tabelTeams SET home_count = home_count + 1 WHERE name = ? AND id_user = ?";
            $query = $this->db->prepare($sqlUpdateFirst);
            $query->bind_param("ss", $league, $userID);
            $query->execute();
        }
        else {
            $img = $this->imgSearch($firstTeam, "team");

            $sqlFirstTeamInsert = "INSERT INTO $tabelTeams (id, id_user, name, home_count, away_count, img) VALUES (NULL, ?, ?, 1, 0, ?)";
            $query = $this->db->prepare($sqlFirstTeamInsert);
            $query->bind_param("isi", $userID, $league, $img);
            $query->execute();
        }

        $sqlSecondTeamCheck = "SELECT * FROM $tabelTeams WHERE name = ? AND id_user = ?";
        $sqlSecondTeamCheck = $this->db->prepare($sqlSecondTeamCheck);
        $sqlSecondTeamCheck->bind_param("ss", $secondTeam, $userID);
        $sqlSecondTeamCheck->execute();
        $result = $sqlSecondTeamCheck->get_result();

        if ($result->num_rows > 0) {
            $sqlUpdateSecond = "UPDATE $tabelTeams SET away_count = away_count + 1 WHERE name = ? AND id_user = ?";
            $query = $this->db->prepare($sqlUpdateSecond);
            $query->bind_param("ss", $league, $userID);
            $query->execute();
        }
        else {
            $img = $this->imgSearch($secondTeam, "team");

            $sqlSecondTeamInsert = "INSERT INTO $tabelTeams (id, id_user, name, home_count, away_count, img) VALUES (NULL, ?, ?, 0, 1, ?)";
            $query = $this->db->prepare($sqlSecondTeamInsert);
            $query->bind_param("isi", $userID, $league, $img);
            $query->execute();
        }

        $sqlTakeIDLeague = "SELECT id FROM $tabelLeagues WHERE name = ?";
        $sqlTakeIDLeague = $this->db->prepare($sqlTakeIDLeague);
        $sqlTakeIDLeague->bind_param("s", $league);
        $sqlTakeIDLeague->execute();
        $LeagueID = $sqlTakeIDLeague->get_result()->fetch_assoc()['id'];

        $teams = [$firstTeam, $secondTeam];
        $teamsIDs = [];
        foreach ($teams as $team) {
            $sqlTakeIDTeam = "SELECT id FROM $tabelTeams WHERE name = ?";
            $sqlTakeIDTeam = $this->db->prepare($sqlTakeIDTeam);
            $sqlTakeIDTeam->bind_param("s", $team);
            $sqlTakeIDTeam->execute();
            $result = $sqlTakeIDTeam->get_result()->fetch_assoc()['id'];

            $teamsIDs[] = $result;
        }

        foreach ($teamsIDs as $team) {
            $sqlInsertBroker = "INSERT IGNORE INTO $tabelBroker VALUES (?, ?)";
            $query = $this->db->prepare($sqlInsertBroker);
            $query->bind_param("ii", $LeagueID, $team);
            $query->execute();
        }
        $this->db->commit();
    }

    private function imgSearch($varible, $teamOrLeague)
    {
        $sqlIMGSearch = "SELECT id FROM images WHERE name = ?";
        $sqlIMGSearch = $this->db->prepare($sqlIMGSearch);
        $sqlIMGSearch->bind_param("s", $varible);
        $sqlIMGSearch->execute();
        $result = $sqlIMGSearch->get_result()->fetch_assoc();
        $imgID = $result ? $result['id'] : null;

        if ($teamOrLeague == "league") {
            if ($imgID === null) {
                $img = 1;
            }
            else {
                $img = $imgID;
            }
        }
        else {
            if ($imgID === null) {
                $img = 2;
            }
            else {
                $img = $imgID;
            }
        }
        return $img;
    }
}
