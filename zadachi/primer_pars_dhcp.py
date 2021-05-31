import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import time
import requests
from bs4 import BeautifulSoup



options = Options()  
options.add_argument("--headless")  
driver = webdriver.Chrome('/home/a.m.gordeev/chromedriver/chromedriver', options = options )   

mel1 = []
mel2 = []

ngnmel1 = []
ngnmel2 = []

smr1 = []
smr2 = []

chv1 = []
chv2 = []


User = 'urer_key'
Token = 'just_token'


def sendmass(canRF, textMessag, Token, User):

	headers = {'X-Auth-Token': Token, 'X-User-Id' :User, 'Content-type' :'application/json' }
	urll = 'https://rocketchat.ru/api/v1/chat.postMessage'
	dataw = '{"channel" : "'+canRF+'", "text": "'+textMessag+'"}'
			
	response2 = requests.post(url = urll, headers=headers, data = dataw.encode('utf-8'))
	print(response2.json())

retyy = []
procentloadsubnet = 90

def pars(url,retyy):
	driver.get(url)
	time.sleep(7)
	#print(page.text)
	soup = BeautifulSoup(driver.page_source, "html.parser")
	try:
		tr  =  soup.find(id = 'shared-networks').find_all('tr')
		i = 1
		while i < len(tr) :
			#print( tr[i].find_all('td')[1].text)
			qwe = td1 = tr[i].find_all('td')[1].text.split()[1].split('(')[1].split(')')[0]
			td1 = tr[i].find_all('td')[1].text.split()[1].split('(')[1].split('%')[0]
			td =float(td1)
			if td > procentloadsubnet :
				ret = tr[i].find_all('td')[0].find_all('b')[0].text
				mass = 'Загрузка '  + ret + ' -- ' +  qwe + '    ' + tr[i].find_all('td')[2].text+ '/'+ tr[i].find_all('td')[3].text +  "\n"
				retyy.append(mass)
				#print(mass) 
			
			i += 1
		retyy.insert(0, ' Сервер DHCP ' +url + '\n')
	except AttributeError as e:
		print( 'Не удалось подключиться к '+ url)
pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = mel1 )
pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = mel2 )
pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = ngnmel1 )
pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = ngnmel2 )

pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = smr1 )
pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = smr2 )

pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = chv1 )
pars(url = 'monitor-dhcp.mts-nn.ru/', retyy = chv2 )


print(mel1)
if len(mel1) > 1 or len(mel2) > 1 or len(smr1) > 1 or len(smr2) > 1 or chv1  > 1 or chv2 > 1 :
	
			
	time.sleep(15)
	if  len(mel1) > 1 :
				
		full_mess = '@here ' + ''.join(mel1)
		sendmass(canRF = '#mrf-spd-mel', textMessag = full_mess, Token = Token, User = User)

	if  len(mel2) > 1 :
		full_mess = '@here ' + ''.join(mel2)
		sendmass(canRF = '#mrf-spd-mel', textMessag = full_mess, Token = Token, User = User)

	if  len(ngnmel1) > 1 :
		full_mess = '@here ' + ''.join(ngnmel1)
		sendmass(canRF = '#mrf-spd-mel', textMessag = full_mess, Token = Token, User = User)

	if  len(ngnmel2) > 1 :
		full_mess = '@here ' + ''.join(ngnmel2)
		sendmass(canRF = '#mrf-spd-mel', textMessag = full_mess, Token = Token, User = User)


	if  len(smr1) > 1 :
		full_mess = '@here ' + ''.join(smr1)
		sendmass(canRF = '#mrf-spd-sm', textMessag = full_mess, Token = Token, User = User)

	if  len(smr2) > 1 :
		full_mess = '@here ' + ''.join(smr2)
		sendmass(canRF = '#mrf-spd-sm', textMessag = full_mess, Token = Token, User = User)


	if  len(chv1) > 1 :
		full_mess = '@here ' + ''.join(chv1)
		sendmass(canRF = '#mrf-spd-chr', textMessag = full_mess, Token = Token, User = User)

	if  len(chv2) > 1 :
		full_mess = '@here ' + ''.join(chv2)
		sendmass(canRF = '#mrf-spd-chr', textMessag = full_mess, Token = Token, User = User)
	
	
driver.close()
driver.quit()