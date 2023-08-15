import datetime
import pytz

integer = {"01":"1110001 1010001 1010001 1010001 1110001", "02":"1110111 1010001 1010111 1010100 1110111", "03":"1110111 1010001 1010111 1010001 1110111", "04":"1110101 1010101 1010111 1010001 1110001", "05":"1110111 1010100 1010111 1010001 1110111"}

#timrzone = ['Europe/Paris', 'Africa/Kampala', 'Asia/Colombo', 'Asia/Riyadh', 'Africa/Luanda', 'Europe/Vienna', 'Asia/Calcutta', 'Asia/Dubai','Europe/London']

tz = pytz.timezone('Europe/Berlin') # Zeitzone Berlin
berlin_now = datetime.datetime.now(tz) # aktuelle Zeit in Berlin
m = berlin_now.strftime("%M") # Minuten
h = berlin_now.strftime("%H") # Stunden

