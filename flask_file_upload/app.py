from flask import Flask, render_template, request, jsonify
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS, patch_request_class
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuración de la carpeta de carga
app.config['UPLOADED_DOCUMENTS_DEST'] = 'upload'  # Directorio donde se guardarán los archivos
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

# Definir el conjunto de cargas para documentos
documents = UploadSet('documents', DOCUMENTS)

# Configurar las cargas
configure_uploads(app, documents)

# Limitar el tamaño de las cargas
patch_request_class(app, 16 * 1024 * 1024)  # 16 MB

@app.errorhandler(413)
def file_too_large(e):
    return jsonify(success=False, message="File is too large"), 413

@app.route('/')
def index():
    return render_template('upload_form.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify(success=False, message='No file part in the request'), 400

    files = request.files.getlist('file')
    if not files:
        return jsonify(success=False, message='No selected files'), 400

    for file in files:
        if file.filename == '':
            return jsonify(success=False, message='One or more files have no name'), 400

        if file and allowed_file(file.filename):
            filename = documents.save(file)  # Guardar el archivo usando Flask-Uploads
        else:
            return jsonify(success=False, message='File type not allowed'), 400

    return jsonify(success=True, message='Files uploaded successfully')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in documents.extensions  # Verificar si la extensión es permitida

if __name__ == '__main__':
    app.run(debug=True)