
## First of all, refer to [this file](https://github.com/harmlessaccount/discord-docs/blob/main/classifier/CLASSIFY.md) to learn how to run the model.

# Get Pokémon name from image
1. **This will teach you:**

   - How to fetch message attachments
   - Host simple pre-trained models
   - How to use cache for optimization

# Automation Script

```python
#classifymon.py
from discord.ext import commands
import os
import aiohttp
import base64
from colorama import Fore, init
import random
import asyncio

# Initialize colorama
init(autoreset=True)

# Bot setup
bot = commands.Bot(command_prefix='>', self_bot=True)
downloadFolder = "pokepics" # Replace with whatever folder you'd like to put the pokémon images in.
TOKEN = ""  # Paste your token here

# Constants, do not change
KEYWORD = "Guess the pokémon"
poketwoId = 716390085896962058
pokemonList = ["growlith", "sandisle", "maltres", "kinghaskan", "pulpasaur", "kakizen"] # We will use those misspelled names as a placeholder for errors, thus reducing detection. Modify those names accordingly.

allowedChannels = [123, 123]  # Replace with your channel IDs

# Makes the folder if it does not exists.
if not os.path.exists(downloadFolder):
    os.makedirs(downloadFolder)

# Needed because API only takes base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')
    

@bot.listen('on_message')
async def on_message(message):
    # Check if the message is in an allowed channel
    if message.channel.id not in allowedChannels:
        return

    # Check if the message is from Pokétwo bot
    if message.author.id != poketwoId:
        return

    try:
        fetched_message = await message.channel.fetch_message(message.id)

        if not fetched_message.embeds:
            return

        for embed in fetched_message.embeds:
            description = embed.description
            if description and KEYWORD in description:
                # We download the image from embed.image.url
                if embed.image and embed.image.url:
                    image_url = embed.image.url
                    fileName = os.path.join(downloadFolder, "pokemon.jpg")
                    await download_file(image_url, fileName)
                    
                    image_base64 = image_to_base64(fileName)
                    prediction = await classify(image_base64)
                    
                    if prediction:
                        # Random delay between 1 and 5 seconds (you can adjust the range)
                        delay = random.uniform(1, 5)
                        await asyncio.sleep(delay)

                        # Send the message with prediction
                        await message.channel.send(f"<@{poketwoId}> c {prediction.lower()}")
                        print(f"{Fore.GREEN}Predicted Pokémon: {prediction.lower()} | Channel ID: {message.channel.id}")

    except Exception as e:
        print(f"{Fore.RED}Error: {e}")

    await bot.process_commands(message)

async def download_file(url, file_path):
    # API request to Discord CDN to retrieve files
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(file_path, 'wb') as f:
                    f.write(await response.read())
                return
            else:
                print(f"{Fore.RED}Failed to download file from {url}")
                return

async def classify(image_base64):
    url = 'http://localhost:5001/classify'
    headers = {'Content-Type': 'application/json'}
    json_data = {'image': image_base64}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=json_data, headers=headers) as response:
                status = response.status
                if status == 200:
                    data = await response.json()
                    return data.get('pokemon', random.choice(pokemonList))
                else:
                    print(f"{Fore.RED}Prediction request failed with status: {status}")
                    return random.choice(pokemonList)
    except Exception as e:
        print(f"{Fore.RED}Exception occurred during classification: {e}")
        return random.choice(pokemonList)

bot.run(TOKEN)
```

The code works. The output should be something like:

```python
Predicted Pokémon: sandile | Channel ID: 111111111111111111
Predicted Pokémon: growlithe | Channel ID: 11111111111111111
Predicted Pokémon: mewtwo | Channel ID: 11111111111111111
```

The code is not complete for undetection or exceptions. That's for you to implement, this should already build a strong base for your catcher.