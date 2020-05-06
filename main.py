Voice = 1
Usertype = 1
Purpose = 0


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
            # 목소리를 선택하는 화면이 나옴
            Voice = voice_choice()
            pass

        elif choice1 == 2:
            # 사용자 유형 선택
            # 사용자 유형을 선택하는 화면이 나옴
            Usertype = usertype_choice()
            pass

        elif choice1 == 3:
            # 사용 목적 선택
            # 사용 목적을 선택하는 화면이 나옴
            Purpose = purpose_choice()
            pass

        elif choice1 == 4 and Purpose == 0:
            # 사용 목적을 선택해달란 경고가 뜸
            pass

        elif choice1 == 4 and Purpose != 0:
            # 다음 버튼을 누른 것. voice, usertype는 모두 default값이 있으니 다음 단계로 넘어감
            pass

    # 특정 목적지 / 학교 순회 중 선택은 purpose에서 이루어짐
    # 특정 목적지 = 1 / 학교 순회 = 2

    if Purpose == 1:

