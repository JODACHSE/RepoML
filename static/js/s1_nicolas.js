// s1_nicolas.js
document.addEventListener("DOMContentLoaded", function () {
    const helloEl = document.getElementById("hello");
    if (helloEl) {
        // Agrega un efecto interactivo al hacer clic sobre el mensaje
        helloEl.addEventListener("click", function () {
            helloEl.style.transition = "transform 0.5s ease-in-out";
            helloEl.style.transform = "rotate(360deg)";
            setTimeout(() => {
                helloEl.style.transform = "rotate(0deg)";
            }, 500);
        });
    }
});
