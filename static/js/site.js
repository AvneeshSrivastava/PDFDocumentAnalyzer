// ==========================================================
// PDF Document Analyzer
// Client-side JavaScript
//
// Responsibilities:
// 1. Sidebar expand/collapse
// 2. Upload spinner
// 3. Prevent multiple form submissions
// ==========================================================

document.addEventListener("DOMContentLoaded", function () {

    // ======================================================
    // Sidebar Toggle
    // ======================================================

    const sidebarButton = document.getElementById("sidebar-toggle");
    const sidebar = document.getElementById("sidebar");

    if (sidebarButton && sidebar) {

        sidebarButton.addEventListener("click", function () {

            // Toggle collapsed state
            sidebar.classList.toggle("sidebar-collapsed");

        });

    }

    // ======================================================
    // Upload Form
    // ======================================================

    const uploadForm = document.getElementById("uploadForm");
    const uploadSpinner = document.getElementById("uploadSpinner");
    const uploadButton = document.getElementById("uploadButton");

    if (uploadForm && uploadSpinner) {

        uploadForm.addEventListener("submit", function () {

            // ----------------------------------------------
            // Show loading spinner
            // ----------------------------------------------

            uploadSpinner.classList.remove("d-none");

            // ----------------------------------------------
            // Prevent multiple uploads
            // ----------------------------------------------

            if (uploadButton) {

                uploadButton.disabled = true;

                uploadButton.innerHTML =
                    '<i class="bi bi-hourglass-split me-2"></i>Processing...';

            }

        });

    }

});

// ======================================================
// Bootstrap Tooltips
// ======================================================

// ==========================================================
// Tooltips (Only when sidebar is collapsed)
// ==========================================================

const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');

tooltips.forEach(function (element) {

    new bootstrap.Tooltip(element, {

        trigger: "hover"

    });

});

sidebarButton.addEventListener("click", function () {

    sidebar.classList.toggle("sidebar-collapsed");

    tooltips.forEach(function (element) {

        if (sidebar.classList.contains("sidebar-collapsed")) {

            element.setAttribute("data-bs-original-title", element.title);

        } else {

            bootstrap.Tooltip.getInstance(element)?.hide();

        }

    });

});