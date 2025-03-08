class demo:
    def __init__(self):
        print(self)

    def __new__(s):
        print(s)


d=demo()
