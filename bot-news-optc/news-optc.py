from cgitb import text
from email.mime import image
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import datetime
from urlextract import URLExtract
import re 
import time
from datetime import tzinfo, timedelta, datetime
from datetime import datetime
from pytz import timezone
import discord
from discord.ext import commands

token = 'OTg1MTU5Nzk5NjM1MzEyNzAw.GE-wN5.emU7N_OJPYjG0n03gQkpg2y-V4IhY2zxZWc16I'
bot = commands.Bot(command_prefix='!')



@bot.command()
async def news(ctx):
    await ctx.send('bot now active')
    while news:
        url = 'https://news.onepiece-tc.jp/news/html/onepiece-tc-news.html'
        r = requests.get(url)
        soupe = BeautifulSoup(r.content,'html.parser')
        for datee in soupe.find('ul',attrs={'id':'info_box'}):
            format = "%m/%d(%H:%M)"
            # Current time in UTC
            now_utc = datetime.now(timezone('UTC'))
            # Convert to Asia/Kolkata time zone
            now_asia = now_utc.astimezone(timezone('Asia/Tokyo'))
            finish = now_asia.strftime(format)
            current_date_japan = finish
            if current_date_japan in datee.text:
                embed = discord.Embed(title='NEW EVENT ON JP ',url="https://news.onepiece-tc.jp/news/html/onepiece-tc-news.html",description=current_date_japan, color=0x00ff)
                imaging = datee.find('font',attrs={'class':'col_1'})
                for img in imaging.find_all('img', src=True):
                    embed.set_image(url= img['src'])
                    await ctx.send(embed= embed)
                time.sleep(60)
                bot.command((news))
            else:
                bot.command((news))

bot.run(token)
   

