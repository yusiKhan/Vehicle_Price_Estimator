document.addEventListener("DOMContentLoaded", function() {

    // 1. Auto-Calculate Car Age
    // We use 2025 as the base year because the dataset contains 2025 models (Age 0).
    // This logic mimics the training data preprocessing.
    const yearInput = document.getElementById('Year');
    const ageInput = document.getElementById('CarAge');
    const BASE_YEAR = 2025;

    if (yearInput && ageInput) {
        yearInput.addEventListener('input', function() {
            const val = parseInt(this.value);
            if (!isNaN(val)) {
                // Ensure age is not negative if user enters > 2025
                const age = Math.max(0, BASE_YEAR - val);
                ageInput.value = age;
            } else {
                ageInput.value = '';
            }
        });
    }

    // 2. Loading State on Submit
    const form = document.getElementById('predictForm');
    const btn = document.getElementById('submitBtn');
    const loader = document.querySelector('.loader');
    const btnText = document.querySelector('.btn-text');

    if (form) {
        form.addEventListener('submit', function() {
            btn.style.opacity = "0.8";
            btn.style.cursor = "wait";
            btnText.innerText = "Analyzing...";
            loader.style.display = "inline-block";
        });
    }
});