# coding=utf-8
import pygame

Voice = 1
Usertype = 1
Purpose = 0
screen = 0  # 현재 스크린 위치 (이 값에 맞추어 스크린 띄우는 화면을 설정하고, 실행되는 함수를 설정한다
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


def screen1(x, y):
    pass


def start_screen():
    global screen
    done = False

    while not done:
        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True

        if screen == 0 :
            # 첫 화면
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen = 1
                    continue

        elif screen == 1:
            # 목소리/목적/다음화면 선택화면
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    screen1_check = screen1(event.pos[0], event.pos[1])

            if screen1_check != 0:
                screen = screen1_check
                continue

        elif screen == 2:
            # 목소리 선택
            pass

        elif screen == 3:
            # 목적 선택
            pass

        else:
            # 돌아다니면서 설명할 때
            pass

        pass
