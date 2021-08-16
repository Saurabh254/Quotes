from discord.ext import commands
import discord
import os 
from dotenv import load_dotenv
from embeds import Embeds

load_dotenv()
token = os.getenv("TOKEN")

client = discord.Client()
worker = Embeds()
@client.event
async def on_ready():
  print("The bot is ready by user {}".format(client))
@client.event
async def on_message(message):
  if message.content.startswith("up!help"):
    help_text = worker._help()
    await message.channel.send(embed=help_text)
    
    
client.run(token)