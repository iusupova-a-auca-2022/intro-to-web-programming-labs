const gallery = document.querySelector(".gallery");
const urls = ["https://www.aaha.org/wp-content/uploads/2024/03/b5e516f1655346558958c939e85de37a.jpg",
        "https://nationalzoo.si.edu/sites/default/files/styles/square_large/public/2025-01/20241030-817A8773-16RP.jpg?h=f6ccde7b&itok=m27pXZwZ",
        "https://s7ap1.scene7.com/is/image/destqueensland/teq/consumer/global/images/destinations/sunshine-coast/blog-images/editorial-hero-banner/2018_SC_Koala_Wildlife_Australiazoo.jpg?bfc=on&fit=wrap&fmt=webp&qlt=100&resMode=bisharp&wid=1200",
        "https://cdn.britannica.com/94/494-050-A674AD3A/Fallow-deer-dama-dama.jpg"
]

urls.forEach(url => {
    let img = document.createElement("img");
    img.src = url;
    img.classList.add("item");
    gallery.appendChild(img);
})

let modal = document.getElementById("modal");
let modalImg = document.getElementById("modal-img");
let btn = document.querySelector(".close");
let images = document.querySelectorAll(".item");

let currentIndex = 0;

images.forEach((img, index) => {
    img.addEventListener("click", function() {
        currentIndex = index;
        modal.classList.remove("fadeOut");
        showImage();
    })
})

function showImage() {
        modal.style.display = "flex";
        modalImg.src = images[currentIndex].src;
}

btn.addEventListener("click", function() {
    modal.classList.toggle("fadeOut");
    modal.style.display = "none";
})

window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
})

modalImg.addEventListener("click", function() {
    modalImg.classList.toggle("zoom");
})

document.getElementById("prev").addEventListener("click", function() {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : images.length - 1;
    showImage();
})

document.getElementById("next").addEventListener("click", function() {
    currentIndex = (currentIndex < images.length - 1) ? currentIndex + 1 : 0;
    showImage();
})