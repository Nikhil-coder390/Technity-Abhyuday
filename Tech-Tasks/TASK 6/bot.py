import os
import telebot
import requests
import json
import csv
from csv import DictWriter

# TODO: 1.1 Get your environment variables
yourkey = os.getenv('b1329187') # Use the name of the environment variable
bot_id  = os.getenv('BOT_TOKEN') # Use the name of the environment variable


bot = telebot.TeleBot('5781498130:AAE_VHLRpBISQIFQR5UULgVkVnC-ZOHaFFM')

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')

@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')



@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    global botRunning
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')

csv_file = None
botRunning = True

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):

    bot.reply_to(message, 'Getting movie info...')
    movie_name = message.text.split()[1]
    response = requests.get(f"http://www.omdbapi.com/?apikey=b1329187&t={movie_name}")
    data = response.json()

    # Check if the data response is successful
    if data['Response'] == 'True':
        # Assign the poster link to the variable poster
        poster = data['Poster']
        title = data['Title']
        year = data['Year']
        genre = data['Genre']
        plot = data['Plot']
        imdb_rating = data['imdbRating']

        info = f"Poster: {poster}\n\n"
        info += f"Title: {title}.\n"
        info += f"Year: {year}.\n"
        info += f"Genre: {genre}.\n"
        info += f"Plot: {plot}.\n"
        info += f"IMDb rating: {imdb_rating} / 10.\n"

        bot.reply_to(message, info, parse_mode='Markdown')

        # Use the global keyword to access the global variable csv_file
        global csv_file
        global csv_writer

        if not csv_file:
            csv_file = open('movie_data.csv', 'w')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Poster','Title', 'Year', 'Genre', 'Plot', 'IMDb Rating'])
            csv_writer.writerow([poster,title, year, genre, plot, imdb_rating])
    else:
        # Handle the case when the data response is not successful
        bot.reply_to(message, f"Sorry, I could not find any information about {movie_name}.")


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    global botRunning
    bot.reply_to(message, 'Generating file...')
    # Use the global keyword to access the global variable csv_file
    global csv_file

    if csv_file:
        csv_file.close()
        doc = open('movie_data.csv', 'rb')
        bot.send_document(message.chat.id, doc)

    else:
        bot.reply_to(message, 'Sorry, there is no data to export.')


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

bot.polling(none_stop=True)
