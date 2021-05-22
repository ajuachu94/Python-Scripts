import requests
from bs4 import BeautifulSoup
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import time

count=0
headers={'Host': 'app.usertesting.com', 'Cookie':  '_session_id=5a126e1a04c64a6358edb46db92ecf9d', 'X-CSRF-Token': 't+14t2b8M49qjPFyYMSL3iIDVf8DdWUQNBJPx6llhRzqG+cVEquxnXGyORg1OnxYmSLBHfgIgsbGv15ucVdxEg=='}
payload = {"operationName":"AvailableTestsQuery","extensions":{"operationId":"orders-app/bbf08309de8abffbae494f93a02b91cf"}}

# get your api_id, api_hash, token
# from telegram as described above
api_id = '2582501'
api_hash = '3afab6e42e73d02ccd80ed039d08e216'
token = '1720638274:AAGP5nLOgb2ETFBTevpzv2eMjPB-KoHoav4'

# your phone number
phone = '919447457207'

while True:
	response = requests.post("https://app.usertesting.com/graphql", headers=headers, json=payload)
	#print(response.json())
	text = str(response.json())
		#print("yes")
	   
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
	   message = "Test Available!"
	    # sending message using telegram client
	   if "scenario" in text:
	   		client.send_message(receiver, message, parse_mode='html')
	except Exception as e:
	      
	    # there may be many error coming in while like peer
	    # error, wwrong access_hash, flood_error, etc
	    print(e);
	  
	# disconnecting the telegram session 
	client.disconnect()
	time.sleep(5)

'''response:
{"data":{"currentUser":{"__typename":"User","availableSessions":[{"__typename":"AvailableSession","compensationAmount":10,"createdAt":"2021-05-19T06:33:37-07:00","deviceType":"Mac or Windows Computer","hasAgreements":false,"id":"RGlzdHJpYnV0aW9uOjpJbnZpdGF0aW9uLTEzODkwNDE5MjQ=","launchedAt":"2021-05-19T12:34:23Z","liveConvoDuration":null,"liveConvoRange":null,"nextScreenerQuestion":{"__typename":"ScreenerQuestion","answerOptions":[{"__typename":"ScreenerQuestionAnswerOption","answerText":"I wasn't aware at all","position":1},{"__typename":"ScreenerQuestionAnswerOption","answerText":"I was aware, but haven't ever used stock video","position":2},{"__typename":"ScreenerQuestionAnswerOption","answerText":"My company or I have used stock video in the past 6 months","position":3},{"__typename":"ScreenerQuestionAnswerOption","answerText":"My company or I have used stock video previously, but not in the past 6 months","position":4}],"containsLinks":false,"currentQuestionPosition":1,"hashId":"a0a6077c20e2fcf7436cb848667cfa20","multiAnswer":false,"questionText":"Before participating in this study, how aware were you of stock video content?","totalQuestionCount":7},"otherRequirement":null,"panelTitle":"The UserTesting Panel","participantFaceRecording":false,"pk":1389041924,"referenceId":"3549793E","sessionId":8656970,"sharingId":"50d9f4d7-9aa5-412c-bfcb-384347efdff4","shortTest":false,"state":"open","study":{"__typename":"Study","id":"U3R1ZHktMzU0OTc5Mw==","pk":3549793,"testPlan":{"__typename":"TestPlan","scenario":"This study will require you to visit multiple stock content sites, evaluate their VIDEO content and site experience, and complete survey questions. The study will take about 30 minutes to complete. If you are not able to dedicate the necessary amount of time to this study please do not participate. Please read the instructions on the survey thoroughly before answering any questions."},"type":"WEB"},"webBrowsers":["Chrome"]}],"testerProfile":{"__typename":"UserTesterProfile","playNotificationSound":true,"takenShortTests":false}}}}

request:
POST /graphql HTTP/1.1
Host: app.usertesting.com
X-CSRF-Token: t+14t2b8M49qjPFyYMSL3iIDVf8DdWUQNBJPx6llhRzqG+cVEquxnXGyORg1OnxYmSLBHfgIgsbGv15ucVdxEg==
Content-Type: application/json
# Content-Length: 129
Connection: close
Cookie:  _session_id=5a126e1a04c64a6358edb46db92ecf9d

{"operationName":"AvailableTestsQuery","variables":{},"extensions":{"operationId":"orders-app/bbf08309de8abffbae494f93a02b91cf"}}
'''
