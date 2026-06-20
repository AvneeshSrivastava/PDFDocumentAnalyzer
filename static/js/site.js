document.addEventListener("DOMContentLoaded", function () {

    // Sidebar
    const sidebarBtn = document.getElementById("sidebar-toggle");
    const sidebar = document.getElementById("sidebar");

    if (sidebarBtn && sidebar) {

        sidebarBtn.addEventListener("click", function () {

            sidebar.classList.toggle("sidebar-collapsed");

        });

    }

    // Upload Spinner
    const form = document.getElementById("uploadForm");
    const spinner = document.getElementById("uploadSpinner");

    if (form && spinner) {

        form.addEventListener("submit", function () {

            spinner.classList.remove("d-none");

        });

    }

});

const uploadButton = document.getElementById("uploadButton");

if (form && spinner) {

    form.addEventListener("submit", function () {

        spinner.classList.remove("d-none");

        if (uploadButton) {

            uploadButton.disabled = true;
            uploadButton.innerText = "Processing...";

        }

    });

}