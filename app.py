# app.py
# We will use this pre-trained model for classifying Pokémons: https://huggingface.co/imjeffhi/pokemon_classifier
# You can test this model's accuracy in your browser, access the Space at: https://huggingface.co/spaces/TroglodyteDerivations/Pokemon_Classifier_Variant_5
from flask import Flask, request, jsonify
from transformers import ViTForImageClassification, ViTFeatureExtractor
from PIL import Image
import torch
import hashlib
import base64
import io

# Initialize Flask
app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = ViTForImageClassification.from_pretrained("imjeffhi/pokemon_classifier").to(device)
featureExtractor = ViTFeatureExtractor.from_pretrained('imjeffhi/pokemon_classifier')

# Cache for images, cached images are loaded 30 times faster
imageCache = {}

def getImageHash(imageData):
    # Generate a hash for the image, used for better storing
    hasher = hashlib.md5()
    hasher.update(imageData)
    return hasher.hexdigest()

def classifyImage(imageData):
    # Classify the image and cache the result as base64
    imgHash = getImageHash(imageData)

    if imgHash in imageCache:
        return imageCache[imgHash]

    img = Image.open(io.BytesIO(imageData))
    extracted = featureExtractor(images=img, return_tensors='pt').to(device)

    predictedId = model(**extracted).logits.argmax(-1).item()
    predictedPokemon = model.config.id2label[predictedId]

    imageCache[imgHash] = predictedPokemon

    return predictedPokemon

@app.route('/classify', methods=['POST'])
def classify():
    # Will take as input a base64 image and output a Pokémon name

    try:
        data = request.json
        imageBase64 = data.get('image', '')

        imageData = base64.b64decode(imageBase64)

        predictedPokemon = classifyImage(imageData)

        return jsonify({
            'pokemon': predictedPokemon
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
