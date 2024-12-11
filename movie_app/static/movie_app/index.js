
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