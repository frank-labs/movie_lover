function getCSRFToken() {
    const csrfCookie = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="));
    return csrfCookie ? csrfCookie.split("=")[1] : "";
}


document.addEventListener("click", function (event) {
    // Check if the clicked element is a "remove-from-collection-btn"
    if (event.target.classList.contains("remove-from-collection-btn")) {
        event.preventDefault();

        // Extract the movie ID and collection ID from the button's dataset
        const movieId = event.target.getAttribute("data-movie-id");
        const collectionId = event.target.getAttribute("data-collection-id");

        // Confirm removal
        if (!confirm("Are you sure you want to remove this movie from the collection?")) {
            return;
        }

        // Send an AJAX request to remove the movie from the collection
        fetch(`/collections/${collectionId}/remove-movie/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: JSON.stringify({ movie_id: movieId }),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to remove movie from collection.");
                }
                return response.json();
            })
            .then((data) => {
                // Remove the movie item from the grid if the request is successful
                if (data.success) {
                    const movieItem = event.target.closest(".movie-item");
                    movieItem.remove();
                } else {
                    alert("An error occurred while removing the movie.");
                }
            })
            .catch((error) => {
                console.error(error);
                alert("An error occurred. Please try again.");
            });
    }
});