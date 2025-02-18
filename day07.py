#상속 받는 것 아니면 () 생략, class 이름은 대문자로 시작.
class Stack:
    def __init__(self):
        self.items = list()

    def push(self, data):
        self.items.append(data)

    def pop(self) -> object:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> object:
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


s1 = Stack()
s1.push(-9)
s1.push(1)
s1.push(977)
print(s1.pop())
print(s1.peek())
print(s1.peek())