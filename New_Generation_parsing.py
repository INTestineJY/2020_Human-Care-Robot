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
    tmp = ""
    f = urlopen(url)
    lines = f.readlines()
    print(len(lines))
    for i in lines:
        tmp += str(i) + " "
    return tmp


def giveMeTextBetween(l, start, end):
    s = l.index(start)
    if s is -1:
        return ""
    s += len(start)

    e = l.index(end)

    return l[s:e]


def get_title(url):
    html = get_html(url)
    ab = giveMeTextBetween(html, '<a href="#none" onclick="javascript:fnGoNodeDetail(', '</a>')
    print(ab)


get_title('https://www.dbpia.co.kr/subject/subjectList?subjCode=ND00')
