from discord.ext import commands
import discord
import os 
from dotenv import load_dotenv
import embeds

client = discord.Client()
worker = Embeds()
@client.event
async def on_ready():
  print("The bot is ready by user {}".format(client))
@client.event
async def on_message(message):
  if message.content.startswith("up!quote"):