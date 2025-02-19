def pre_order(node):
    if node is None:
        print("-> end")
        return
    print(node.data, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        print("-> end")
        return
    in_order(node.left)
    print(node.data, end=' ')
    in_order(node.right)


def post_order(node):
    if node is None:
        print("-> end")
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=' ')


def inis_group(groups):
    global root

    node = TreeNode()
    node.data = groups[0]
    root = node

    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
    print("BST 구성 완료")


def insert_group(groups):
    for group in groups[::]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
        print(f"{group} 추가 완료")


def find_group(group):
    current = root
    while True:
        if group == current.data:
            print(f"{group}을/를 찾았습니다.")
            break
        elif group < current.data:
            if current.left is None:
                print(f"{group}이/가 존재하지 않습니다.")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{group}이/가 존재하지 않습니다.")
                break
            current = current.right


def delete_group(group):
    current = root
    parent = None
    while True:
        if group == current.data:
            if current.left == None and current.right == None:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
                del current

            elif current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                del current

            elif current.left == None and current.right != None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                del current

            print(f"{group}'이/가 삭제됨.")
            break

        elif group < current.data:
            if current.left is None:
                print(f"{group}이/가 존재하지 않습니다.")
                break
            parent = current
            current = current.left
        else:
            if current.right is None:
                print(f"{group}이/가 존재하지 않습니다.")
                break
            parent = current
            current = current.right


class TreeNode:

    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


if __name__ == "__main__":
    groups = input("그룹을 입력하세요: ").split(' ')
    inis_group(groups)
    while True:
        num = int(input("번호를 입력하세요.\n1) 삽입   2) 검색   3) 삭제   4) 종료   : "))
        if num == 1:
            i_group = input("삽입할 그룹을 입력하세요: ").split(' ')
            insert_group(i_group)
        elif num == 2:
            f_group = input("검색할 그룹을 입력하세요: ")
            find_group(f_group)
        elif num == 3:
            d_group = input("삭제할 그룹을 입력하세요: ")
            delete_group(d_group)
        elif num == 4:
            print("프로그램 종료")
            break
        else:
            print("다시 입력해주세요.")

