def dec_oct(n) -> int:
    if n == 0:
        return ""
    else:
        return dec_oct(n // 8) + str(n % 8)


n = int(input())
print(dec_oct(n))