# 파일 입출력

import random

#list 이름은 복수형. 중복이니까?
# 상받은 사람 제거하기 방법 3가지 : del, remove(element), pop(key)
students = []

try:
    #file pointer / 오픈할 때 많이 씀
    # 'r' : 읽기 전용
    file = input("File name = ")
    fp = open(file, 'r')
    readme_list = fp.readlines()
    # 나누는 기준을 '_'로 설정
    rls = readme_list[0].split('_')
    print(readme_list)
    print(rls)
    # 열면 닫아야함
    fp.close()
except FileNotFoundError as err:
    print(f"{file} is not exist. {err}")