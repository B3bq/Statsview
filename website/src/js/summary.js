//SUMMARY
//summary text
window.addEventListener('DOMContentLoaded', ()=>{
    //taking season from url
    let querystring = window.location.search;
    let urlParam = new URLSearchParams(querystring);
    let season = urlParam.get('season');

    if(season == 'year'){
        document.getElementById('lol').hidden =false;
        document.getElementById('cs').hidden =false;
    }
    
    document.getElementById('text').innerHTML = "Check your " + season + " summary";
})

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
            body: `season=${encodeURIComponent(season)}&sport=${encodeURIComponent(selected)}`
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
