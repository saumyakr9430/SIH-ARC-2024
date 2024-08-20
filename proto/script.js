document.getElementById('ciphertext-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const ciphertext = document.getElementById('ciphertext').value.trim();
    const resultElement = document.getElementById('algorithm');
    const errorElement = document.getElementById('error-message');
    const errorTextElement = document.getElementById('error-text');

    // Clear previous results
    resultElement.textContent = '';
    errorElement.classList.add('hidden');

    if (!ciphertext) {
        errorElement.classList.remove('hidden');
        errorTextElement.textContent = 'Ciphertext cannot be empty.';
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5001/identify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ ciphertext })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const data = await response.json();
        if (data.algorithm) {
            resultElement.textContent = `Detected Algorithm: ${data.algorithm}`;
        } else if (data.error) {
            errorElement.classList.remove('hidden');
            errorTextElement.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        errorElement.classList.remove('hidden');
        errorTextElement.textContent = `Error: ${error.message}`;
    }
});
