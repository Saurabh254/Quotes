from discord.ext import commands
import discord
import os 
from dotenv import load_dotenv
from embeds import Embeds
from QJsonFormatter import Quote, runner
import asyncio

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
  if message.content.startswith("up!ping"):
    latency = round(client.latency * 1000)
    await message.channel.send(embed=worker.ping(latency))
  if message.content.startswith("up!quote"):
    quote = Quote()
    jsonL =  runner(quote)
    q_text = quote.Text_Quotes(jsonL)
    author = quote.author_ofQuote(jsonL)
    await message.channel.send(embed=worker._quote_(q_text, author))
    
client.run(token)