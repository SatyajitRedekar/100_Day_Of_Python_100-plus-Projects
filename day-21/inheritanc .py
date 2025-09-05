class Animal :
    def __init__(self):
        self.eye = "two"
        self.mouth = True

    def breath(self):
        print("inhale", "exhale")

class Dog(Animal) :
    def __init__(self):
        super().__init__()
    def swim(self):
        print("dog can swim")
        print("but dog can't ")

nemo = Dog()
nemo.swim()
nemo.breath()