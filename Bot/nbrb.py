import requests

bot_token = '788479435:AAE1sn3Sw7t_9h-8dMC0oA2YabMqp6AH-QA'
tel_api_url = "https://api.telegram.org.bot{}/"

methods = {'updates': 'GetUpdates'}

def get_rate_today_usd():
	
	usd = 'http://www.nbrb.by/API/ExRates/Rates/145'
	
	response = requests.get(usd).json()
	
	# price = response['Cur_ID']
	return str(response)

def get_rate_today_rub():
	
	rub = 'http://www.nbrb.by/API/ExRates/Rates/298'
	
	response = requests.get(rub).json()
	# price = response['Cur_ID']
	return str(response)

def  text_code():
	return "Вы ввели информацию неверного типа, введите код валюты!"	

# def get_rate_date():
	# date = input('Введите дату:')
	# while date != None:
		
	# 	url = 'http://www.nbrb.by/API/ExRates/Rates/145?{}'.format(date)

		# response = requests.get(url).json()
	# return str(response)


	








# def get_rate_date():
#     url = 'http://www.nbrb.by/API/ExRates/Rates/145?onDate=2016-5-7'
#     response=requests.get(url).json()
#     price=response['Cur_OfficialRate']
#     return str(price)+' курс USD на 2016-05-07 '