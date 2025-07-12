from flask import Flask, render_template, request, jsonify
from encrypt_decrypt import encrypt_data, decrypt_data
import base64
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

FILENAME_DELIMITER = b'::FILENAME::'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    file = request.files['file']
    password = request.form['password']
    original_filename = file.filename.encode()
    file_content = file.read()

    merged_data = original_filename + FILENAME_DELIMITER + file_content
    encrypted_data = encrypt_data(merged_data, password)
    encoded_content = base64.b64encode(encrypted_data).decode()

    return jsonify({
        'filename': f"{file.filename}.enc",
        'content': encoded_content
    })

@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    file = request.files['file']
    password = request.form['password']

    if not file or not password:
        return jsonify({'error': 'File or password missing.'}), 400

    try:
        encrypted_content = file.read()
        decrypted_data = decrypt_data(encrypted_content, password)  

        print("Decrypted data preview:", decrypted_data[:100])  
        print("Decrypted data preview:", decrypted_data[:100])
        print("Looking for delimiter:", FILENAME_DELIMITER in decrypted_data)
        

        if FILENAME_DELIMITER not in decrypted_data:
            print("Delimiter check failed!")
            raise ValueError("Delimiter missing")

        filename_part, content_part = decrypted_data.split(FILENAME_DELIMITER, 1)
        original_filename = filename_part.decode(errors='ignore')  # Optional: avoid crashes on decode

        encoded_content = base64.b64encode(content_part).decode()

        return jsonify({
            'filename': original_filename,
            'content': encoded_content
        })

    except ValueError as ve:
        print("ValueError:", ve)
        return jsonify({'error': f'Decryption failed: {str(ve)}'}), 400
    except Exception as e:
        print("Exception:", e)
        return jsonify({'error': 'Decryption failed: Invalid file or wrong password.'}), 400



@app.route('/encrypt-text', methods=['POST'])
def encrypt_text():
    data = request.json
    text = data['text'].encode()
    password = data['password']
    encrypted = encrypt_data(text, password)
    return base64.b64encode(encrypted).decode()

@app.route('/decrypt-text', methods=['POST'])
def decrypt_text():
    data = request.json
    text = base64.b64decode(data['text'])
    password = data['password']
    try:
        decrypted = decrypt_data(text, password)
        return decrypted.decode()
    except Exception:
        return "Decryption failed.", 400

if __name__ == '__main__':
    app.run(debug=True)
