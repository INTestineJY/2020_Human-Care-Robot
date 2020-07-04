# coding=utf-8

"""import rospy
from std_msgs.msg import Int32, Bool, Int32MultiArray"""

from deokyongkim import *
from sub_button_funtions import *
from pygame.locals import *
import ctypes
from more_function_parsing import *

dest_list = ["S509", "S511", "S512", "S513", "S514", "S515", "S517", "S501", "S502", "S503", "S504", "S505", "S506",
             "S507", "S508", "S510", "S516", "A501", "A502", "A503", "A504", "A506", "A508", "A509", "A505", "A507"]
dest_list_sub = ["지구과학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "수학 강의실", "융합창작실1", "융합창작실2", "공학실험실",
                 "고체지구과학실",
                 "지구과학실험실", "유체지구과학실", "천체관측실", "기구보관실", "교원연구실", "협의회실""알고리즘 학습실", "미술실 1", "미술실 2", "그래픽 디자인실",
                 "미술실 3",
                 "도예실", "레이저 커팅기실", "미술 비품실", "플로터실"]
destination_num = -1
now_place_num = 9

Screen_ClassButton_List = [1, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 91, 92, 93, 94, 95, 96, 97, 101, 111, 112, 113, 114,
                           115, 116, 121, 122]

"""class RosNode:
    def __init__(self):
        self.pub1 = rospy.Publisher('stop', Bool, queue_size=10)
        self.pub2 = rospy.Publisher('order', Int32, queue_size=10)
        self.sub1 = rospy.Subscriber('visit', Int32, self.via)
        self.sub2 = rospy.Subscriber('pivot_pos', Int32MultiArray, self.user_recognize)

    # 경유지에 도착했을 때 안내해주는 함수
    def via(self, data):
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

for i in range(15):
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
    global screen
    if is_credit_button(e.pos[0], e.pos[1]) is True:
        pass


while not done:
    now_screen = screen_list[screen]
    ourscreen.blit(now_screen.sheet, (0, 0))

    # 화면을 띄운다

    if screen == 0:
        # 임시 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)

    elif screen == 1:
        # 첫 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen_stack.append(2)
                print(screen_stack)
                print(event.pos[0], event.pos[1])
                screen = 2

    elif screen == 2:
        # 방문자 유형 선택 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in now_screen.buttons:
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        screen_stack.append(3)
                        print(screen_stack)
                        screen = 3
                back_button(event)

        pass

    elif screen == 3:
        # 이용 목적 선택

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        if i == 1:  # 학교 순회 선택
                            screen_stack.append(0)
                            print(screen_stack)
                            screen = 0
                        elif i == 2:  # 목적지 선택
                            screen_stack.append(4)
                            print(screen_stack)
                            screen = 4
                        else:  # 부가기능 선택
                            screen_stack.append(14)
                            print(screen_stack)
                            screen = 14

                    if button_check is True:
                        break
        pass

    elif screen == 4:
        # S A 선택화면

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                i = 0
                for button in now_screen.buttons:
                    print("check")
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen_stack.append(screen + i)
                        print(screen_stack)
                        screen += i

                    if button_check is True:
                        break
        pass

    elif screen == 5:
        # S 중 선택화면: 강의실/실험실/기타

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen_stack.append(screen + i + 1)
                        print(screen_stack)
                        screen += 1 + i

                    if button_check is True:
                        break
        pass

    elif screen == 6:
        # A 중 선택화면: 교무실/관리시설/학생시설

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen_stack.append(screen + i + 3)
                        print(screen_stack)
                        screen += 3 + i

                    if button_check is True:
                        break
        pass

    elif 7 <= screen <= 12:
        # 세부 강의실 선택 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                back_button(event)
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True

                    if button_check is True:
                        Screen_ClassButton_Num = 10 * screen + i
                        destination_num = Screen_ClassButton_List.index(Screen_ClassButton_Num)
                        screen_stack.append(13)
                        print(screen_stack)
                        screen = 13
                        break

    elif screen == 13:
        # 목적지
        font = pygame.font.Font('./Image/NanumSquareB.ttf', 88)
        text = font.render(dest_list[destination_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 631, 526
        ourscreen.blit(text, text_rect)

        font = pygame.font.Font('./Image/NanumSquareB.ttf', 44)
        text = font.render(dest_list_sub[destination_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 631, 626
        ourscreen.blit(text, text_rect)

        # 현재 위치
        font = pygame.font.Font('./Image/NanumSquareB.ttf', 88)
        text = font.render(dest_list[now_place_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 1283, 526
        ourscreen.blit(text, text_rect)

        font = pygame.font.Font('./Image/NanumSquareB.ttf', 44)
        text = font.render(dest_list_sub[now_place_num], True, (84, 137, 222))
        text_rect = text.get_rect()
        text_rect.center = 1283, 626
        ourscreen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button(event) is not True:
                    # messenger.destination(destination_num)
                    screen_stack.append(0)
                    print(screen_stack)
                    screen = 0

    elif screen == 14:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button(event) is not True:
                    screen_stack.append(0)
                    print(screen_stack)
                    screen = 0

    else:
        # 돌아다니면서 설명할 때
        pass

    pygame.display.update()
    clock.tick(10)
    pass

print("finish")
