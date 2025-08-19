const btn = document.getElementById('showPhotos');
const photos = document.getElementById('photos');
let isOpen = true;

btn?.addEventListener('click', ()=>{
    if(isOpen){
        photos.style.display = 'flex';
    }else{
        profil.src = profilDefault;
        photos.style.display = 'none';
    }
    isOpen = !isOpen;
})

const profil = document.getElementById('profil');
const images = document.querySelectorAll('img[name="profil"]');
const resetBtn = document.getElementById('cancelProfile')

const profilDefault = profil.src;

images.forEach((image)=>{
    image.addEventListener('click', ()=>{
        profil.src = image.src;

        images.forEach(img => {
            img.style = 'border: none; border-radius: 0;';
        })

        image.style = 'border: 5px solid #2ECC71; border-radius: 50%;';
    })
})

resetBtn.addEventListener('click', ()=>{
    profil.src = profilDefault;
    photos.style.display = 'none';
})