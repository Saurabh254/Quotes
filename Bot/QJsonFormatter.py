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
      jsonL = json.loads(rawJson)
    return jsonL