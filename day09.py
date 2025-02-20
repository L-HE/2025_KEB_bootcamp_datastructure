def pre_order(node):
    """

    :param node:
    :return:
    """
    if node is None:
        print("-> end")
        return
    print(node.data, end=' ')
    pre_order(node.left)
    pre_order(node.right)


def insert():


def delete():


def search():


if __name__ == '__main__':
    root = None
    while True:
        num = int(input("기능을 선택해주세요.\n1)삽입   2)삭제   3)검색   4)전위순회   5)종료:   "))
        if num == 1:
            values = input("삽입할 데이터: ").split(' ')
            insert(root, values)
        elif num == 2:
            value = input("삭제할 데이터: ")
            delete(root, value)
        elif num == 3:
            value = input("검색할 데이터: ")
            search(root, value)
        elif num == 4:
            pre_order(root)
        elif num == 5:
            print("프로그램 종료")
            break
        else:
            print("다시 입력해주세요.")