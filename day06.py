# 파일 입출력

import random
import csv

try:
    #file pointer / 오픈할 때 많이 씀
    # 'r' : 읽기 전용
    with open('students.csv', 'r') as fp:
        students_list = fp.readlines()
        students_list.remove("이상혁\n")

        for _ in range(3):
            random_pick = random.choice(students_list)
            print(random_pick, end='')
            students_list.remove(random_pick)
        #print(random.choice(students_list), end='')
except FileNotFoundError as err:
    print(err)