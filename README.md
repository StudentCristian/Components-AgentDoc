## Configuración del entorno de desarrollo

1. **Crear un entorno virtual**: Esto aísla las dependencias de tu proyecto.
   ```bash
   python3 -m venv env
   ```

2. **Activar el entorno virtual**: Navega al directorio del proyecto y activa el entorno.
   ```bash
   cd flask_file_upload
   source env/bin/activate
   ```

3. **Instalar dependencias**: Instala las dependencias necesarias desde `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Flask**: Establece las variables de entorno necesarias.
   ```bash
   export FLASK_APP="app.py"
   export FLASK_ENV="development"
   ```

5. **Ejecutar la aplicación**: Inicia el servidor de desarrollo de Flask.
   ```bash
   flask run
   ```

6. **Guardar dependencias**: Guarda las dependencias instaladas en `requirements.txt` (si has instalado nuevas dependencias).
   ```bash
   pip freeze > requirements.txt
   ```

Nota: Buscar el archivo `flask_uploads.py` y importar de esta forma para evitar errores de versiones:

```python
import sys

PY3 = sys.version_info[0] == 3

if PY3:
    string_types = str,
else:
    string_types = basestring,

import os.path
import posixpath

from flask import current_app, send_from_directory, abort, url_for
from itertools import chain
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from flask import Blueprint
```

---

## **Flask-Uploads**

Flask-Uploads allows your application to flexibly and efficiently handle file uploading and serving the uploaded files. You can create different sets of uploads - one for document attachments, one for photos, etc. - and the application can be configured to save them all in different places and to generate different URLs for them.

>Así luce el componente para subir archivos de manera local creado con `Flask`:

![alt text](/assets/upload_file.png)

---

**Referencias**

[Flask-Uploads](https://pythonhosted.org/Flask-Uploads/)

[step-by-step-guide-to-file-upload-with-flask](https://stackabuse.com/step-by-step-guide-to-file-upload-with-flask/)

[Tutorial-Flask](https://j2logo.com/tag/tutorial-flask/page/2/)