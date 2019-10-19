import pyowm
import telebot

owm = pyowm.OWM('528753763b150c1496e0bda79b14c834', language = "ru")
bot = telebot.TeleBot('907303916:AAHNP_XsMoOCi8ekCYSzNNJ6TtVtEvhHKlw')

#
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты начал работу со мной. Напиши город, если хочешь узнать погоду')
#


@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = " В городе " + message.text + " сейчас: " + w.get_detailed_status() + "\n"
	answer += " температура сейчас: " + str(temp) + "\n\n"

	if (temp) < 10:
	    answer += " холодно, сиди дома) "
	elif (temp) < 20:
	    answer += " нормально, можно гулять "
	else:
	    answer += " тепло, пора ехать на море "

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)
