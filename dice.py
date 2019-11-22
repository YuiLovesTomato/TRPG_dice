#-*- coding:utf-8 -*-
import random as rand

class exitCommand(Exception):
    pass

def listen():
    print("=" * 50)
    temp = input(": ")
    if temp == "exit":
        raise exitCommand
    time = int(temp[0])
    size = int(temp[2:])
    if time == 2:
        v1 = rand.randrange(1,size)
        v2 = rand.randrange(1,size)
        print("%d + %d = %d" % (v1, v2, v1+v2))
    if time == 1:
        v1 = rand.randrange(1, size)
        print("%d" % v1)


print("=" * 50)
print("TRPG dice roller by @yuilovestomato")
print("굴릴 주사위 값을 입력해주세요. ex) 2d6, 1d4")
print("나온 값에 능력수정치는 계산되어 있지 않습니다. 상황에 맞게 더해주세요.")
print("종료하시려면 exit를 입력하세요.")

try:
    while True:
        listen()
except exitCommand:
    pass

