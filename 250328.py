t, k, n = map(int, input().split())

for _ in range(t):
    down_layer = [i for i in range(1, n+1)]
    up_layer = []
    people = 0
    for _ in range(k):
        for j in range(n):
            people += down_layer[j]
            up_layer.insert(j, people)
            if len(up_layer) > n:
                up_layer.pop(-1)
            down_layer[j] = up_layer[j]
        people = 0
    print(up_layer[-1])