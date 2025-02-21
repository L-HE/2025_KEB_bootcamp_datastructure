# Assignment
# v3.1) v2.8 코드의 출력 방식을 BFS로 변경하시오.
from collections import deque


def insert(root, value):
    if root is None:
        node = TreeNode()
        node.data = value
        return node

    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def delete(root, value):
    if root is None:
        return root
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:  # 자식이 두 개인 경우
            root.data = find_min(root.right).data
            root.right = delete(root.right, root.data)
    return root


def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def search(root, value):
    current = root
    while current:
        if value == current.data:
            return current
        elif value < current.data:
            current = current.left
        else:
            current = current.right
    return None


def bfs(node):
    if node is None:
        print("트리가 존재하지 않습니다.")
        return
    current = node
    queue = deque([current.data])
    while queue:
        node = queue.popleft()
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left.data)
        if node.right:
            queue.append(node.right.data)



class TreeNode:

    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


if __name__ == '__main__':
    root = None
    while True:
        num = int(input("기능을 선택해주세요.\n1)삽입   2)삭제   3)검색   4)bfs   5)종료:   "))
        if num == 1:
            value = input("삽입할 데이터: ")
            insert(root, value)
            print(f"{value} 삽입 완료")
        elif num == 2:
            value = input("삭제할 데이터: ")
            if search(root, value):
                root = delete(root, value)
                print(f"{value} 삭제 완료")
            else:
                print(f"{value}은(는) 트리에 존재하지 않습니다.")
        elif num == 3:
            value = input("검색할 데이터: ")
            if search(root, value):
                print(f"{value}을(를) 찾았습니다.")
            else:
                print(f"{value}이(가) 존재하지 않습니다.")
        elif num == 4:
            bfs(root)
        elif num == 5:
            print("프로그램 종료")
            break
        else:
            print("다시 입력해주세요.")