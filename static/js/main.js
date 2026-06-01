// ONG Impact Portal — scripts légers côté client
document.addEventListener("DOMContentLoaded", () => {
  const nav = document.querySelector(".main-nav");
  if (nav && window.innerWidth < 768) {
    nav.setAttribute("aria-label", "Navigation principale");
  }
});
