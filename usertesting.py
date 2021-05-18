import requests
from bs4 import BeautifulSoup
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events

count=0
data = requests.get("https://app.usertesting.com/my_dashboard/available_tests_v3", headers={'Host': 'app.usertesting.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Cookie':  '_session_id=5a126e1a04c64a6358edb46db92ecf9d'})

soup = BeautifulSoup(data.text, 'html.parser')
for title in soup.find_all('title'):
	if (count==0):
		print("Title is : ", title.get_text())
		count+=1

# get your api_id, api_hash, token
# from telegram as described above
api_id = '2582501'
api_hash = '3afab6e42e73d02ccd80ed039d08e216'
token = '1720638274:AAGP5nLOgb2ETFBTevpzv2eMjPB-KoHoav4'
  
# your phone number
phone = '919447457207'
   
# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)
   
# connecting and building the session
client.connect()
  
# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id 
if not client.is_user_authorized():
   client.send_code_request(phone)  
    # signing in the client
   client.sign_in(phone, input('Enter the code: '))
   myself = client.get_me()
   print(myself)
try:
    # receiver user_id and access_hash, use
    # my user_id and access_hash for reference
   receiver = InputPeerUser(int('625309381'), int('5937154808433052345'))
   message = "Test Received!"
    # sending message using telegram client
   client.send_message(receiver, message, parse_mode='html')
except Exception as e:
      
    # there may be many error coming in while like peer
    # error, wwrong access_hash, flood_error, etc
    print(e);
  
# disconnecting the telegram session 
client.disconnect()
