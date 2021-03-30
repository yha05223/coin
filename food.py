#밥 먹자
#메뉴 1,2,3 정하자
# 먹는 몌뉴 선택 메뉴 출력
import random
##아래 전체를 반복시킴##
for i in range(1, 4):

    print("밥먹자")
    print("메뉴는?")
    # 메뉴 변수 나열
    menulist = '돈가스', '떡튀순', '자장면'
    print("1.학식 2.분식 3.중식 4.랜덤")

    menu = input(str(i) + ".입력: ")
    #만약에 사용자가 입력한 값이 1 과 같으면

    if menu == '1':
        print("학식")

    if menu == '2':
        print("분식")

    if menu == '3':
        print("중식")

    if menu == '4':
        print("내 맘데로")
        print (random.choice(menulist))
    # 랜덤을 고르면 위 메뉴중에서 아무꺼나
#여기까지 반복
