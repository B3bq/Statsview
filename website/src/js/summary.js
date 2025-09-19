//SUMMARY
let lang = navigator.language; //browser language

//selecting sport
document.getElementById('sport').addEventListener("change", function(){
    //taking season from url
    let querystring = window.location.search;
    let urlParam = new URLSearchParams(querystring);
    let season = urlParam.get('season');

    document.getElementById('text').style.visibility = 'hidden';

    const selected = this.value; //take selected value

    fetch('src/php/summary.php', {
        method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `season=${encodeURIComponent(season)}&sport=${encodeURIComponent(selected)}&lang=${encodeURIComponent(lang)}`
    })
    .then(response=>response.json())
    .then(data=>{
        if(data.home && data.away){
            document.getElementById('data').innerHTML = data.summary + data.home + data.away + data.leagues + data.teams;
        }else{
            document.getElementById('data').innerHTML = data.summary + data.leagues + data.teams;
        }
    })
})
