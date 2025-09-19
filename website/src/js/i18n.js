function getCookie(name){
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

const userID = getCookie("user"); //user id

Promise.all([
  fetch("src/js/locales/en_translation.json").then(res => res.json()),
  fetch("src/js/locales/pl_translation.json").then(res => res.json())
]).then(([en, pl]) => {
  i18next.init({
    lng: navigator.language.startsWith("pl") ? "pl" : "en",
    fallbackLng: "en",
    resources: {
      en: { translation: en },
      pl: { translation: pl }
    }
  }).then(() => {
    translatePage();

    if(userID){
      updateMenuForUser();
      
      let querystring = window.location.search;
      let urlParam = new URLSearchParams(querystring);
      let season = urlParam.get('season');

      if(season == 'year'){
          document.getElementById('lol').hidden =false;
          document.getElementById('cs').hidden =false;
          document.getElementById('text').innerHTML = i18next.t("summary.year");
          document.getElementById('text').style = "text-wrap: wrap;";
        }else{
          document.getElementById('text').innerHTML = i18next.t("summary.season");
          document.getElementById('text').style = "text-wrap: wrap;";
      }
    }
  });
});

function translatePage() {
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    el.innerHTML = i18next.t(key);
  });

  document.querySelectorAll("[data-i18n-attr]").forEach(el => {
    const mappings = el.getAttribute("data-i18n-attr").split(";");
    mappings.forEach(map => {
      const [attr, key] = map.split(":");
      el.setAttribute(attr.trim(), i18next.t(key.trim()));
    });
  });
}
function updateMenuForUser(){
  document.getElementById('option1').innerHTML = i18next.t("menu_account.option1");
  document.getElementById('option1').title = i18next.t("menu_account.option1");
  document.getElementById('option1').href = "account.php";

  document.getElementById('option2').innerHTML = i18next.t("menu_account.option2");
  document.getElementById('option2').title = i18next.t("menu_account.option2");
  document.getElementById('option2').href = "actionpanel.html";
        
  document.getElementById('logout').innerHTML = i18next.t("menu_account.logout");
  document.getElementById('logout').title = i18next.t("menu_account.logout");
}