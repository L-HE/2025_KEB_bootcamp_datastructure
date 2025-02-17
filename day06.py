def fibonacci_recursion(n) -> int:
    """
    피보나치 수 계산함수 (재귀함수 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    memo = {}

    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo = {n: fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)}
        return memo[n]



def fibonacci_loop(n) -> int:
    """
    피보나치 수 계산함수 (반복문 버전)
    :param n:
    :return: 피보나치 계산 결과 값
    """
    n_list=[0 ,1]
    for i in range(n+1):
        n_list.append(n_list[i] + n_list[i + 1])

    return n_list[n]

n = int(input())
#print(fibonacci_loop(n))
print(fibonacci_recursion(n))