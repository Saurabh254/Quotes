import aiohttp
import asyncio
import time
import json


class Quote:
  async def fetch_json(self):
    async with aiohttp.ClientSession() as session:
      response = await session.get("http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
      rawJson = await response.text()
      jsonL = json.loads(rawJson)
      return jsonL
  def Text_Quotes(self,jsonL):
    Qtext = jsonL.get("quoteText")
    return Qtext
  def author_ofQuote(self,jsonL):
    author = jsonL.get("quoteAuthor")
    return author
def runner(quote):
  asyncio.run(quote.fetch_json())