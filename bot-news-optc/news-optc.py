from timeit import repeat
import requests
from bs4 import BeautifulSoup
import datetime
import time
from datetime import tzinfo, timedelta, datetime
from datetime import datetime
from pytz import timezone
import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv


bot = commands.Bot(command_prefix='!')
load_dotenv(dotenv_path="config")


@bot.command()
async def news(ctx):
        await ctx.send('bot now active')
        while True:
            url = 'https://news.onepiece-tc.jp/news/html/onepiece-tc-news.html'
            r = requests.get(url)
            soupe = BeautifulSoup(r.content,'html.parser')
            for datee in soupe.find('ul',attrs={'id':'info_box'}):
                format = "%Y-%m-%d"
                now_utc = datetime.now()
                finish = now_utc.strftime(format)
                current_date_japan2 = finish
                if current_date_japan2 in datee.text:
                    embed = discord.Embed(title='NEW EVENT ON JP ',url="https://news.onepiece-tc.jp/news/html/onepiece-tc-news.html",description=current_date_japan2, color=0x00ff)
                    imaging = datee.find('font',attrs={'class':'col_1'})
                    for img in imaging.find_all('img', src=True):
                        embed.set_image(url= img['src'])
                        await ctx.send(embed= embed)
            time.sleep(86400)

bot.run('OTg1MTU5Nzk5NjM1MzEyNzAw.GfuDfb.RBRpAyDxORX3iZlxJ8_qHqxzqEstiRrXCTXjpQ')


