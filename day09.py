# Assignment1
# find_vertex 함수에 BFS를 적용하시오.
from collections import deque


class Graph:
	def __init__(self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g) :
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(name_ary[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(name_ary[row], end=' ')
        for col in range(g.SIZE):
            print(f"{g.graph[row][col]:2}", end=' ')
        print()
    print()


def dfs(g, current, find_vtx, visited):
    visited = []
    visited.append(current)

    # 찾고자 하는 vtx를 찾은 경우
    if current == find_vtx:
        return True

    # 간선으로 연결되어 있으면서, vertex가 방문한 적 없음
    for vertex in range(g.SIZE):
        if g.graph[current][vertex] != 0 and vertex not in visited:
            if dfs(g, vertex, find_vtx, visited):
                return True
    return False


def find_vertex(g, find_vtx):
    """
    with bfs
    :param g:
    :param find_vtx:
    :return:
    """
    visited = []
    queue = deque([0])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.append(current)
        if current == find_vtx:
            return True
        for i in range(g.SIZE):
            if g.graph[current][i] != 0 and i not in visited:
                queue.append(i)
    return False




#G1 = None
name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

g_size = 6
G1 = Graph(g_size)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print_graph(G1)

# 간선 목록 만들기 [weight, start, end]
edge_ary = []
for i in range(g_size) :
    for k in range(g_size) :
        if G1.graph[i][k] != 0 :
            edge_ary.append([G1.graph[i][k], i, k])

print(edge_ary, len(edge_ary))

# weight 순으로 목록 내림차순 정렬
from operator import itemgetter
edge_ary = sorted(edge_ary, key = itemgetter(0), reverse = True)

print(edge_ary, len(edge_ary))

# 중복 edge 제거
new_ary = []
for i in range(0, len(edge_ary), 2) :
    new_ary.append(edge_ary[i])

print(new_ary, len(new_ary))

index = 0
while len(new_ary) > g_size - 1:	# edge가 'vertex-1'일 때까지 반복
    start = new_ary[index][1]
    end = new_ary[index][2]
    saveCost = new_ary[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = find_vertex(G1, start)
    endYN = find_vertex(G1, end)

    if startYN and endYN :
        del new_ary[index]
    else :
        G1.graph[start][end] = saveCost
        G1.graph[end][start] = saveCost
        index += 1

print_graph(G1)