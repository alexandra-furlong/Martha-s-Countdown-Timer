# import all the discord modules 
import discord
from discord.ext import commands
import os
import asyncio

# import datetime module.
import datetime
import time

# import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# import commands from the discord.ext module.
from discord.ext import commands

# loads the .env file that resides on the same level as the script.
load_dotenv()

# intialize discord token.
DISCORD_TOKEN = 'MTEwMjY5MzQyNjY3MzIyNTcyOQ.Gfbvft.xaUOdk3yA6ggKHVnKaQVed7iRwH1cSLyb3Jhs0'

# creates a new bot object with a specified prefix. it can be whatever you want it to be.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# HELP COMMAND 
class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s' % (self.context.clean_prefix, command.qualified_name)
        # return '%s%s %s' % (self.context.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", color=discord.Color.blurple())

        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort=True)
           command_signatures = [self.get_command_signature(c) for c in filtered]

           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "Martha Commands:")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

bot.help_command = MyHelp()

@bot.command()
async def marthaCountdown(ctx):
    # assigned regular string date => 2023-05-15 07:28:00 
    year   = 2023
    month  = 5
    day    = 15
    hour   = 7
    minute = 28

    # set the datetime 
    martha_time = datetime.datetime(year, month, day, hour, minute)

    # calculate the difference in time
    init_time = martha_time - datetime.datetime.now()
    
    # divmod(dividend, divisor) returns tuple containing the quotient & the remainder
    # divisor = 3600 because there 3600 seconds in 1 hour 
    init_hours, init_rem       = divmod(init_time.seconds, 3600)
    init_minutes, init_seconds = divmod(init_rem, 60)

    # check that delta_time is not negative
    if init_time < datetime.timedelta(0):
        await ctx.send(f"✿˖°. ˖°. It's time for martha to hop on Valorant !! ˖°. ˖°.✿")
    
    else:
        # display message with the starting countdown date and time
        msg = await ctx.send(f"martha's valorant comeback countdown: {init_time.days} days {init_hours} hours {init_minutes} minutes {init_seconds} seconds")
        
        while True:
            # delay 1 second
            await asyncio.sleep(1)
            
            # calculate the difference in time
            delta_time = martha_time - datetime.datetime.now()
            
            # divmod(dividend, divisor) returns tuple containing the quotient & the remainder
            # divisor = 3600 because there 3600 seconds in 1 hour 
            hours, rem       = divmod(delta_time.seconds, 3600)
            minutes, seconds = divmod(rem, 60)

            # if the countdown has ended, output the message! 
            if delta_time < datetime.timedelta(0):
                await ctx.send(f"✿˖°. ˖°. It's time for martha to hop on Valorant !! ˖°. ˖°.✿")
                break

            # otherwise continue counting down & editing the message with current time
            await msg.edit(content=f"martha's valorant comeback countdown: {delta_time.days} days {hours} hours {minutes} minutes {seconds} seconds")

# rank command
@bot.command()
async def marthaRank(ctx):
    await ctx.send("Martha is currently unranked, but her hidden MMR determines that she will place Radiant.") 

# bio command
@bot.command()
async def marthaBio(ctx):
    await ctx.send("Martha is NA's best Jett main. Originally signed with Sentinels, but felt bad for the mediocre pro player Tenz & instead gave him the position in 2021.") 

# executes the bot with the specified token. token has been removed and used just as an example.
bot.run(DISCORD_TOKEN)