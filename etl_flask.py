from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# Ensure the 'uploads' folder exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    # Save the uploaded file to the 'uploads' directory
    file.save(os.path.join('uploads', file.filename))
    return f'File {file.filename} uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)

