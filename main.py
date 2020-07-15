# coding=utf-8

"""import rospy
from std_msgs.msg import Int32, Bool, Int32MultiArray"""

from deokyongkim import *
from sub_button_funtions import *
from pygame.locals import *
from more_function_parsing import get_news
import ctypes
from more_function_parsing import *

dest_list = ["", "S509", "S511", "S512", "S513", "S514", "S515", "S517", "S501", "S502", "S503", "S504", "S505", "S506",
             "S507", "S508", "S510", "S516", "A501", "A502", "A503", "A504", "A506", "A508", "A509", "A505", "A507", ""]
dest_list_sub = ["", "지구과학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "융합창작실1", "융합창작실2",
                 "공학실험실",
                 "고체지구과학실",
                 "지구과학실험실", "유체지구과학실", "천체관측실", "기구보관실", "교원연구실", "협의회실", "알고리즘 학습실", "미술실 1", "미술실 2", "그래픽 디자인실",
                 "미술실 3",
                 "도예실", "레이저 커팅기실", "미술 비품실", "플로터실", ""]
destination_num = -1
now_place_num = 10
robot_now_place_num = 10

Screen_ClassButton_List = [1, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 91, 92, 93, 94, 95, 96, 97, 101, 111, 112, 113,
                           114,
                           115, 116, 121, 122, 141]

subtitle_list = ["세종과학예술영재학교에 오신 것을 진심으로 환영합니다.",
                 "저는 휴먼 케어 로봇 웬디입니다.",
                 "로봇 위에 놓여 있는 무선 키패드 혹은 터치를 통해 조작할 수 있습니다.",
                 "아무 키나 눌러주세요!",
                 "###은 시청각장애인을 위한 자막과 음성 서비스를 지원하고 있습니다.",
                 "청각 장애인에게는 화면에 모든 음성이 자막으로 나타납니다.",
                 "시각 장애인에게는 운행 중 로봇의 음성이 없을 때",
                 "비프음을 재생해 로봇의 위치를 소리로 나타냅니다.",
                 "비장애인을 선택하셨습니다.",
                 "시각장애인을 선택하셨습니다.",
                 "청각장애인을 선택하셨습니다.",
                 "이용 목적을 선택해 주세요.",
                 "학교 순회를 원하시면 1번",
                 "목적지 안내를 원하시면 2번",
                 "부가기능 사용을 원하시면 3번을 눌러주세요.",
                 "학교 순회를 선택하셨습니다.",
                 "목적지 안내를 선택하셨습니다.",
                 "부가기능을 선택하셨습니다.",
                 "목적지를 선택해주세요.",
                 "S동과 A동 중 하나를 선택해주세요.",
                 "A동은 현재 안내가 불가능합니다.",
                 "대신, A동의 시설 안내는 사용이 가능합니다.",
                 "방문하려는 장소의 유형을 선택해주세요.",
                 "S동에는 강의실, 공학실, 기타 시설이 있습니다.",
                 "강의실을 선택하셨습니다.",
                 "공학실을 선택하셨습니다.",
                 "기타 시설을 선택하셨습니다.",
                 "목적지를 선택해주세요.",
                 "S동 강의실은 지구과학 강의실인 S509, 수학 강의실인 S511, S512, S513, S514, S515, S517이 있습니다.",
                 "목적지를 선택해주세요.",
                 "S동 공학실은 융합창작실인 S501, S502,",
                 "공학실험실인 S503이 있습니다.",
                 "S동의 기타 시설은 고체지구과학실인 S504, 지구과학실험실인 S505, 유체지구과학실인 S506, 천체관측실인 S507, 기구보관실인 S508, 교원연구실인 S510, 협의회실인 S516이 있습니다.",
                 "A동에는 컴퓨터실, 미술실, 기타시설이 있습니다.",
                 "A동의 컴퓨터실은 알고리즘 실습실 A501이 있습니다.",
                 "A동의 미술실은 미술실인 A502, A503, A506, 그래픽 디자인실인 A504, 도예실인 A508, 레이저 커팅실 A509가 있습니다.",
                 "A동의 기타 시설은 미술 비품실인 A505, 플로터실 A507이 있습니다.",
                 "부가기능에는 ‘최신 뉴스 가져오기’가 있습니다.",
                 "네이버 뉴스를 통한 최신 뉴스의 헤드라인 3개는 다음과 같습니다.",
                 "S501를 선택하셨습니다.",
                 "S502를 선택하셨습니다.",
                 "S503를 선택하셨습니다.",
                 "S504를 선택하셨습니다.",
                 "S505를 선택하셨습니다.",
                 "S506를 선택하셨습니다.",
                 "S507를 선택하셨습니다.",
                 "S508를 선택하셨습니다.",
                 "S509를 선택하셨습니다.",
                 "S510를 선택하셨습니다.",
                 "S511를 선택하셨습니다.",
                 "S512를 선택하셨습니다.",
                 "S513를 선택하셨습니다.",
                 "S514를 선택하셨습니다.",
                 "S515를 선택하셨습니다.",
                 "S516를 선택하셨습니다.",
                 "S517를 선택하셨습니다.",
                 "현재 위치는 융합창작실 S501입니다.",
                 "현재 위치는 융합창작실 S502입니다.",
                 "현재 위치는 공학실험실 S503입니다.",
                 "현재 위치는 고체지구과학실 S504입니다.",
                 "현재 위치는 지구과학실험실 S505입니다.",
                 "현재 위치는 유체지구과학실 S506입니다.",
                 "현재 위치는 천체과학실 S507입니다.",
                 "현재 위치는 기구보관실 S508입니다.",
                 "현재 위치는 지구과학 강의실 S509입니다.",
                 "현재 위치는 교원연구실 S510입니다.",
                 "현재 위치는 수학 강의실 S511입니다.",
                 "현재 위치는 수학 강의실 S512입니다.",
                 "현재 위치는 수학 강의실 S513입니다.",
                 "현재 위치는 수학 강의실 S514입니다.",
                 "현재 위치는 수학 강의실 S515입니다.",
                 "현재 위치는 협의회실 S516입니다.",
                 "현재 위치는 수학 강의실 S517입니다.",
                 "목적지에 도착했습니다.",
                 "시작 위치로 돌아왔습니다."]

