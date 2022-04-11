import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.topendsports.com/sport/soccer/list-player-of-the-year-ballondor.htm"
r = requests.get(url).text
s = BeautifulSoup(r, "html.parser")

a = s.find_all("table", class_="list")

ball=[]
for i in a:
   i.find_all("td")
   for x  in i:
       ball.append(x.text.strip("\n").split(("\n")))
print(ball)