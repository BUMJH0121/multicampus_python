first = {'id': 1, 'name': 'hong kildong', 'email': 'hong@mail.com', 'hp_num': '010-2343-9870'}
second = {'id': 2, 'name': 'lee soonsin', 'email': 'lee@mail.com', 'hp_num': '010-3333-5555'}
third = {'id': 3, 'name': 'jang youngsil', 'email': 'jang@mail.com', 'hp_num': '010-7777-1234'}
fourth = {'id': 4, 'name': 'king sejong', 'email': 'king@mail.com', 'hp_num': '010-4567-0987'}
list = [first, second, third, fourth]
for value in list:
    for k,v in value.items():
        print("{}: {}".format(k, v))