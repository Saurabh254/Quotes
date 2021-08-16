from discord.ext import commands
import discord
import os 
import time
from dotenv import load_dotenv
from embeds import Embeds
from QJsonFormatter import _Quotes_
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
    latency = round(client.latency * 100)
    await message.channel.send(embed=worker.ping(latency))
  if message.content.startswith("up!quote"):
    quote =  _Quotes_()
    jsonL = quote._response_()
    text_quote = quote.Json_quote(jsonL)
    author = quote.author_ofQuote(jsonL)
    await message.channel.send(embed=worker._quote_(text_quote, author))
  if message.content.startswith("up!start"):
    while True:
      quote =  _Quotes_()
      jsonL = quote._response_()
      text_quote = quote.Json_quote(jsonL)
      author = quote.author_ofQuote(jsonL)
      time.sleep(10)
      await message.channel.send(embed=worker.loop_quote_(text_quote, author))
    
    
client.run(token)