from os import system
from datetime import datetime
from time import sleep
try:
    from selenium import webdriver 
except:
    system("pip3 install selenium")
    from selenium import webdriver 
try:
    from bs4 import BeautifulSoup
except:
    system("pip install beautifulsoup4")
    from bs4 import BeautifulSoup

date = datetime.now().strftime("%d-%m-%Y")
writer_online = open("online_hidden_services_on-"+date+".txt","w+")
writer_offline = open("offline_hidden_services_on-"+date+".txt","w+")
url = "https://dark.fail/"

print("Starting Chrome WebDriver....")
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get(url)
content = driver.page_source
driver.quit()

soup = BeautifulSoup(content, features="lxml")

# list of online services
print("Extractig list of online services....")
for data in soup.findAll('div', attrs={'class':'online'}):
    for lines in data.findAll('li', attrs={'class':'online status1'}):
        if lines.text == None:
            pass
        else:
            writer_online.write(lines.text)
sleep(3)
print("Done !!!")
sleep(1)

# list of online services
print("Extractig list of offline services....")
for data in soup.findAll('div', attrs={'class':'offline'}):
    for lines in data.findAll('li', attrs={'class':'status0'}):
        if lines.text == None:
            pass
        else:
            writer_offline.write(lines.text)

sleep(3)
print("Done!!!")
sleep(1)
print("Exiting!!!")
sleep(1)

writer_online.close()
writer_offline.close()