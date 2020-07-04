# import sys
# from urllib.request import urlopen
# import re
# from html import unescape
#
#
# # url : https://www.dbpia.co.kr/subject/subjectList?subjCode=ND00.html
# def get_html(url):
#     f = urlopen(url)
#
#     encoding = f.info().get_content_charset(failobj="utf-8")
#
#     text = f.read().decode(encoding)
#
#     return text
#
#
# def paper_title(url):
#     html = get_html(url)
#
#     for partial_html in re.findall(r'<td calss="left"><a.*?</td>', html, re.DOTALL):
#         title = re.sub(r'<.*?>', "", partial_html)
#         title = unescape(title)
#         print('title: ', title)
#
#
# paper_title("https://www.dbpia.co.kr/subject/subjectList?subjCode=ND00.html")

from urllib.request import urlopen

hmm = "https://www.dbpia.co.kr/subject/subjectList?subjCode=ND00"


def get_html(url):
    f = urlopen(url)
    print(f.read())


def giveMeTextBetween(url):
    get_html(url)


get_html(hmm)
