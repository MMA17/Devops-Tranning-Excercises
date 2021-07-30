import requests
from bs4 import BeautifulSoup

wr = open('output.csv', 'w')
url = 'https://bizflycloud.vn/tin-tuc/caas-20210622161033206.htm'
test = requests.get(url)
soup = BeautifulSoup(test.text, 'html.parser')

wr.write("name/title; content; created date; url\n")
wr.write(str(soup.title.string) + "; ")

# print (soup.get_text('detail-content'))
# for data in soup.find_all('div', {'class':'detail-content'}):
#     print(data.text)
for content in soup.find_all('p'):
    a = content.text
    a = a.replace(';',".")
    wr.write(a)
wr.write(";")

date = soup.find('div', {'class': 'read-time'})
wr.write(date.text+"; ")

wr.write(url)
