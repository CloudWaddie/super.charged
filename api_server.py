from flask import Flask, request
import gemini_api
from io import BytesIO
from PIL import Image
import base64

app = Flask(__name__)

@app.route('/api/textToText', methods=['POST'])
def handle_text_to_text():
    data = request.get_json()
    prompt = data['prompt']
    key = data['key']
    result = gemini_api.textToText(prompt, key)
    return {'result': result}

@app.route('/api/imageToText', methods=['POST'])
def handle_image_to_text():
    data = request.get_json()
    image_base64 = data['image']
    key = data['key']

    # Convert base64 string back to image
    image_data = base64.b64decode(image_base64.split(',')[1])
    image = Image.open(BytesIO(image_data))

    result = gemini_api.ImageToText(image, key)
    return {'result': result}

@app.route('/api/imageAndTextToText', methods=['POST'])
def handle_image_and_text_to_image():
    data = request.get_json()
    prompt = data['prompt']
    image_base64 = data['image']
    key = data['key']

    # Convert base64 string back to image
    image_data = base64.b64decode(image_base64.split(',')[1])
    image = Image.open(BytesIO(image_data))

    result = gemini_api.ImageAndTextToText(prompt, image, key)
    return {'result': result}

if __name__ == '__main__':
    app.run(port=5000)