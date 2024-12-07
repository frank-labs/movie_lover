// Function to get CSRF token
function getCSRFToken() {
    const csrfCookie = document.cookie
        .split("; ")
        .find((row) => row.startsWith("csrftoken="));
    return csrfCookie ? csrfCookie.split("=")[1] : "";
}



document.addEventListener("DOMContentLoaded", () => {
    // Event delegation to handle actions dynamically
    const tableBody = document.querySelector("table tbody");

    tableBody.addEventListener("click", function (e) {
        const row = e.target.closest("tr"); // Find the clicked row
        const collectionId = row.dataset.id; // Get the collection ID

        if (e.target.classList.contains("edit-btn")) {
            // Enable inline editing
            row.querySelectorAll(".display").forEach(el => el.classList.add("d-none"));
            row.querySelectorAll(".edit-input").forEach(el => el.classList.remove("d-none"));
            row.querySelector(".edit-btn").classList.add("d-none");
            row.querySelector(".check-btn").classList.remove("d-none");
        } else if (e.target.classList.contains("check-btn")) {
            // Save changes
            const newName = row.querySelector(".collection-name .edit-input").value;
            const newDescription = row.querySelector(".collection-description .edit-input").value;

            // Send data to the backend (AJAX)
            fetch(`/collections/update/${collectionId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCSRFToken(),
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ name: newName, description: newDescription }),
            })
            .then(response => {
                if (response.ok) {
                    // Update UI with new values
                    row.querySelector(".collection-name .display").textContent = newName;
                    row.querySelector(".collection-description .display").textContent = newDescription;
                    
                    // Switch back to display mode
                    row.querySelectorAll(".display").forEach(el => el.classList.remove("d-none"));
                    row.querySelectorAll(".edit-input").forEach(el => el.classList.add("d-none"));
                    row.querySelector(".edit-btn").classList.remove("d-none");
                    row.querySelector(".check-btn").classList.add("d-none");
                } else {
                    alert("Failed to update. Please try again.");
                }
            })
            .catch(error => console.error("Error:", error));
        } else if (e.target.classList.contains("delete-btn")) {
            // Delete collection
            if (confirm("Are you sure you want to delete this collection?")) {
                fetch(`/collections/delete/${collectionId}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": getCSRFToken(),
                    },
                })
                .then(response => {
                    if (response.ok) {
                        row.remove(); // Remove row from the DOM
                    } else {
                        alert("Failed to delete. Please try again.");
                    }
                })
                .catch(error => console.error("Error:", error));
            }
        }
    });
});
