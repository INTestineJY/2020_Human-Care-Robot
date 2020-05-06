Voice = 1
Usertype = 1
Purpose = 1


while(True):
    # start_screen()은 시작 화면을 보여주는 함수
    start_screen()

    # 여기서 녹음된 목소리 / 사용자 유형 / 사용 목적 선택
    # choice는 위 세 가지를 선택하는 함수
    # 1 : 녹음된 목소리
    # 2 : 사용자 유형
    # 3 : 사용 목적 선택
    # 4 : 다음 버튼 (다음 단계로 그냥 진행. 선택하지 않고)

    while(True):
        choice1 = choice()
        if choice1 == 1:
            # 목소리 선택
            Voice = voice_choice()
            pass

        elif choice1 == 2:
            # 사용자 유형 선택
            Usertype = usertype_choice()
            pass

        elif choice1 == 3:
            # 사용 목적 선택
            Purpose = purpose_choice()
            pass

    # 특정 목적지 / 학교 순회 중 선택
    # 특정 목적지 = 1 / 학교 순회 = 2
    # choose() 는 두번째 선택 함수

    choice2 = choose()

    if choice2 == 1:
        # 특정 목적지 입력
        pass
    elif choice2 == 2:
        # 학교 순회
        pass

