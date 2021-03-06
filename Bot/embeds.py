import discord

class Embeds:
  def ping(self,latency):
    embedVar = discord.Embed(title="Pong!", description=f"Latency: 💚 {latency}ms", color=0x00ff00)
    return embedVar
   
  def _help(self):
    embedVar = discord.Embed(title="Quotes Bot Commands", description="Use prefix: up!", color=0x00ff00)
    embedVar.add_field(name="start", value="Start sending Quotes on a particular channel at a specific time.\nCommand format:\n`up!start [time(seconds)] [channelid]`\nExample:\n`up!start 1000 875207122370048072`", inline=False)
    embedVar.add_field(name="quote", value="Show a random Quote", inline=False)
    embedVar.add_field(name="ping", value="Show bot latency", inline=False)
    embedVar.add_field(name="developer", value="Show developer of this bot", inline=False)
    embedVar.add_field(name="stop", value="Stop this bot from sending Quotes", inline=False)
    embedVar.add_field(name="invite", value="Invite this bot to your server", inline=False)
    embedVar.set_thumbnail(url="https://cdn.discordapp.com/emojis/876529388227813407.png?v=1&size=64")
    embedVar.set_footer(text="Powered by Quotes API")
    return embedVar
    
  def developer(self):
    embedVar = discord.Embed(title="Quotes Bot", description="Developed by:\nSaurabh Vishwakarma", color=0x00ff00)
    embedVar.add_field(name="Developer's Github", value = "Click [here](https://www.github.com/Saurabh-Vishwakarm)")
    return embedVar
    
  def _invite_(self):
    embedVar = discord.Embed(title="Quotes Bot", description="Add Quotes Bot to your server\nClick [here](https://discord.com/oauth2/authorize?client_id=867422533622956063&permissions=8&scope=bot)", color=0x00ff00)
    embedVar.set_footer(text="Powered by Quotes API")
    return embedVar
    
  def _quote_(self, text, author):
    embedVar = discord.Embed(title="Quote", description=text, color=0x000ff00)
    embedVar.set_footer(text=f"Quote by {author}")
    return embedVar
    
  def loop_quote_(self, text, author):
    embedVar = discord.Embed(title="Daily Quote", description=text, color=0x000ff00)
    embedVar.set_footer(text=f"Quote by {author}")
    return embedVar

  def loop_started(self):
    embedVar = discord.Embed(title="Quotes Bot", description="Quote bot is successfully activated", color=0x000ff00)
    embedVar.set_footer(text="Powered by Quotes API")
    return embedVar

  def on_stop(self):
    embedVar = discord.Embed(title="Quote Bot", description="Service stopped", color=0x000ff00)
    embedVar.set_footer(text=f"Powered by Quotes API")
    return embedVar
  def Json_error(self):
    embedVar = discord.Embed(title="Quote Bot", description="Webpage not responding, Try again", color=0x000ff00)
    embedVar.set_footer(text=f"Powered by Quote API")
    return embedVar