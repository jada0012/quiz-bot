import discord
from discord.ext import commands
import config
from dictionary_create import country_capitals_dict
import random

intents = discord.Intents.default()
intents.members = True



client = commands.Bot(command_prefix=',', intents=intents)

@client.event
async def on_ready():
    print("hasn't broken yet")




@client.command()
async def capital(ctx, num=1):
    for i in range(num):
    
        cnt = random.choice(list(country_capitals_dict.keys()))
        
        await ctx.send(f"what is the capital of {cnt}")
        msg = await client.wait_for('message')
        if msg.content.capitalize() == country_capitals_dict[cnt]:
            await ctx.send('correct!!')
        else: 
            await ctx.send(f"wrong, it's actually {country_capitals_dict[cnt]} ")



    

client.run(config.TOKEN)