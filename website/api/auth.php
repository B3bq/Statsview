<?php

class User{
    private $db;

    public function __construct($conn){
        $this->db = $conn;
    }

    public function userName(){
        $data = json_decode(file_get_contents("php://input"), true);
        $name = $data['name'];

        $query = "SELECT * FROM users WHERE name = ?";
        $query = $this->db->prepare($query);
        $query->bind_param("s", $name);
        $query->execute();
        $res = $query->get_result();

        if($res->num_rows == 0){
            echo json_encode(["success" => True]);
        }else{
            echo json_encode(["success" => False]);
        }
    }

    public function userChecking(){
        $data = json_decode(file_get_contents("php://input"), true);
        $login = $data['login'];
        $pass = $data['password'];

        $query = "SELECT mail, name FROM users WHERE mail = ? or name = ?";
        $query = $this->db->prepare($query);
        $query->bind_param("ss", $login, $login);
        $query->execute();
        $res = $query->get_result();

        if ($res->num_rows > 0) {
            $query = "SELECT password FROM users WHERE name = ? or mail = ?";
            $query = $this->db->prepare($query);
            $query->bind_param("ss", $login, $login);
            $query->execute();
            $response = $query->get_result()->fetch_assoc()['password'];

            if(password_verify($pass, $response)){
                $query = "SELECT id_users FROM users WHERE name = ? or mail = ?";
                $query = $this->db->prepare($query);
                $query->bind_param("ss", $login, $login);
                $query->execute();
                $userID = $query->get_result()->fetch_assoc()['id_users'];

                echo json_encode(["success" => true, "id_user" => $userID]);
            }else{
                echo json_encode(["success" => false, "text" => "Incorrect password"]);
            }
        }else{
            echo json_encode(["success" => false, "text" => "User don't exist"]);
        }
    }
    
    public function userAdd(){
        $data = json_decode(file_get_contents("php://input"), true);
        $name = $data['name'];
        $mail = $data['mail'];
        $hash = $data['hashed'];

        if ($this->userExists($name)){
            echo json_encode(["success" => false]);
            return;
        }else{
            $query = "INSERT INTO users (id_users, mail, name, password, photo) VALUES (NULL, ?, ?, ?, 'src/img/user.png')";
            $query = $this->db->prepare($query);
            $query->bind_param("sss", $mail, $name, $hash);
            $query->execute();

            echo json_encode(["success" => true]);
        }
    }

    private function userExists($login){
        $query = "SELECT id_users FROM users WHERE name = ?";
        $stmt = $this->db->prepare($query);
        $stmt->bind_param("s", $login);
        $stmt->execute();
        $res = $stmt->get_result();
    
        return $res->num_rows > 0;
    }
}

?>