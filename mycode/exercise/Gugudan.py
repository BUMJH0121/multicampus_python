while True:
    print("구구단 몇 단을 계산할까요(1~9)?")
    user_input = int(input())
    if user_input == 0:
        print("구구단 게임을 종료합니다.")
        break
    else:
        print("구구단 {}단을 계산합니다.".format(user_input))
        for i in range(1 ,10):
            print("{}X{}={}".format(user_input, i, user_input*i))