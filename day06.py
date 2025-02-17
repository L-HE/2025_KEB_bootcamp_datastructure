# v1.2) https://github.com/inhadeepblue/2024_KEB_datastructure_algorithm
# v0.7 guess number 예제를 자동화하고 로그파일(guess.txt)을 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록 한다.
import random


def choose_number(num1, num2) -> int :
    avg = (num2 + num1) // 2
    return avg


low = 1
high = 100
answer = random.randint(low, high)
chance = 7

with open('guess.txt', 'w') as fp:
    while chance != 0:
        guess = choose_number(low, high)
        fp.write(f'Guess number is {guess}.')
        if guess == answer:
            print(f'You win. Answer is {answer}')
            fp.write(f'You win. Answer is {answer}')
            break
        elif guess > answer:
            chance = chance - 1
            print(f'{guess} is bigger. Chance left : {chance}')
            fp.write(f'{guess} is bigger. Chance left : {chance}\n')
            high = guess
        else:
            chance = chance - 1
            print(f'{guess} is lower. Chance left : {chance}')
            fp.write(f'{guess} is lower. Chance left : {chance}\n')
            low = guess
    else:
        print(f'You lost. Answer is {answer}')