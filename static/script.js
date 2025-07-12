function toggleMode() {
    const mode = document.getElementById('modeSelector').value;
    document.getElementById('fileSection').style.display = (mode.includes('file')) ? 'block' : 'none';
    document.getElementById('textSection').style.display = (mode.includes('text')) ? 'block' : 'none';

    document.getElementById('encryptBtn').style.display = (mode === 'file-encrypt' || mode === 'text-encrypt') ? 'block' : 'none';
    document.getElementById('decryptBtn').style.display = (mode === 'file-decrypt' || mode === 'text-decrypt') ? 'block' : 'none';

    document.getElementById('resultContainer').style.display = 'none';
    document.getElementById('downloadBtn').style.display = 'none';
}

function togglePassword() {
    const input = document.getElementById('passwordInput');
    const eyeIcon = document.getElementById('eyeIcon');
    if (input.type === 'password') {
        input.type = 'text';
        eyeIcon.className = 'fa fa-eye-slash';
    } else {
        input.type = 'password';
        eyeIcon.className = 'fa fa-eye';
    }
}

function handleEncrypt() {
    const mode = document.getElementById('modeSelector').value;
    if (mode === 'file-encrypt') {
        processFile('/encrypt');
    } else if (mode === 'text-encrypt') {
        processText('/encrypt-text');
    }
}

function handleDecrypt() {
    const mode = document.getElementById('modeSelector').value;
    if (mode === 'file-decrypt') {
        processFile('/decrypt');
    } else if (mode === 'text-decrypt') {
        processText('/decrypt-text');
    }
}

function processFile(url) {
    const file = document.getElementById('fileInput').files[0];
    const password = document.getElementById('passwordInput').value;
    if (!file || !password) {
        alert("Please select a file and enter a password.");
        return;
    }

    const formData = new FormData();
    formData.append('file', file);
    formData.append('password', password);

    fetch(url, { method: 'POST', body: formData })
        .then(response => response.json())
        .then(data => {
    if (data.error) {
        alert(data.error);
        return;
    }

    
    const decodedContent = atob(data.content);  // base64 to binary string
    const byteArray = new Uint8Array(decodedContent.split('').map(char => char.charCodeAt(0))); // binary string to Uint8Array

    const blob = new Blob([byteArray], { type: 'application/octet-stream' });

    const resultContainer = document.getElementById('resultContainer');
    resultContainer.style.display = 'block';
    document.getElementById('resultText').textContent = 'File encrypted successfully!';

    const downloadBtn = document.getElementById('downloadBtn');
    downloadBtn.href = window.URL.createObjectURL(blob);
    downloadBtn.download = data.filename;
    downloadBtn.style.display = 'inline-block';
})
       .catch(error => alert('Error: ' + error));
}

function processText(url) {
    const text = document.getElementById('textInput').value;
    const password = document.getElementById('passwordInput').value;
    if (!text || !password) {
        alert("Please enter text and a password.");
        return;
    }

    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, password })
    })
    .then(response => {
        if (!response.ok) throw new Error("Decryption failed.");
        return response.text();
    })
    .then(result => {
        const resultContainer = document.getElementById('resultContainer');
        resultContainer.style.display = 'block';
        document.getElementById('resultText').textContent = result;
        document.getElementById('downloadBtn').style.display = 'none';
    })
    .catch(error => alert('Error: ' + error));
}
