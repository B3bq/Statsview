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
        <form>
            <?php
                $server = "localhost";
                $login = "root";
                $password = "";
                $base = "stats";


                $connect = mysqli_connect($server, $login, $password, $base); //connecting to database

                //shoing a choose list of leagues
                $sql = "SELECT name FROM league";
                $result = $connect->query($sql);


                if($result->num_rows > 0){
                    //echo "<form>";
                    echo "<select name='league'>";
                    while($row = mysqli_fetch_assoc($result)){
                        echo "<option>".$row['name']."</option>";
                    }
                    //echo "</form>";
                    echo "</select>";
                }else{
                    echo "<h1>You don't have any teams to choose</h1>";
                }


                //showing a choose list of teams
                $sql2 = "SELECT name FROM teams";
                $result = $connect->query($sql2);

                if($result->num_rows > 0){
                    //echo "<form>";
                    echo "<select name='teamOne'>";
                    while($row = mysqli_fetch_assoc($result)){
                        echo "<option>".$row['name']."</option>";
                    }
                    //echo "</form>";
                    echo "</select>";
                }else{
                    echo "<h1>You don't have any teams to choose</h1>";
                }

                mysqli_close($connect);
                ?>
            </form>
    </div>
</body>
</html>