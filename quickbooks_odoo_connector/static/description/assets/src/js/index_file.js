
document.addEventListener("DOMContentLoaded", function () {
    alert("Hello, World!");
    const toggles = document.querySelectorAll(".accordion-toggle");
   console.log(toggles);
    toggles.forEach((toggle) => {
    toggle.addEventListener("click", function (e) {
        e.preventDefault();
        const contentId = this.getAttribute("href").substring(1);
        const content = document.getElementById(contentId);

        if (content.style.display === "block") {
        content.style.display = "none";
        } else {
        document.querySelectorAll('.accordion-content').forEach((el) => el.style.display = 'none');
        content.style.display = "block";
        }
    });
    });
});
