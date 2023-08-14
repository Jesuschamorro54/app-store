"use strict";

const urlApi = "http://127.0.0.1:5000"
const http = {
    get: async function (url) {
        const response = await fetch(urlApi + url);
        return response.json();
    },

    post: async function (url, data) {

        var getHeader = {
            method: "POST", 
            cache: "no-cache",
            credentials: "same-origin",
            headers: {"Content-Type": "application/json"},
            redirect: "follow",
            referrerPolicy: "no-referrer",
            body: JSON.stringify(data),
        }
    
        const response = await fetch(urlApi + url, getHeader);
        return response.json();
    },
}

var currentCardIndex = 0;

function scrollCarousel(operation) {
  let possibleIndex =
    operation == "next" ? currentCardIndex + 4 : currentCardIndex - 4;

  possibleIndex = possibleIndex < 0 ? 0 : possibleIndex;

  let card = document.getElementById("card-" + possibleIndex);

  if (card) {
    currentCardIndex = possibleIndex;

    card.scrollIntoView({
      behavior: "smooth",
      inline: "start",
      block: "nearest",
    });
  }
}

const carousel = document.getElementById("carousel-cards");

function getFirtsVisibleElement() {
  // Obtén la posición actual del scroll en el div
  const scrollX = carousel.scrollLeft-55;

  // Obtiene el ancho del div visible
  const visibleWidth = carousel.clientWidth;

  for (const element of carousel.children) {
    const elementOffsetLeft = element.offsetLeft;

    // Comprueba si el elemento está dentro del área visible del div
    if (elementOffsetLeft >= scrollX && elementOffsetLeft <= scrollX + visibleWidth) {
      //   return element; // Retorna el primer elemento visible
      currentCardIndex = parseInt(element.id.split('-')[1]);
      break;
    }
  }

  // return null;
}

function debounce(func, tiempoEspera) {
  let timeoutId;

  return function (...args) {
    const context = this;

    // Borra el timeout actual para reiniciar el conteo
    clearTimeout(timeoutId);

    // Establece un nuevo timeout para ejecutar la función después del tiempo de espera
    timeoutId = setTimeout(() => {
      func.apply(context, args);
    }, tiempoEspera);
  };
}

const scrollDebounce = debounce(getFirtsVisibleElement, 500)
if (carousel) carousel.addEventListener("scroll", scrollDebounce);
