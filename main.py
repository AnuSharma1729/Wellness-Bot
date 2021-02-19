import os
import random
import Methods.negative_patterns as np
from keep_alive import keep_alive
from dotenv import load_dotenv
from googlemaps import Client
from replit import db
from datetime import datetime
import json

import requests

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} is here for you!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if np.contains_depression_traces(message.content.lower()):
        response = np.get_depression_response()
        await message.channel.send(response)
    if np.contains_school_traces(message.content.lower()):
        await message.channel.send("What topic?")
    if np.contains_schooltopic_traces(message.content.lower()):
        await message.channel.send(
            'Based on your request, here\'s what I found: https://www.khanacademy.org/math/trigonometry%27'
        )
    if np.contains_jobfinding_traces(message.content.lower()):
        await message.channel.send(
            "What kind of job are you looking for? What kind of salary? How far from you?"
        )
    if np.contains_jobarea_traces(message.content.lower()):
        await message.channel.send(
            "Hope this helps: https://careers.google.com/jobs/results/")
    if np.contains_jobmanage_traces(message.content.lower()):
        await message.channel.send(
            "Here are some helpful resources: https://basecamp.com/%22")
    if np.contains_relationship_traces(message.content.lower()):
        await message.channel.send(
            "Relationships are complicated but very precious. I might not be able to understand how you are feeling right now but I have a place for you to talk it out: https://discord.gg/9g98gZ9H%22"
        )
    if np.contains_stress_traces(message.content.lower()):
        response = np.get_stress_response()
        await message.channel.send(response)
    await bot.process_commands(message)


@bot.command(name='exercise', help='Activities to get your mind off of things')
async def offer_exercise(ctx):

    exercises = [
        'Go for a walk! https://media.giphy.com/media/omHPYZttAVAAw/giphy.gif ',
        "How about a run? Don't forget to warm up! https://media.giphy.com/media/3oKIPavRPgJYaNI97W/giphy.gif ",
        'Stand up, walk around, and streeeeetch! https://media.giphy.com/media/8mvV5eUXkM18iCm5Eg/giphy.gif ',
        'Try some yoga! https://media.giphy.com/media/H3SYd8rWzFXQrAWLNc/giphy.gif ',
        'Get some fresh air but don\'t forget your mask https://tenor.com/bgdjG.gif',
        'Try some pushups. Down, up 1! https://media.giphy.com/media/3ohhwElB92YQv0igda/giphy.gif ',
        'Get up and do some jumping jacks https://cdn.lowgif.com/full/65353ed76bf13aa5-digital-icon-pack-clock-gif-by-seth-eckert-motion.gif'
    ]
    response = random.choice(exercises)
    await ctx.send(response)


@bot.command(
    name='findMuseums',
    help='Find local museums to visit! Invoke !findMuseums <location name>')
async def offer_park(ctx, *locations):
    location = ""
    for place in locations:
        location = location + place
    gmaps = Client('AIzaSyA0QJJKbsee6MVN7DAiVSeTUOV2F-V0rRs')
    latitude = gmaps.geocode(location)[0]['geometry']['location']['lat']
    longitude = gmaps.geocode(location)[0]['geometry']['location']['lng']
    results = findPlaces(latitude, longitude, "museum")
    MAX_RESULTS = 5
    curr_result = 0
    for result in results:
        if curr_result == MAX_RESULTS:
            return
        message = str(curr_result + 1) + ". Name: " + result[
            'name'] + "\n\tLocation: " + result['vicinity']
        await ctx.send(message)
        curr_result = curr_result + 1


@bot.command(
    name='findParks',
    help='Find some greenery near you! Invoke !findParks <location name>')
async def offer_park(ctx, *locations):
    location = ""
    for place in locations:
        location = location + place
    gmaps = Client('AIzaSyA0QJJKbsee6MVN7DAiVSeTUOV2F-V0rRs')
    latitude = gmaps.geocode(location)[0]['geometry']['location']['lat']
    longitude = gmaps.geocode(location)[0]['geometry']['location']['lng']
    results = findPlaces(latitude, longitude, "park")
    MAX_RESULTS = 5
    curr_result = 0
    for result in results:
        if curr_result == MAX_RESULTS:
            return
        message = str(curr_result + 1) + ". Name: " + result[
            'name'] + "\n\tLocation: " + result['vicinity']
        await ctx.send(message)
        curr_result = curr_result + 1


def findPlaces(lat, lng, tag, radius=4000, pagetoken=None):
    type = tag
    APIKEY = 'AIzaSyA0QJJKbsee6MVN7DAiVSeTUOV2F-V0rRs'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&type={type}&key={APIKEY}{pagetoken}".format(
        lat=lat,
        lng=lng,
        radius=radius,
        type=type,
        APIKEY=APIKEY,
        pagetoken="&pagetoken=" + pagetoken if pagetoken else "")
    print(url)
    response = requests.get(url)
    res = json.loads(response.text)
    # print(res)
    print("here results ---->>> ", len(res["results"]))
    return res["results"]


@bot.command(name='compliment',
             help="Feeling down? It\'s totally okay,  Type !compliment")
async def offer_park(ctx):
    compliments = [
        'You have never been more perfect.',
        'Who\'s the boss? You\'re the boss.',
        'You are the smartest person I know.', 'WOW! You look great today.',
        'You have the best smile.', 'You light up the whole server.',
        'You are more fun than bubble wrap'
    ]
    response = random.choice(compliments)
    await ctx.send(response)
    await message.author.send(response)


keep_alive()
bot.run(TOKEN)