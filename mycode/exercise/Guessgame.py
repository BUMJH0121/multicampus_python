import random

guess_number = str(random.randint(1,100))
count = 1
while True:
    print("숫자를 입력해 주세요")
    user_input = input()
    if guess_number == user_input:
        print("{}번 만에 맞추셨습니다.".format(count))
        break
    elif guess_number > user_input:
        print("숫자가 너무 작습니다.")
        count = count+1
    else:
        print("숫자가 너무 큽니다.")
        count = count+1