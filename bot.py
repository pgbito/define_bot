import discord
client = discord.Client(intents=discord.Intents.all())
from dotenv import dotenv.dotenv_values()

import requests


def cut(ms):
    ## Used for cut strings
    fs = list()
    i = str()
    for char in ms:
        if len(i) >= 1995:
            i += char
            fs.append(i)
            i = str()
        else:
            i += char
    fs.append(i)
    print(fs)
    return fs

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
selfbot=True


headers = {
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com",
	"X-RapidAPI-Key": "a8ba08bfa0msh205b4f313d75453p105ddajsnc3b8b8d008dd"
}
example_info ={"list":[
    {"definition":"Grizzway is the most [ultimate chad] on all of [shitpost]. Every man and woman has a fat crush on him and wishes they were him. He produces [sick beats], is handsome as fuck, is a great cook, and is the future owner of shitpost.","permalink":"http://grizzway.urbanup.com/14401794","thumbs_up":6,"sound_urls":[],"author":"Meme king","word":"Grizzway","defid":14401794,"current_vote":"","written_on":"2019-11-06T18:25:16.771Z","example":"Milo: OMG [grizzway] is so hot I wish he would love me as much as I love him\r\nKobi: [Frig off] milo, [grizzy] is mine","thumbs_down":18}]}
@client.event
async def on_message(message: discord.Message):
    if selfbot:
     async for fixed_message in message.channel.history(limit=1):
        message=fixed_message

    if message.content.startswith('>define'):
        response = requests.request("GET", url, headers=headers, params={"term": ' '.join(message.content.split(' ')[1:])})
        if response.ok:
            if selfbot:
                # NOT EMBED REPLY
                 response = response.json()['list'][0]
                 for paragraph in cut(response['definition']):
                   await message.reply(content=paragraph)
                 return
            response = response.json()['list'][0]
            for paragraph in cut(response['definition']):
                embed = discord.Embed()

                embed.description = paragraph
                embed.color = discord.Colour.orange()
                embed.set_author(name=response['word'],url=response['permalink'] )
                embed.add_field('Example',response['example'])
        




token ='e'

client.run(token,bot=(not selfbot))
