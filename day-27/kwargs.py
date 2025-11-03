# todo this is known as the many keyword args
def calculate(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)

calculate(add=1,mul=2,div=3)

# Example for how this kwargs saves to the files
class Car:
    def __init__(self,**kwargs):
        self.model = kwargs.get("model") # using get is because of if in kwargs the value
        self.car = kwargs.get("car")     # in not present then it will return NONE rather
        self.color = kwargs.get("color") # crash the program

car = Car(color="green")
print(car.color)
print(car.model)