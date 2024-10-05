from flask import Flask, render_template, request, abort, make_response, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuración de la carpeta de carga
app.config['UPLOAD_FOLDER'] = 'upload'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

ALLOWED_EXTENSIONS = {'docx', 'doc'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(413)
def file_too_large(e):
    return make_response(jsonify(message="File is too large"), 413)

# Nueva ruta para la raíz
@app.route('/')
def index():
    return render_template('upload_form.html')  # Asegúrate de tener este archivo HTML

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(success=False, message='No file part in the request'), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify(success=False, message='No selected file'), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(success=True, message='File uploaded successfully')
        except Exception as e:
            return jsonify(success=False, message=f'Error saving file: {str(e)}'), 500

    return jsonify(success=False, message='File type not allowed'), 400