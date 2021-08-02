import requests
import multiprocessing
from bs4 import BeautifulSoup

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def get_content(url):
    wr = open('output.csv', 'a')
    # session = get_session()
    test = session.get(url)
    soup = BeautifulSoup(test.text, 'html.parser')
    wr.write(str(soup.title.string) + "; ")

    for content in soup.find_all('p'):
        a = content.text
        a = a.replace(';', ".")
        wr.write(a)
    wr.write(";")
    date = soup.find('div', {'class': 'read-time'})
    wr.write(date.text+"; ")
    wr.write(url + "\n")
    wr.close()


def get_all_content(urls):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(get_content, urls)

