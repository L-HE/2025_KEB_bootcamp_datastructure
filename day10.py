# Assignment
# Baekjoon 1158 요세푸스 : 수업시간에 설명(큐(데크), 원형링크드리스트)한 방법 외의 방법으로 문제를 해결하고 깃허브에 업로드 하시오.


def jose(n, k, current = 0) -> list:
    members = [i for i in range(1, n + 1)]
    res = []
    del_num = None

    if len(members) == 2:
        a = members.pop(current)
        res.append(members.pop())
        res.append(a)
        return res
    else:
        if current == 0:
            del_num = (k-len(members))%(len(members)-1) + 1
            if del_num == len(members) + 1:
                current = 0
            else:
                current = del_num
            res.append(members.pop(del_num))
            return jose(n, k, current)
        else:
            del_num = (k-len(members))%(len(members)-1) - 1
            if del_num == len(members) + 1:
                current = 0
            else:
                current = del_num
            res.append(members.pop(del_num))
            return jose(n, k, current)




if __name__ == "__main__":
    j = list(map(int, input().split(' ')))
    n = j[0]
    k = j[1]

    print(jose(n, k))