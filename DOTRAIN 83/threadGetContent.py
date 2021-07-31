import requests
import concurrent.futures
import threading
from bs4 import BeautifulSoup

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "seesion"):
        thread_local.session = requests.Session()
    return thread_local.session


def get_content(url):
    wr = open('output.csv', 'a')
    session = get_session()
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
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_content, urls)

