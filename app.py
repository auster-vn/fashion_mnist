from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import cv2
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = load_model('models/final_model.keras')
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28))
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=[0, -1])  # Thêm batch và channel

    predictions = model.predict(img).flatten()  # Flatten để có mảng 1 chiều
    result = [
        {'class': class_names[i], 'probability': float(predictions[i])}
        for i in range(len(class_names))
    ]

    return jsonify({'predictions': result})
if __name__ == '__main__':
    app.run(debug=True)

