document.addEventListener("DOMContentLoaded", () => {

    const toggleButton = document.getElementById("sidebar-toggle");
    const sidebar = document.getElementById("sidebar");

    toggleButton.addEventListener("click", () => {
        sidebar.classList.toggle("sidebar-collapsed");
    });

});