subtitle_screen_dic = {}


def write_subtitle(subtitle_num):
    font = pygame.font.Font('./Image/NanumSquareB.ttf', 40)
    text = font.render(subtitle_list[subtitle_num], True, (84, 137, 222))
    text_rect = text.get_rect()
    text_rect.center = 960, 850
    ourscreen.blit(text, text_rect)


"""class RosNode:
    def __init__(self):
        self.pub1 = rospy.Publisher('stop', Bool, queue_size=10)
        self.pub2 = rospy.Publisher('order', Int32, queue_size=10)
        self.sub1 = rospy.Subscriber('visit', Int32, self.via)
        self.sub2 = rospy.Subscriber('pivot_pos', Int32MultiArray, self.user_recognize)

    # 경유지에 도착했을 때 안내해주는 함수
    def via(self, data):
        robot_now_place_num = data
        pass

    # 정지 명령 발송
    def stop(self):
        self.pub1.publish(True)

    # 출발 명령 발송
    def go(self):
        self.pub1.publish(False)

    # 목적지 정보 전송
    def destination(self, index):
        self.pub2.publish(index)

    # 사용자를 인식할 수 없을 때
    def user_recognize(self, data):
        # 사용자의 앞뒤 위치가 범위를 벗어났을 때
        if data[0] == 1:
            pass
        # 사용자의 좌우 위치가 범위를 벗어났을 때
        if data[1] == 1:
            pass
        self.stop()


rospy.init_node("messenger", anonymous=True)
messenger = RosNode()"""

pygame.init()
clock = pygame.time.Clock()

Voice = 1
Usertype = 1
Purpose = 0
screen = 1
# 현재 스크린 위치 (이 값에 맞추어 스크린 띄우는 화면을 설정하고, 실행되는 함수를 설정한다

width = 1920
height = 1080

ourscreen = pygame.display.set_mode((width, height))

screen_list = []

screen_stack = [1]

for i in range(17):
    example_screen = Scene(i)
    screen_list.append(example_screen)

done = False

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pygame.display.set_mode(screensize, FULLSCREEN)


def back_button(e):
    global screen
    if is_back_button(e.pos[0], e.pos[1]) is True:
        screen_stack.pop()
        print(screen_stack)
        screen = screen_stack[-1]
        return True


def credit_button(e):
    global screen, screen_stack
    if is_credit_button(e.pos[0], e.pos[1]) is True:
        screen_stack, screen = next_screen_stack(screen_stack, -1)
        return True


count_frame = 0


def new_function():
    ttt = get_news()
    hmm = ""
    for some in ttt:
        if len(some) >= 20:
            hmm += some[0:8] + "..." + "\n"
        else:
            hmm += some + "\n"
    return hmm


title = get_news()


def play_audio():
    pygame.mixer.music.load('./audio/test.mp3')
    pygame.mixer.music.play()


save_screen_stack = 0

