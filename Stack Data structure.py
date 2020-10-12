class stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.x = x
        self.stack.append(self.x)
        print(self.stack)

    def pop(self):
        if len(self.stack)== 0:
            print("stack is empty")
        else:
            return self.stack.pop()

ob = stack()
ob.push(20)
ob.push(30)
ob.pop()
print(ob.stack)