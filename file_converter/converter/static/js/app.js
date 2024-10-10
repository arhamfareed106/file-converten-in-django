document.addEventListener('DOMContentLoaded', () => {
    // Animate the h1 element on page load
    gsap.from("h1", { duration: 1, y: -50, opacity: 0, ease: "bounce" });

    // Handle form submit with animation
    const fileForm = document.getElementById('fileForm');
    if (fileForm) {
        fileForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Prevent the default form submission behavior

            // Validate file input and format selection
            const fileInput = document.getElementById('fileInput');
            const formatSelect = document.getElementById('format');
            if (!fileInput.files.length || !formatSelect.value) {
                alert("Please select a file and format.");
                return; // Stop the submission process if no file or format is selected
            }

            // Animate the form
            gsap.to(fileForm, {
                duration: 0.5, 
                scale: 0.95, 
                opacity: 0.7, 
                onComplete: () => {
                    fileForm.submit(); // Submit the form after animation completes
                }
            });
        });
    }
});

 // Animate the container with a fade-in effect
 gsap.from(".container", {
    duration: 1, 
    opacity: 0, 
    y: -50, 
    ease: "power2.out"
});

// Animate the form elements with a staggered fade-in effect
gsap.from("form input, form select, form button", {
    duration: 1, 
    opacity: 0, 
    y: 50, 
    stagger: 0.2, 
    ease: "power2.out"
});

// Add hover effect on the submit button
const button = document.querySelector("button");
if (button) {
    button.addEventListener("mouseenter", () => {
        gsap.to(button, { scale: 1.1, duration: 0.2, ease: "power1.inOut" });
    });

    button.addEventListener("mouseleave", () => {
        gsap.to(button, { scale: 1, duration: 0.2, ease: "power1.inOut" });
    });
}
