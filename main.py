# coding=utf-8

import rospy
from std_msgs.msg import Int32, Bool, String

from deokyongkim import *

dest_list = ['', '']


class RosNode:
    def __init__(self):
        self.pub1 = rospy.Publisher('stop', Bool, queue_size=10)
        self.pub2 = rospy.Publisher('order', Int32, queue_size=10)
        self.sub1 = rospy.Subscriber('visit', Int32, self.via)
        self.sub2 = rospy.Subscriber('find_piv', String, self.stop)

    # 경유지에 도착했을 때 안내해주는 함수
    def via(self, data):
        pass

    # 정지 명령 발송
    def stop(self):
        self.pub1.publish(True)

    # 출발 명령 발송
    def go(self):
        self.pub1.publish(False)

    def destination(self, index):
        self.pub2.publish(index)


rospy.init_node("service_core", anonymous=True)
messenger = RosNode()

pygame.init()
clock = pygame.time.Clock()

Voice = 1
Usertype = 1
Purpose = 0
screen = 1
# 현재 스크린 위치 (이 값에 맞추어 스크린 띄우는 화면을 설정하고, 실행되는 함수를 설정한다

list_purpose1 = []
list_purpose2 = []

# 목적에 맞춘 목적지 순서 리스트
# Purpose 1 은 한군데만 (리스트 안에 든 것도 하나만)
# Purpose 2 는 학교 순회 (순회하는 곳의 순서에 맞춰 리스트에 미리 넣어두기)


width = 1920
height = 1080

back_button_x_1 = 47
back_button_y_1 = 980
back_button_x_2 = 118
back_button_y_2 = 1052


def is_back_button(x, y):
    if back_button_x_1 <= x <= back_button_x_2 and back_button_y_1 <= y <= back_button_y_2:
        return True
    return False


ourscreen = pygame.display.set_mode((width, height))

screen_list = []

for i in range(15):
    example_screen = Scene(i)
    screen_list.append(example_screen)

done = False

while not done:
    ourscreen.fill((10, 100, 100))
    now_screen = screen_list[screen]
    ourscreen.blit(now_screen.sheet, (0, 0))

    # 화면을 띄운다

    if screen == 0:
        # 임시 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

    if screen == 1:
        # 첫 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen = 2

    elif screen == 2:
        # 방문자 유형 선택 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in now_screen.buttons:
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        screen = 3
                    if is_back_button(event.pos[0], event.pos[1]) is True:
                        screen = 1

        pass

    elif screen == 3:
        # 이용 목적 선택

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_back_button(event.pos[0], event.pos[1]) is True:
                    screen = 2
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        if i == 1:  # 학교 순회 선택
                            screen = 0
                        elif i == 2:  # 목적지 선택
                            screen = 4
                        else:  # 부가기능 선택
                            screen = 0

                    if button_check is True:
                        break
        pass

    elif screen == 4:
        # S A 선택화면

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_back_button(event.pos[0], event.pos[1]) is True:
                    screen = 3
                i = 0
                for button in now_screen.buttons:
                    print("check")
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
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
                if is_back_button(event.pos[0], event.pos[1]) is True:
                    screen = 4
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
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
                if is_back_button(event.pos[0], event.pos[1]) is True:
                    screen = 4
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
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
                if is_back_button(event.pos[0], event.pos[1]) is True:
                    if screen in [7, 8, 9]:
                        screen = 5
                    else:
                        screen = 6
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        screen = 13
                        button_check = True

                    if button_check is True:
                        break

    else:
        # 돌아다니면서 설명할 때
        pass

    pygame.display.update()
    clock.tick(10)
    pass

print("finish")
