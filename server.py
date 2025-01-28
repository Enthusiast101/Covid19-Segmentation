import io
import base64
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template_string
from PIL import Image

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string("<h1>Hello, Don't forget to check out my vlog channel<h1> <br>" + youtube_code)


@app.route("/model", methods = ['POST'])
def data():
    file = request.files['image']
    
    image = Image.open(file)
    image = image.resize((128, 128)) 
    image = np.asarray(image)[..., np.newaxis][np.newaxis, ...]
    
    model = tf.keras.models.load_model("models/UNet.h5")
    pred = model.predict(image)
    
    pred = np.squeeze(pred)
    pred = (pred * 255).clip(0, 255).astype(np.uint8)
    pred = Image.fromarray(pred)

    buffer = io.BytesIO()
    pred.save(buffer, format="PNG")
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    return jsonify({"success": True, "image": image_base64}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1111, debug=True)