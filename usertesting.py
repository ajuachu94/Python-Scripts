import requests
from bs4 import BeautifulSoup

count=0
data = requests.get("https://app.usertesting.com/my_dashboard/available_tests_v3", headers={'Host': 'app.usertesting.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Cookie':  '_session_id=5a126e1a04c64a6358edb46db92ecf9d'})

soup = BeautifulSoup(data.text, 'html.parser')
for title in soup.find_all('title'):
	if (count==0):
		print("Title is : ", title.get_text())
		count+=1