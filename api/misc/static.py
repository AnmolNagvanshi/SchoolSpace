from app import app
from flask import send_from_directory

@app.route('/static/<path:path>/<string:file>', methods=['GET', 'POST'])
def serve_static_resources(path, file):
    return send_from_directory(path, file)

