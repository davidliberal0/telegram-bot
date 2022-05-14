import os
import telebot

# For API Functions and Requests
import random
import requests 
import json

API_KEY = os.getenv('API_KEY') # obtaining the key in the .env (environment)
bot = telebot.TeleBot(API_KEY) # accesses and creates the bot using the API key 

# Help and Start Message 
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! I am DavidWTBot. \n I am here to help you know all about David, World Tour!")

@bot.message_handler(commands=['Hello'])
def greet(message):
    bot.send_message(message.chat.id, "Hey! Hows it going?")

@bot.message_handler(commands=['weather'])
def today(message):
    json_data = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Orlando&appid=3199c00e2910515dab56aee19546a741').json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    weather = f"Condition: {condition} \n Temperature: {str(temp)} °C \n Humidity: {str(humidity)} \n Wind Speed: {str(wind)} \n"

    bot.send_message(message.chat.id, weather)

@bot.message_handler(commands=['joke'])
def joke(message):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    json_data = json.loads(response.text)
    joke = json_data['setup'] + ' --> ' + json_data['punchline']
    bot.send_message(message.chat.id, joke)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
    
    if "wassup" in message.text.lower():
        bot.send_message(message.chat.id, "Whats good bro!")
    elif "are you" and "how" in message.text.lower():
        bot.send_message(message.chat.id, "Im doing great!")
    elif message.text == "When is his birthday?":
        birth_year = 2001
        age = str(2021 - birth_year)
        bot.send_message(message.chat.id, f"David's birthday is October 22, 2001. Currently, David is {age} years old")
    elif message.text == "interests?":
        bot.send_message(message.chat.id, "David's interests are EVERYTHING!")
    else:
        bot.send_message(message.chat.id, "Yeah man")


bot.polling()