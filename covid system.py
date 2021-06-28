from bs4 import BeautifulSoup
import requests
from plyer import notification
def getData(url):
     r = requests.get(url)
     return r.text
def notify_me(title, message):
     notification.notify(
     title = title,
     message = message,
     app_icon = None,
     timeout = 10,
     )
if __name__ == "__main__":
     myHtmlData = getData('https://www.mohfw.gov.in/')
     soup = BeautifulSoup(myHtmlData, 'html.parser')
     active_cases = soup.find("li", {'class': 'bgblue'}).find('strong').get_text()
     Cured_Discharged = soup.find("li", {'class': 'bggreen'}).find('strong').get_text()
     Deaths = soup.find("li", {'class': 'bg-red'}).find('strong').get_text()
     Total_cases = int(active_cases) + int(Cured_Discharged) + int(Deaths)
     notify_title = "COVID-19 Status (Source : https://www.MoHFW.gov.in/)"
     notify_text = f"Confirmed : {Total_cases}\nActive Cases : {active_cases}\nCured/Discharged : {Cured_Discharged}\nDeaths : {Deaths}"
     notify_me(notify_title, notify_text)