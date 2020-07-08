import bs4
import requests
num = 0


def news_get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

    return response.text


def sub_get_insert_time_and_press(url):
    """
    기사에서 기사 등록일과 언론사를 찾아 반환한다.
    :param url: 기사 url
    :return: 기사 등록일, 언론사
    """
    sub_html = get_html(url)  # get_html() 을 이용해서, 대상 기사에 접속 html tag 를 가져온다.
    sub_soup = bs4.BeautifulSoup(sub_html, 'html.parser')  # bs4 parser 를 이용하여, 뽑아오기 쉽게 parsing 한다.

    # <div class='sponser'> 안에 있는, <span class='t11'> 의 text 를 추출한다.
    news_insert_time = sub_soup.select('div.sponsor span.t11')[0].getText().split()[1]

    # <div class='press_logo'> 안에 있는, <a> 안에 있는 <img> 들 중에 첫번째[0] 요소의 title 을 가져온다.
    news_press = sub_soup.select('div.press_logo a img')[0].get('title')

    return news_insert_time, news_press


def get_news():
    html = get_html('https://news.naver.com')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    titles = []

    # <div class='main_component'> 안에 있는, <li> 안에 있는 <a> 를 모두 검색하여 List 형식으로 반환한다.
    news_main = soup.select('div.main_component li a')

    chk = 0

    for i in news_main:
        # ex) <a href="https://news.naver.com/main/..."><strong>CPU 가격 30% 급등…중소 PC업체들 '비상'</strong></a>
        news_title = i.getText().strip()  # <a> 에 담겨있는 text 를 가져온다.
        news_url = i.get('href')  # <a> 에 설정되어 있는 href 값을 가져온다.

        if 'https://' in news_url:
            news_insert_time, news_press = sub_get_insert_time_and_press(news_url)
            # print("%s | %s | %s | %s" % (news_title, news_press, news_insert_time, news_url))
            titles.append(news_title)
            print("did")
            chk += 1
            if chk == 5:
                return titles


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    did = True

    while did:
        try:
            response = requests.get(url)
            response.raise_for_status()
            did = False
        except Exception:
            print("ERROR")
            did = True


    return response.text


def isEnglishOrKorean(input_s):
    k_count = 0
    e_count = 0
    for c in input_s:
        if ord('가') <= ord(c) <= ord('힣'):
            k_count += 1
        elif ord('a') <= ord(c.lower()) <= ord('z'):
            e_count += 1
    return "k" if k_count > 1 else "e"


def get_abstract_title(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    titles = soup.select('li.item div.titWrap')

    # print("hohoho")

    for i in titles:
        pass

    return ['미세먼지 농도가 소프트콘택트렌즈 착용에 미치는 영향', '게임 장애/중독 연구에 대한 비판적 분석', '간호사의 태움 개념분석', '한국의 젠트리피케이션', '도시공간에서의 미세먼지 문제의 이해와 해결방안']


def abstract_name(url):
    answer = ""
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # <div class='main_component'> 안에 있는, <li> 안에 있는 <a> 를 모두 검색하여 List 형식으로 반환한다.
    news_main = soup.select('span.articleTitle')

    for i in news_main:
        # ex) <a href="https://news.naver.com/main/..."><strong>CPU 가격 30% 급등…중소 PC업체들 '비상'</strong></a>
        news_title = i.getText().strip()  # <a> 에 담겨있는 text 를 가져온다.
        # news_url = i.get('onclick')  # <a> 에 설정되어 있는 href 값을 가져온다.

        news_l = news_title.split()

        for j in news_l:
            if isEnglishOrKorean(j) == 'k':
                print(j, end=' ')
                answer += j + ' '
    return answer


def abstract_and_keyword(url):
    answer = ""
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # <div class='main_component'> 안에 있는, <li> 안에 있는 <a> 를 모두 검색하여 List 형식으로 반환한다.
    news_main = soup.select('p.article')
    for i in news_main:
        # ex) <a href="https://news.naver.com/main/..."><strong>CPU 가격 30% 급등…중소 PC업체들 '비상'</strong></a>
        news_title = i.getText().strip()  # <a> 에 담겨있는 text 를 가져온다.
        # news_url = i.get('onclick')  # <a> 에 설정되어 있는 href 값을 가져온다.

        news_l = news_title.split()
        for j in news_l:
            if isEnglishOrKorean(j) == 'k':
                print(j, end=' ')
                answer += j + ' '
        print("")
        print("="*30)
        print("")
    news_key = soup.select('dl.keyword.eHideSec a')

    key = ""

    for i in news_key:
        key_title = i.getText().strip()

        key_l = key_title.split('#')

        for j in key_l:
            if isEnglishOrKorean(j) == 'k':
                print(j)
                key += j + '\n'
    return answer, key


def add_file(url):
    global num
    print(num)
    put_in = abstract_and_keyword(url)
    num += 1
    name = "abstract" + str(num) + '.txt'
    key_name = "keyword" + str(num) + '.txt'
    f = open(name, 'w')
    ff = open(key_name, 'w')
    f.write(put_in[0])
    ff.write(put_in[1])
    f.close()
    ff.close()


if __name__ == "__main__":
    # tmptmp = get_abstract_title("https://www.dbpia.co.kr/subject/subjectList?subjCode=ND00")
    # print(tmptmp)
    text = get_news()

    for i in text:
        print(i)
