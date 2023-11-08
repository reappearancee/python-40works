"""숫자 맞추기 게임""" 
import random

### 1-1번
# random_number = random.randint(1, 100)
# print(random_number)

### 1-2번
# random_number = random.randint(1, 100)
# game_count = 1
# while True:
#     my_num = int(input("1~100사이의 숫자를 입력해주세요. :"))
#     if my_num > random_number:
#         print("다운")
#     elif my_num < random_number:
#         print("업")
#     elif my_num == random_number:
#         print(f"정답입니다. {game_count}회 만에 맞췄습니다.")
#         break
#     game_count = game_count + 1

### 1-3번
random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_num = int(input("1~100사이의 숫자를 입력해주세요. :"))

        if my_num > random_number:
            print("다운")
        elif my_num < random_number:
            print("업")
        elif my_num == random_number:
            print(f"정답입니다. {game_count}회 시도하셨네요.")
            break
        game_count = game_count + 1
    except:
        print("숫자를 입력해주세요.")
