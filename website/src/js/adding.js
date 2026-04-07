let lang = navigator.language; //browser language

//ADDING FROM EXIST

function getSeasontype() {
    const today = new Date();
    const month = today.getMonth() + 1; // months are zero-indexed

    if (month === 1){
        return 'season';
    }
    if (month === 7){
        return 'year';
    }

    return 'auto';
}

async function getLeagues(sport) {
    const seasonType = getSeasontype();

    async function request(season) {
        const response = await fetch('src/php/leagueex.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `season=${encodeURIComponent(season)}&sport=${encodeURIComponent(sport)}&lang=${encodeURIComponent(lang)}`
        });
        return response.json();
    }

    if (seasonType === 'season' || seasonType === 'year') {
        return request(seasonType);
    }

    let data = await request('season'); // first try season for auto

    if (!data.leagues || data.leagues.trim() === '') {
        data = await request('year');
    }

    return data;
}

async function getTeams(sport, league) {
    const seasonType = getSeasontype();

    async function request(season) {
        const response = await fetch('src/php/team.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `season=${encodeURIComponent(season)}&sport=${encodeURIComponent(sport)}&league=${encodeURIComponent(league)}&lang=${encodeURIComponent(lang)}`
        });
        return response.json();
    }

    if (seasonType === 'season' || seasonType === 'year') {
        return request(seasonType);
    }

    let data = await request('season');

    if (!data.firstTeam || data.firstTeam.trim() === '') {
        data = await request('year');
    }

    return data;
}

//select leagues
document.getElementById('sportAdd').addEventListener("change", async function(){
    const selected = this.value;
    const data = await getLeagues(selected);

    document.getElementById('league').hidden = false;
    document.getElementById('league').innerHTML = data.leagues;
})

//select teams
document.getElementById('league').addEventListener("change", async function(){
    const sport = document.getElementById('sportAdd').value;
    const selected = this.value;
    const data = await getTeams(sport, selected);

    document.getElementById('add_btn').hidden = false;
    document.getElementById('fteam').hidden = false;
    document.getElementById('second').hidden = false;
    document.getElementById('fteam').innerHTML = data.firstTeam;
    document.getElementById('second').innerHTML = data.secondTeam;
})