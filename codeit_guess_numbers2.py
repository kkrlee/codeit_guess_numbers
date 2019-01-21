from random import randint
ANSWER = randint(1, 20)
NUM_TRIES = 4

tries = 0
guess = -1

while tries < NUM_TRIES and guess != ANSWER:

    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 : " % (NUM_TRIES - tries)))
    tries = tries + 1

    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")

if guess == ANSWER:
    print("축하합니다. %d번만에 숫자를 맞추셨습니다." % tries)

else:
    print("아쉽습니다. 정답은 %d였습니다." % ANSWER)
