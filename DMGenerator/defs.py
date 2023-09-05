import time
import requests as web
from random import randrange as r
from bs4 import BeautifulSoup as bs


def inTput(prompt_string):
    response = input(prompt_string)
    return int(response)

def waitRead(list):
    time.sleep(len(list)/(6.666*10))

def fillerString(iterates):
    return "a" * iterates


def scrape(url, html_type, html_class):
    url = web.get(url).text
    soup = bs(url, "lxml")
    tables = soup.find_all(html_type, html_class)
    return tables

def dieRoll(diceSize, numbers_of_dice = 1):
    sum = 0
    for i in numbers_of_dice:
        rolled = r(diceSize)
        sum += rolled
    return sum
