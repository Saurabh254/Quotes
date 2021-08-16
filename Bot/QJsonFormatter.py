import aiohttp
import asyncio
import time
import json

url = "http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en"

class Quote:
  async def __init__(self):
    async with aiohttp.ClientSession() as session:
      response = await session.get(url)
      rawJson = await response.text()
      self.jsonL = json.loads(rawJson)
  def Text_Quotes(self):
    Qtext = self.json.get("quoteText")
    return Qtext
  def author_ofQuote(self):
    author = self.json.get("quoteAuthor")
    return author