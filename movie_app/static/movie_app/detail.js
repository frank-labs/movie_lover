function getCSRFToken() {
    const csrfCookie = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="));
    return csrfCookie ? csrfCookie.split("=")[1] : "";
}

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
