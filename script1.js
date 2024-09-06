document.getElementById('chat-form').onsubmit = function(e) {
    e.preventDefault();
    const textInput = document.getElementById('text-input');
    const text = textInput.value;
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'text': text})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('response').innerText = data.intent;
    })
    .catch(error => console.error('Error:', error));
    textInput.value = '';  
};
