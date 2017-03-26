import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
import re
import pandas as pd


# print(np.arange(0, 1, 0.1))
# print(sum([1, 2, 3]))

# list_a = []
# list_a.append('Hello')
# list_a.append('World')
# print(list_a)

# a = "5721"
# print(long(a))

# print(len('-12'))
#
# test_url = "http://www.baidu.com"
#
# response = urllib.request.urlopen(test_url)
# print(response.getcode())
# print(response.read())

# html = urllib.request.urlopen("http://www.baidu.com")
# bs_obj = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
# link_list = bs_obj.findAll('a')
# for link in link_list:
#     print(link.name, link['href'], link.get_text())
# print("title tag: ", bs_obj.body.p)

"""
Request an address


def get_html_title(url):

    try:
        html = urllib.request.urlopen(url)
    except Exception as e:
        return None

    try:
        bs_obj = BeautifulSoup(html.read(), 'html_parser')
        title = bs_obj.title
    except Exception as e:
        return None

    return title

title = get_html_title("http://www.taobao.com")
if title is not None:
    print(title)
else:
    print("Getting the Title is failure")
"""

# pattern = re.compile(r'[A-Za-z0-9._+]+@[A-Za-z]+\.(com|org|edu|net)')
# match = pattern.match('bliang33@csu.edu.au')
# print(match.group())
#
#
# html = urllib.request.urlopen("http://www.pythonscraping.com/pages/page3.html")

ser_obj = pd.Series(range(10, 20))
print(ser_obj)


