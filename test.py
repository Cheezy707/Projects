lis = ["bread", "toast", "loaf"]
dic = {x:y for x,y in enumerate(lis)}

print(dic)

class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):                # what print() shows
        return f"bark"

    def __int__(self):
        return 4

    def __repr__(self):               # what the debugger/REPL shows
        return f"Dog(name={self.name!r})"

rex = Dog("Rex")

print(int(rex)*2)