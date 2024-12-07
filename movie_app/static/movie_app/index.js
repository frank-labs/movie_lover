document.addEventListener("DOMContentLoaded", function () {
    const watchLaterButton = document.getElementById("watch-later-btn");

    if (watchLaterButton) {
        watchLaterButton.addEventListener("click", function () {
            const movieId = this.getAttribute("data-movie-id");
            const url = `/toggle-watch-later/${movieId}/`; // Update with the correct URL pattern

            // Perform AJAX request
            fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(), // Ensure CSRF token is included
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.added) {
                        // Update button to show the movie was added
                        watchLaterButton.innerHTML = `
                            <i id="watch-later-icon" class="bi bi-check-circle text-success"></i> In Watch Later
                        `;
                    } else {
                        // Update button to show the movie was removed
                        watchLaterButton.innerHTML = `
                            <i id="watch-later-icon" class="bi bi-clock"></i> Add to Watch Later
                        `;
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        });
    }


});
// Function to get CSRF token
function getCSRFToken() {
    const csrfCookie = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="));
    return csrfCookie ? csrfCookie.split("=")[1] : "";
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".remove-watch-later-btn").forEach(button => {
        button.addEventListener("click", function (e) {
            e.preventDefault();
            const movieId = this.dataset.movieId;

            if (confirm("Are you sure you want to remove this movie from your Watch Later list?")) {
                fetch(`/watch-later/remove/${movieId}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCSRFToken(), // Ensure CSRF token is passed
                        "Content-Type": "application/json"
                    },
                })
                    .then(response => {
                        if (response.ok) {
                            // Remove the movie item from the DOM
                            this.closest(".movie-item").remove();
                        } else {
                            alert("Failed to remove the movie. Please try again.");
                        }
                    })
                    .catch(error => {
                        console.error("Error:", error);
                        alert("An error occurred. Please try again.");
                    });
            }
        });
    });
});