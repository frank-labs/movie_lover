function getCSRFToken() {
    const csrfCookie = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="));
    return csrfCookie ? csrfCookie.split("=")[1] : "";
}
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

document.getElementById('submit-add-to-collections').addEventListener('click', function () {
    // Get the movie ID from the button's data-movie-id attribute
    const movieId = this.getAttribute('data-movie-id');
    
    // Collect all selected collections (checkboxes)
    const checkboxes = document.querySelectorAll('#add-to-collections-form input[name="collections"]:checked');
    const selectedCollections = Array.from(checkboxes).map(checkbox => checkbox.value);

    // Check if any collections are selected
    if (selectedCollections.length === 0) {
        alert("Please select at least one collection.");
        return;
    }

    // Prepare POST data
    const postData = {
        movie_id: movieId,
        collections: selectedCollections,
    };
    const addToCollectionsUrl = this.getAttribute('data-url');
    // Send the data to the server using Fetch API
    fetch(addToCollectionsUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify(postData),
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error("Failed to add movie to collections");
            }
        })
        .then(data => {
            // Success feedback
            alert(data.message || "Movie successfully added to selected collections!");
            // Optionally dismiss the modal
            const modal = bootstrap.Modal.getInstance(document.getElementById('addToCollectionModal'));
            modal.hide();
        })
        .catch(error => {
            console.error(error);
            alert("An error occurred while adding the movie to collections.");
        });
});
