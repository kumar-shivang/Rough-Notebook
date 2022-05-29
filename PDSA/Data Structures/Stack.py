class Stack:
    def __init__(self):
        self.items = []

 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)

 
    def pop(self):
        return self.items.pop()
    def __str__(self):
        string = ""
        for i in self.items:
            string+= str(i)
            string += ", "
        return "[" + string[:-2] + "]"
a = Stack()
a.push(0)
a.push(2)
a.push(3)


