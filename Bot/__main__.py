from discord.ext import commands, tasks
import discord
import os 
import time
from dotenv import load_dotenv
from embeds import Embeds
from QJsonFormatter import _Quotes_
import asyncio
#Token load
load_dotenv()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="up!")
worker = Embeds()
@bot.event
async def on_ready():
  print("The bot is ready by user {}".format(bot))
  activity = discord.Game(name="Quote", type=3)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Quotes API"))



@bot.command(name="start")
async def start(ctx,time, args):
  global quoter_send
  await ctx.send(embed=worker.loop_started())
  @tasks.loop(seconds=(int(time)))
  async def quoter_send():
    quote =  _Quotes_()
    jsonL = quote._response_()
    text_quote = quote.Json_quote(jsonL)
    author = quote.author_ofQuote(jsonL)
    print("tasks running successfully")
    print(f"Now waiting for {time}")
    channel = bot.get_channel(int(args))
    await channel.send(embed=worker.loop_quote_(text_quote, author))
  quoter_send.start()

@bot.command(name="stop")
async def stop(ctx):
  quoter_send.cancel()
  print("User used stop command")
  await ctx.send(embed=worker.on_stop())
    
@bot.command(name="developer")
async def developer(ctx):
  print("user used developer commad")
  await ctx.send(embed=worker.developer())

@bot.command(name="ping")
async def ping(ctx):
  print("User used ping command")
  latency = round(bot.latency * 1000)
  await ctx.send(embed=worker.ping(latency))
    
@bot.command(name="invite")
async def _invite(ctx):
  print("user used invite command")
  await ctx.send(embed=worker._invite_())
  
bot.remove_command('help')
@bot.command(name="help")
async def Qhelp_(ctx):
  print("user used help command")
  await ctx.send(embed=worker._help())
    
@bot.command(name="quote")
async def quote(ctx):
  try:  
    quote =  _Quotes_()
    jsonL = quote._response_()
    text_quote = quote.Json_quote(jsonL)
    author = quote.author_ofQuote(jsonL)
    await ctx.send(embed=worker._quote_(text_quote, author))
    print("worked successfully")
  except:
    await ctx.send(embed=worker.Json_error())
    print(f"Got an Json error")

bot.run(token)


