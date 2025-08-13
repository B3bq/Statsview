
![Logo](https://raw.githubusercontent.com/B3bq/Statsview/main/assets/logo.svg)

# STATSVIEW
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



# This is the project of app and website something like spotify wrapped
This will be show a summary stats of watched matches, how many games of team was watched, which league was watched most from all year. Also you can get a summary after end of a season. 

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/B3bq/Statsview/main/assets/Zrzut%20ekranu%202025-07-31%20173135.png)
![App Screenshot](https://raw.githubusercontent.com/B3bq/Statsview/main/assets/Zrzut%20ekranu%202025-07-31%20173206.png)
![App Screenshot](https://raw.githubusercontent.com/B3bq/Statsview/main/assets/Zrzut%20ekranu%202025-08-02%20224821.png)
![App Screenshot](https://raw.githubusercontent.com/B3bq/Statsview/main/assets/Zrzut%20ekranu%202025-08-02%20224841.png)


## Run Locally

First you need to make database in mysql server and import one of statsview.sql

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```
You need to install these libraries

#### PySide6
```bash
  pip install PySide6
```

#### mysql.connector
```bash
  pip install mysql-connector-python
```

#### dotenv
```bash
  pip install python-dotenv
```

#### BCRYPT
https://pypi.org/project/bcrypt

#### Composer
https://getcomposer.org/download/

#### PHPMailer
```bash
  composer require phpmailer/phpmailer
```
#### dotenv
```bash
  composer vlucas/phpdotenv
```

Install dependencies

```bash
  npm install
```



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`EMAIL_LOGIN`

`EMAIL_PASSWORD`

