
from random import randint ## 모듈에서랜덤함수 가져오기.

print ("welcome tp 카지노!")
user_choice =int(input("choose number!"))
pc_choice = randint(1,50) ## i imported this
## 내장함수! 

playing =True

while playing:
    user_choice =int(input("choose number!"))
    if user_choice== pc_choice:
        print("니가 이겼다")
        playing =False
    elif user_choice> pc_choice:
        print("더 낮게! ")
    elif user_choice<pc_choice:
        print("더 높게! ")
        