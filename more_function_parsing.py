import bs4
import requests
num = 0


def get_html(url):
    """
    웹 사이트 주소를 입력 받아, html tag 를 읽어드려 반환한다.
    :param url: parsing target web url
    :return: html tag
    """
    response = requests.get(url)
    response.raise_for_status()

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

    titles = soup.select('h5')

    print("hohoho")

    for i in titles:
        print("DIDID")
        print(i)


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


get_abstract_title("https://www.dbpia.co.kr/subject/subjectList?subjCode=ND00")


#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09274444#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08280776")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09263409#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09227142")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09037418")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271232")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09229427")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09221705#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271233")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09262409")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09229421")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09219695")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09274438")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09226213#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09219372#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271356")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08766546#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272226")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08645914")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08765169#none")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01618430")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09274471")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08000513")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07514225#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08766547#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07608092")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07423418")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08752216")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09216565")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271954")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272231")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09264454")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271346")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09263062")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271234")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07514225")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01928676")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07321794")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271348")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08789893")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09114170")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08789876")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07016166")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07489560")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09226163")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06703356")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09228807")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09227462")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09227172")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01086338#none")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09226262")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09226278")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06521693")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01468131#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09262371")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09227596")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09216053")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09220003")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09220186")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09228799")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09218048")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09215825")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09218627")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09218189")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06383685")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09228183")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE02343993")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09233205")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09215993")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09219372")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09232421")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01875263")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08770220")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08767527")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08770217")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08770219")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01460715")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07489214")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01020820")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08769798")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07489274")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06370417")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09271356")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08280776")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09056508")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08769544")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08770986")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08770986")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08767518")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09056657")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08766547")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08766561")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08769800")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09215827")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07521365")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07521266")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08895296")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09233104")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08844838")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09233103")





# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07617176")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09218303")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09219310")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08769917")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09221123")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08769090")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08762552")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08746655")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08741434")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08744313")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08733750")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08511708")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08008631")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08011862")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08008629")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08751979")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08008730")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08167711")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08167714")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07624034")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07611437")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07614453")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07605567")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07604753")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08741395")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07606709")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07588077")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07575580")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07540539")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07538575")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07531899")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08001658")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07524164")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07522504")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07514205")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07504719")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08221508")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07610124")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07474125")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07449045")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08221527")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08221527")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07291710")
# # 여기서부터는 전기/제어계측공학
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09231895")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09226260")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07614904")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08767782")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08750983")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08749698")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08745232")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08732741")
#
# # 여기까지 50개
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08140457")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07621992")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08732258")
# # 수학, 통계학
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07364622")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07244778")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07245445")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07611776")
# # 물리학
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07230216")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01835422")
# # 전자/정보통신학
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06142657")
#
# #검색어 : 공학
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08168112#none")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272843")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09228843")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09219885")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08765543")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07610115")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08766899")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07540239")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08752821")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08751488")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08733185")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08328870")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08008578")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08000284")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08001069")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08741395")
# # 검색어 : 수학
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272967")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272978")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272974")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272969")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09272975")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08768417")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08732221")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08732224")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08732225")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08732223")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE08168092")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07997316")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07621026")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07621029")
#
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07621027")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07621023")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09274438")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09274432")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09273486")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09264415")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE09228814")
# # 분야 : 치의학
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE07539491")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE06514591")
# add_file("https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01216097")

# 100 개
