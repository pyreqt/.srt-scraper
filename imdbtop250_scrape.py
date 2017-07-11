#Scape imdn
# check - http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/
# - http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html
from bs4 import BeautifulSoup
import requests
import re

url = r"http://www.imdb.com/chart/top"
req = requests.get(url)
soup = BeautifulSoup(req.content,'lxml')
tdtags=soup.find_all('td',class_='titleColumn')
for i in range(len(tdtags)):
    print(tdtags[i].a.string.extract())




