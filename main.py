import discord
import re

def add_movie(name):
    movie_file = open("data/movies.txt", "a")
    movie_file.write(name + "\n")

def list_movies():
    movie_list = open("data/movies.txt","r").read()
    return movie_list

################################################
################################################
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg_content = message.content

    match = re.search(r"ch.add (.*)", msg_content)
    if match:
        movie = match.group(1)
        add_movie(movie)

        adding_msg = f"Adding movie {movie}..."
        await message.channel.send(adding_msg)

    #( Add list functionality )
    match = re.search(r"ch.list", msg_content)
    if match:
        await message.channel.send(list_movies())

client.run("TOKEN")
