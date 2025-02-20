def pre_order(node):
    if node is None:
        print("-> end")
        return
    print(node.data, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def inis_group(value) -> object:
    """
    입력받은 값의 리스트를 받아, 이진탐색트리로 구성하는 함수
    :param groups: 입력받은 값의 리스트
    :return:
    """
    # global root
    #
    # node = TreeNode()
    # node.data = groups[0]
    # root = node

    for value in values[1:]:
        node = TreeNode()
        node.data = value
        current = root
        while True:
            if value < current.data:
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
    """
    삽입할 값의 리스트를 받아 기존의 트리에 추가하는 함수
    :param groups: 삽입할 값의 리스트
    :return: 추가된 이진탐색트리
    """
    # for group in groups[::]:
    #     node = TreeNode()
    #     node.data = group
    #     current = root
    #     while True:
    #         if group < current.data:
    #             if current.left is None:
    #                 current.left = node
    #                 break
    #             current = current.left
    #         else:
    #             if current.right is None:
    #                 current.right = node
    #                 break
    #             current = current.right
    #     print(f"{group} 추가 완료")
    def insert(root, value):
        for value in values[::]:
            if root is None:
                node = TreeNode()
                node.data = value
                return node

            if value < root.data:
                root.left = insert(root.left, value)
            else:
                root.right = insert(root.right, value)
            return root


# def insert(root, data):
#     """
#     (?)준영씨의 코드 루팡
#     :param root: 클래스 객체 초기 설정
#     :param data: 입력받은 수
#     :return:
#     """
#     if root is None:
#         node = TreeNode()
#         node.data = data
#         return node
#
#     if data < root.data:
#         root.left = insert(root.left, data)
#     else:
#         root.right = insert(root.right, data)
#     return root


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


def delete(value):
    current = root
    parent = None
    while True:
        if value == current.data:
            if current.left is None and current.right is None:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
                del current

            elif current.left is not None and current.right is None:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                del current

            elif current.left is None and current.right is not None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
                del current

            elif current.left is not None and current.right is not None:
                child = current.left
                if parent.left == current:
                    parent.left = child.right
                    
                else:
                    parent.right = child.right
                    while True:
                        if child.right is None:
                            child.right = current.right
                            break
                        child = child.right
                    del current


            print(f"{value}'이/가 삭제됨.")
            break

        elif value < current.data:
            if current.left is None:
                print(f"{value}이/가 존재하지 않습니다.")
                break
            parent = current
            current = current.left
        else:
            if current.right is None:
                print(f"{value}이/가 존재하지 않습니다.")
                break
            parent = current
            current = current.right


class TreeNode:

    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


if __name__ == "__main__":
    values = input("그룹을 입력하세요: ").split(' ')

    global root

    node = TreeNode()
    node.data = values[0]
    root = node
    inis_group(values)

    while True:
        num = int(input("번호를 입력하세요.\n1) 삽입   2) 검색   3) 삭제   4) 전위순회   5) 종료   : "))
        if num == 1:
            i_group = input("삽입할 그룹을 입력하세요: ").split(' ')
            insert_group(i_group)
        elif num == 2:
            f_group = input("검색할 그룹을 입력하세요: ")
            search(root, f_group)
        elif num == 3:
            d_group = input("삭제할 그룹을 입력하세요: ")
            delete(d_group)
        elif num == 4:
            pre_order(root)
        elif num == 5:
            print("프로그램 종료")
            break
        else:
            print("다시 입력해주세요.")

