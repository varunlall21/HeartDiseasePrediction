document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Get form data
    const formData = new FormData(this);
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = parseFloat(value); // Convert values to numbers
    });
    
    // Send data to backend
    fetch('/predict', { // Assuming your Flask route for prediction is '/predict'
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Display prediction result
            const resultDiv = document.getElementById('prediction-result');
            resultDiv.innerHTML = `Prediction Probability: ${data.prediction.toFixed(2) * 100}%`;
            resultDiv.style.display = 'block'; // Show the result section

            // Display tips and suggestions
            const tipsSection = document.querySelector('.tips-section');
            const tipsList = tipsSection.querySelector('ul');
            tipsList.innerHTML = ''; // Clear previous tips
            data.tips.forEach(tip => {
                const li = document.createElement('li');
                li.textContent = tip;
                tipsList.appendChild(li);
            });
            tipsSection.style.display = 'block'; // Show the tips section

        })
        .catch(error => {
            console.error('Error:', error);
            // Handle errors (e.g., display an error message to the user)
            const resultDiv = document.getElementById('prediction-result');
            resultDiv.innerHTML = 'An error occurred during prediction.';
            resultDiv.style.color = '#ff0000'; // Red color for error
            resultDiv.style.display = 'block';
        });
});
