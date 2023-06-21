import discord
import re

def add_movie(name):
    movie_file = open("data/movies.txt", "a")
    movie_file.write(name + "\n")

def list_movies(list_movie):
    movie_list = open(list_movie,"r").read()
    return movie_list

def seen_movie(movie):
    movie_list = open("data/movies.txt","r")
    movie_line = movie_list.readline()

    new_movie_list = ""
    found_movie = False

    while movie_line:
        if movie_line.find(movie) == -1:
            new_movie_list += movie_line
        elif not movie_line.find(movie):
            found_movie = True
        movie_line = movie_list.readline()

    if found_movie:
        movie_list = open("data/movies.txt", "w")
        movie_list.write(new_movie_list)

        movie_list = open("data/movies_seen.txt", "a")
        movie_list.write(movie + "\n")

    return found_movie


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

        await message.add_reaction("👌")

    match = re.search(r"ch.list(.*)", msg_content)
    if match:
        extra_param = match.group(1)
        if extra_param == " seen":
            await message.channel.send(list_movies("data/movies_seen.txt"))
        else:
            await message.channel.send(list_movies("data/movies.txt"))

    match = re.search(r"ch.seen (.*)", msg_content)
    if match:
        movie = match.group(1)
        could_seen = seen_movie(movie)

        if could_seen:
            await message.add_reaction("👌")
        else:
            await message.add_reaction("❌")

client.run("")
