document.addEventListener("DOMContentLoaded", function() {
    const details = document.querySelectorAll("details");

    details.forEach(detail => {
        detail.addEventListener("click", function() {
            const panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    });
});

