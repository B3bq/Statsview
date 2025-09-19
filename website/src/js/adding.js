let lang = navigator.language; //browser language

//ADDING FROM EXIST
//select leagues
document.getElementById('sportAdd').addEventListener("change", function(){
    const selected = this.value;

    let season = '';

    // get today date
    const today = new Date();
    const mm = String(today.getMonth()+1).padStart(2, '0');
    const todayString = `${mm}`;

    if(todayString == '07'){
        season = 'season';
    }else{
        season = 'year';
    }

    fetch('src/php/leagueex.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `season=${encodeURIComponent(season)}&sport=${encodeURIComponent(selected)}&lang=${encodeURIComponent(lang)}`
    })
    .then(response=>response.json())
    .then(data=>{
        document.getElementById('league').hidden = false;
        document.getElementById('league').innerHTML = data.leagues;
    })
})

//select teams
document.getElementById('league').addEventListener("change", function(){
    const sport = document.getElementById('sportAdd').value;
    const selected = this.value;

    let season = '';

    // get today date
    const today = new Date();
    const mm = String(today.getMonth()+1).padStart(2, '0');
    const todayString = `${mm}`;

    if(todayString == '07'){
        season = 'season';
    }else{
        season = 'year';
    }

    fetch('src/php/team.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `season=${encodeURIComponent(season)}&sport=${encodeURIComponent(sport)}&league=${encodeURIComponent(selected)}&lang=${encodeURIComponent(lang)}`
    })
    .then(response=>response.json())
    .then(data=>{
        document.getElementById('add_btn').hidden = false;
        document.getElementById('fteam').hidden = false;
        document.getElementById('second').hidden = false;
        document.getElementById('fteam').innerHTML = data.firstTeam;
        console.log(data.firstTeam);
        document.getElementById('second').innerHTML = data.secondTeam;
    })
})