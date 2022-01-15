import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


dwarfs_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

browser = requests.get(dwarfs_url)


soup = bs(browser.text,"html.parser")

table = soup.find('table')

temp_list= []

table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
Star = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    Star.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    
    
    
df2 = pd.DataFrame(list(zip(Star,Distance,Mass,Radius)),columns=['Star','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf.csv')