while not done:
    if screen == -1:
        image_name = "./image/test_image/대지 100.png"
        now_screen = pygame.image.load(image_name)
        ourscreen.blit(now_screen, (0, 0))
    else:
        now_screen = screen_list[screen]
        ourscreen.blit(now_screen.sheet, (0, 0))
    # 화면을 띄운다

    if save_screen_stack != len(screen_stack):
        save_screen_stack = len(screen_stack)
        play_audio()

    if screen == -1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)

    if screen == 0:
        # 임시 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)

    elif screen == 1:
        # 첫 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if credit_button(event) is not True:
                    screen_stack, screen = next_screen_stack(screen_stack, 2)
            if event.type == pygame.KEYUP:
                screen_stack, screen = next_screen_stack(screen_stack, 2)

    elif screen == 2:
        # 방문자 유형 선택 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)
                for button in now_screen.buttons:
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        screen_stack, screen = next_screen_stack(screen_stack, 3)
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3]:
                    screen_stack, screen = next_screen_stack(screen_stack, 3)

    elif screen == 3:
        # 이용 목적 선택

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        if i == 1:  # 학교 순회 선택
                            screen_stack, screen = next_screen_stack(screen_stack, 0)
                        elif i == 2:  # 목적지 선택
                            screen_stack, screen = next_screen_stack(screen_stack, 4)
                        else:  # 부가기능 선택
                            screen_stack, screen = next_screen_stack(screen_stack, 14)

                    if button_check is True:
                        break
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    screen_stack, screen = next_screen_stack(screen_stack, 0)
                elif event.key in [pygame.K_2, pygame.K_KP2]:
                    screen_stack, screen = next_screen_stack(screen_stack, 4)
                elif event.key in [pygame.K_1, pygame.K_KP1]:
                    screen_stack, screen = next_screen_stack(screen_stack, 14)

    elif screen == 4:
        # S A 선택화면

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen_stack, screen = next_screen_stack(screen_stack, screen + i)

                    if button_check is True:
                        break
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 1)
                if event.key in [pygame.K_2, pygame.K_KP2]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 2)
        pass

    elif screen == 5:
        # S 중 선택화면: 강의실/실험실/기타

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen_stack, screen = next_screen_stack(screen_stack, screen + i + 1)

                    if button_check is True:
                        break
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 2)
                if event.key in [pygame.K_2, pygame.K_KP2]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 3)
                if event.key in [pygame.K_3, pygame.K_KP3]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 4)
        pass

    elif screen == 6:
        # A 중 선택화면: 교무실/관리시설/학생시설

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen_stack, screen = next_screen_stack(screen_stack, screen + i + 3)

                    if button_check is True:
                        break
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 4)
                if event.key in [pygame.K_2, pygame.K_KP2]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 5)
                if event.key in [pygame.K_3, pygame.K_KP3]:
                    screen_stack, screen = next_screen_stack(screen_stack, screen + 6)
        pass

    elif 7 <= screen <= 12:
        # 세부 강의실 선택 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            button_check = False

            i = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)

                for button in now_screen.buttons:
                    i += 1

                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        break

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    button_check = True
                    i = 1
                if event.key in [pygame.K_2, pygame.K_KP2]:
                    button_check = True
                    i = 2
                if event.key in [pygame.K_3, pygame.K_KP3]:
                    button_check = True
                    i = 3
                if event.key in [pygame.K_4, pygame.K_KP4]:
                    button_check = True
                    i = 4
                if event.key in [pygame.K_5, pygame.K_KP5]:
                    button_check = True
                    i = 5
                if event.key in [pygame.K_6, pygame.K_KP6]:
                    button_check = True
                    i = 6
                if event.key in [pygame.K_7, pygame.K_KP7]:
                    button_check = True
                    i = 7

            if button_check is True:
                Screen_ClassButton_Num = 10 * screen + i
                destination_num = Screen_ClassButton_List.index(Screen_ClassButton_Num)
                screen_stack, screen = next_screen_stack(screen_stack, 13)
                break

    elif screen == 13 or screen == 15:
        # 목적지
        font = pygame.font.Font('./Image/NanumSquareB.ttf', 88)
        text = font.render(dest_list[now_place_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 631, 526
        ourscreen.blit(text, text_rect)

        font = pygame.font.Font('./Image/NanumSquareB.ttf', 44)
        text = font.render(dest_list_sub[now_place_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 631, 626
        ourscreen.blit(text, text_rect)

        # 현재 위치
        font = pygame.font.Font('./Image/NanumSquareB.ttf', 88)
        text = font.render(dest_list[destination_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 1283, 526
        ourscreen.blit(text, text_rect)

        font = pygame.font.Font('./Image/NanumSquareB.ttf', 44)
        text = font.render(dest_list_sub[destination_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 1283, 626
        ourscreen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button(event) is not True and credit_button(event) is not True and screen is 13:
                    # messenger.destination(destination_num)
                    screen_stack.append(15)
                    print(screen_stack)
                    screen = 15

        if screen == 15:
            count_frame += 1
            arrow_count = count_frame // 10
            image_name = "./image/test_image/" + "driving" + str(arrow_count % 3 + 1) + ".png"
            image = pygame.image.load(image_name)
            image = pygame.transform.scale(image, (250, 100))
            ourscreen.blit(image, (839, 513))

            if now_place_num == destination_num:
                # messenger.pub1.publish(1)
                pass
            elif robot_now_place_num != now_place_num and not pygame.mixer.music.get_busy():
                now_place_num = robot_now_place_num

    elif screen == 14:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)
                i = 0
                for button in now_screen.buttons:
                    print("eha;lsdkfj")
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen_stack.append(16)
                        print(screen_stack)
                        screen = 16

                    if button_check is True:
                        break

    elif screen == 16:
        ####code here

        asdf = 0
        for i in title:
            font = pygame.font.Font('./Image/NanumSquareB.ttf', 44)
            text = font.render(i, True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = 960, 300 + asdf
            ourscreen.blit(text, text_rect)
            asdf += 100

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                credit_button(event)

    else:
        # 돌아다니면서 설명할 때
        pass

    pygame.display.update()
    clock.tick(10)
    pass

print("finish")
# blah
