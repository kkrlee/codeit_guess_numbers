from random import randint
ANSWER = randint(1, 20)
tries = 4

while tries <= 4:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 : " % tries))
    tries = tries - 1

    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")
    else:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (4 - tries))
        break
    if tries == 0:
        print("아쉽습니다. 정답은 %d였습니다." % ANSWER)
        break
