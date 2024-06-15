import os
import discord
import re
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if(message.author.id == client.user.id):
            return
        
        #check if its twitter link
        twitterRe = r'https?:\/\/(www\.)?twitter\.com\/[A-Za-z0-9_]+\/status\/\d+'
        xRe = r'https?:\/\/(www\.)?x\.com\/[A-Za-z0-9_]+\/status\/\d+'
        tiktokAtRe = r'https?:\/\/(www\.)?tiktok\.com\/@[\w.-]+\/video\/\d+'
        tiktokTRe = r'https?:\/\/(www\.)?tiktok\.com\/t\/[A-Za-z0-9]+\/?'

        tMatch = re.match(twitterRe, message.content)
        xMatch = re.match(xRe, message.content)
        tt1Match = re.match(tiktokAtRe, message.content)
        tt2Match = re.match(tiktokTRe, message.content)


        linkType = ""

        if tMatch or xMatch:
            linkType = "twitter"
        elif tt1Match or tt2Match:
            linkType = "tiktok"
        
        if linkType != "":
            await message.edit(suppress = True)
            midx = message.content.find(".com")
            rMessage = message.content[midx:]
            rMessage = f"https://www.vx{linkType}" + rMessage
            print(rMessage)

            await message.reply(f"There's a {linkType} link, here's a better embed:\n" + rMessage)

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
