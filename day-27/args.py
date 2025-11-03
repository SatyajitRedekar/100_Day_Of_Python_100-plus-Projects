def hello(*args):# Take as much as posible inputs in just one args
    for x in args:
        print(x)

hello(3,2,4,)

# Exercise - Unlimited positional arguments
# todo we called the positional args because of access depend on position
def add(*args) :
   print(sum(args))


add(1,2,3,4)