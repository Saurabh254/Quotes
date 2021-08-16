import discord

class Embeds:
  def ping(self,latency):
    embedVar = discord.Embed(title="Pong!", description=f"💚 {latency}ms", color=0x00ff00)
    return embedVar
   
  def _help(self):
    embedVar = discord.Embed(title="Quotes Bot Commands", description="Use prefix: up!", color=0x00ff00)
    embedVar.add_field(name="start", value="start Quotes bot on this particular channel", inline=False)
    embedVar.add_field(name="quote", value="Show a random Quote", inline=False)
    embedVar.add_field(name="ping", value="Show bot latency", inline=False)
    embedVar.add_field(name="developer", value="Show developer of this bot", inline=False)
    embedVar.add_field(name="stop", value="Stop this bot from sending Quotes", inline=False)
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/emojis/876529388227813407.png?v=1&size=64")
    return embedVar
    
  def developer(self):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/emojis/876529388227813407.png?v=1&size=64")
    return embedVar
    
  def _quote_(self, text, author):
    embedVar = discord.Embed(title="Daily Quotes", description=text, color=0x00ff00)
    embedVar.set_footer(text=f"Quote by {0}".format(author))
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/emojis/876529388227813407.png?v=1&size=64")
    return embedVar
  