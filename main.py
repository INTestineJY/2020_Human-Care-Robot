# coding=utf-8
import pygame
from deokyongkim import *

pygame.init()
clock = pygame.time.Clock()

Voice = 1
Usertype = 1
Purpose = 0
screen = 1
# 현재 스크린 위치 (이 값에 맞추어 스크린 띄우는 화면을 설정하고, 실행되는 함수를 설정한다
# 0: 맨 처음 화면
# 1: 첫 선택 화면
# 2: 목소리 선택 화면
# 3: 사용자 유형 선택 화면
# 10: 설명 화면

list_purpose1 = []
list_purpose2 = []

# 목적에 맞춘 목적지 순서 리스트
# Purpose 1 은 한군데만 (리스트 안에 든 것도 하나만)
# Purpose 2 는 학교 순회 (순회하는 곳의 순서에 맞춰 리스트에 미리 넣어두기)


width = 1024
height = 600

ourscreen = pygame.display.set_mode((width, height))

screen_list = []

for i in range(5):
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
                print("change screen")
                screen = 2

    elif screen == 2:
        # 방문자 유형 선택 화면
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

    elif screen == 3:
        # 이용 목적 선택

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                i = 0
                for button in now_screen.buttons:
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
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen += 1+i

                    if button_check is True:
                        break
        pass

    elif screen == 6:
        # A 중 선택화면: 교무실/관리시설/학생시설

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                i = 0
                for button in now_screen.buttons:
                    i += 1
                    button_check = False
                    if button.isClicked(event.pos[0], event.pos[1]) is True:
                        button_check = True
                        screen += 3+i

                    if button_check is True:
                        break
        pass


    else:
        # 돌아다니면서 설명할 때
        pass

    pygame.display.update()
    clock.tick(10)
    pass

print("finish")
