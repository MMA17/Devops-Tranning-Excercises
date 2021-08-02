import multiThread
import time


def singleThread(urls):
    for url in urls:
        multiThread.get_content(url)