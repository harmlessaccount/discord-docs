# First bot (Python)

Let's create our first bot using [discord.py-self](https://github.com/dolfies/discord.py-self).

`pip install discord.py-self`

Then, make a file, name it whatever you like (make sure it's not named something like discord.py)

    #selfbot.py
    import discord
    from discord.ext import commands
    bot = commands.Bot(command_prefix='>', self_bot=True)
    TOKEN = "" #Paste your account token here
    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')
    
    bot.run(TOKEN)
    import discord
    from discord.ext import commands
    bot = commands.Bot(command_prefix='>', self_bot=True)
    TOKEN = "" #Paste your account token here
    u/bot.command()
    async def ping(ctx):
        await ctx.send('pong')
    
    bot.run(TOKEN)

Great, if it worked, the output should be something like this:

`> python "selfbot.py"`

`2024-08-25 00:00:00 INFO discord.client Logging in using static token.`

`2024-08-25 00:00 :00 INFO discord.http Found user agent Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36, build number 999999.`

Then, simply go on Discord and type ">ping" anywhere, and your own account should send a response, "pong".
