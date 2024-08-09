# app.py
from flask import Flask, request, send_file, render_template
from main import dress_person_with_garment
import os

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    person_image = request.files['person-image']
    garment_image = request.files['garment-image']

    person_image_path = os.path.join('uploads', person_image.filename)
    garment_image_path = os.path.join('uploads', garment_image.filename)

    person_image.save(person_image_path)
    garment_image.save(garment_image_path)

    output_path = dress_person_with_garment(person_image_path, garment_image_path)
    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
