# coding=utf-8


"""
https://www.hongxiu.com/rank/hxyuepiao

无限debug
"""

import os
import codecs
import json
import random
import time
import traceback

import numpy as np
import pandas as pd

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

path_chromedriver = "Your ChromeDriver Path.exe"

options = webdriver.ChromeOptions()


# options.add_argument("--headless")


# driver = webdriver.Chrome()


def strip(tag):
    if tag is None:
        return ""
    return tag.text.strip()


def mydriver():
    return webdriver.Chrome(
        options,
    )


def ins(f):
    with codecs.open(f, "r", encoding="utf-8") as _ins:
        return _ins.read()


def insJson(f):
    with codecs.open(f, "r", encoding="utf-8") as _ins:
        return json.load(_ins)


def out(f, s):
    with codecs.open(f, "w", encoding="utf-8") as _out:
        _out.write(s)


def outJson(f, s):
    with codecs.open(f, "w", encoding="utf-8") as _out:
        json.dump(s, _out)


def click_elem(driver, xpath):
    try:
        elem = driver.find_element(By.XPATH, xpath)
        elem.click()
    except Exception as e:
        pass
    time.sleep(1)


def getBodyHtml(
    driver,
):
    elem = driver.find_element(By.TAG_NAME, "body")
    if elem is None:
        return ""
    return elem.get_attribute("outerHTML").strip()


def gettext(html, name, attrs):
    bsobj = bs4.BeautifulSoup(html, "html.parser")
    txt = bsobj.find(name=name, attrs=attrs)
    return strip(txt)


def main():
    #  step1

    try:
        driver = mydriver()
        url = ""
        driver.get(url)
        html = getBodyHtml(driver)
        html = gettext(getBodyHtml(driver), "div", {"class": "rank-list"})
        urls = []
        out("html.html", html)
        outJson("html.json", urls)
    except Exception as e:
        traceback.print_exc()
    finally:
        driver.close()


if __name__ == "__main__":
    pass
