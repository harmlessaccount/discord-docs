# Pokémon Classifier with Integrated API

This is a simple code integrating a pre-trained model from HugginFace with an API.

# Installation

Run a virtual environment. You can install the packages globally in your machine but it might result in some conflicts.

1. **Clone the Repository**

   ```bash
   git clone https://github.com/harmlessaccount/discord-docs/classifier
   cd classifier
   ```
2. **Create a Virtual Environment**
    ```bash
    python -m venv classifymon
    ```
3. **Activate the Virtual Environment**

   - **On Windows:**

     ```bash
     classifymon\Scripts\activate
     ```

   - **On macOS and Linux:**

     ```bash
     source classifymon/bin/activate
     ```
4. **Install dependencies**
   ```bash
   pip install requirements.txt
   ```

# Usage

1. Run the code
   ```bash
   python app.py
   ```
2. Your output should look like this
   ```
    * Serving Flask app '123'
    * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on all addresses (0.0.0.0)
    * Running on http://127.0.0.1:5001
    * Running on http://000.000.000:5001
    ```

# Speed test
You **need** aiohttp to achieve these speeds.

1. Non-cached images (aiohttp)
   ```bash
   Predicted Pokémon: Torkoal
   API response time: 0.3161 seconds
   ```
2. Cached images (aiohttp)
   ```bash
   Predicted Pokémon: Torkoal
   API response time: 0.0105 seconds
   ```

That is an over 30x speed increase on cached images. This does not takes into account downloading images.

# Cache

I made a basic cache implementation to help with recognition times. It just simply checks if the base64 encoded image has even been classified before. I have not made the cache persistant, take this example further for your needs.

# Notes

The accuracy of the classifier is NOT perfect. 
- You can check [results.json](https://github.com/harmlessaccount/discord-docs/classifier/results.json) to verify how the classifier performed with some NON-CACHED data scraped from PokéTwo. 
- You can check [results_cached.json](https://github.com/harmlessaccount/discord-docs/classifier/results_cached.json) to verify how the classifier performed with some CACHED data scraped from PokéTwo.
- [Access PokéTwo scraped data](https://github.com/SmartGuy09/Poketwo-Data/tree/main).
- [Read more](https://medium.com/@imjeffhi4/tutorial-using-vision-transformer-vit-to-create-a-pok%C3%A9mon-classifier-cb3f26ff2c20) about the model and a step-to-step guide on training it.
- [HugginFace model.](https://medium.com/@imjeffhi4/tutorial-using-vision-transformer-vit-to-create-a-pok%C3%A9mon-classifier-cb3f26ff2c20)
- [Test the model in your browser.](https://huggingface.co/spaces/TroglodyteDerivations/Pokemon_Classifier_Variant_5)
