# Pressing buttons

If you have tried modern bots, you would see that they include various components like buttons, modals, and menus. These are called component interactions and were introduced around two years ago. They are however, quite undocumented and confusing at times. Let's learn how to press buttons.

Firstly, if we fetch a message with buttons, and try to print its components using `message.components` we'll get something like this:

```<ActionRow children=[<Button style=<ButtonStyle.secondary: 2> custom_id='ACTION1' url=None disabled=False label=None emoji=<PartialEmoji animated=False name='🔲' id=None>>, <Button style=<ButtonStyle.secondary: 2> custom_id='ACTION2' url=None disabled=False label=None emoji=<PartialEmoji animated=False name='🔳' id=None>>, <Button style=<ButtonStyle.secondary: 2> custom_id='ACTION3' url=None disabled=True label=None emoji=<PartialEmoji animated=False name='🔵' id=None>>, <Button style=<ButtonStyle.secondary: 2> custom_id='ACTION4' url=None disabled=False label=None emoji=<PartialEmoji animated=False name='🔶' id=None>>, <Button style=<ButtonStyle.secondary: 2> custom_id='ACTION5' url=None disabled=True label=None emoji=<PartialEmoji animated=False name='🔷' id=None>>]>   ```

This represents buttons, and is what `button.click()` takes to function. Let's see some example code.

```
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", self_bot = True)

TOKEN = "" # Paste your USER token inside the quotes
@bot.command() # Usage !click messageId buttonIndex
async def click(ctx: commands.Context, messageId: int, buttonIndex: int):
    channel = ctx.channel
    try:
        message = await channel.fetch_message(messageId) # Fetch the message by ID
        if message and message.components: 
            print(message.components) # Checks if there is any buttons on the message
            buttons = message.components[0].children # Gets the list of buttons
            print(buttons)
            if 0 <= buttonIndex < len(buttons): # Avoids inputting a button not in the list
                button = buttons[buttonIndex]
                await button.click()
                await ctx.send(f"Clicked button {buttonIndex}.")
            else:
                await ctx.send("Invalid button index.")
        else:
            await ctx.send("Message has no buttons.")
    except discord.NotFound:
        await ctx.send("Message not found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(TOKEN)
```

If this worked, you should be able to run the `!click` command and properly press buttons on-demand. You can take this example further easily, letting you fully automate most modern bots.
