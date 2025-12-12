const pantalla = document.querySelector(".pantalla");
const botones = document.querySelectorAll(".btn");

botones.forEach(boton => manejarEventoClick(boton));
    boton.addEventListener("click", () => {
        console.log(boton.textContent)
    });
