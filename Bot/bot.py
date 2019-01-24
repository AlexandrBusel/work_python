import requests

import misc
from nbrb import get_rate_today_usd
from nbrb import get_rate_today_rub
# from nbrb import get_rate_date
from nbrb import text_code

from time import sleep


token = misc.token


URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0




def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()

def get_message():

	data = get_updates()
	last_object = data['result'][-1]

	update_id = last_object['update_id']

	global last_update_id
	if last_update_id != update_id:
		last_update_id = update_id

		chat_id = last_object['message']['chat']['id']
		message_text = last_object['message']['text']

		message = {'chat_id': chat_id,
					'text': message_text}
		return message	
	return None			




def send_message(chat_id, text='Wait a second, please...'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
	
	requests.get(url)



def main():
	
	while True:
		answer = get_message()

		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']
			
			# if type(text) == type ('int'):
			# 		# if(type('text')==types.IntType):		
			# 		# if type('text') == type ('int'):
			# 	send_message(chat_id, text_code())
			# else:
				# if type('text') == type ('str'):
			if text == 'usd':
				send_message(chat_id, get_rate_today_usd())
							
			if text == 'rub':
				send_message(chat_id, get_rate_today_rub())

			if type('text') != [type ('str')]:			
				send_message(chat_id, text_code())

			# if text == 'usd_date':
			# 	send_message(chat_id, get_rate_date())
			# if text == 'Что я писал 5 сообщений назад':
			# 	send_message(chat_id, send_last_message())
			if text == 'что я писал пять сообщений назад?':
				last_object = get_updates()['result'][-6]['message']['text']
				send_message(chat_id, last_object)

		else:
			continue

		sleep(2) 			


if __name__ == '__main__':
	main()







	