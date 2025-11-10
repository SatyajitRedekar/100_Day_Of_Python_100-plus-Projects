
# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print(number)

    def fizz_buzz(target):
        for number in range(1, target + 1):
            # use and (not or)
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz")
            # use elif (not if)
            elif number % 3 == 0:
                print("Fizz")
            # use elif (not if)
            elif number % 5 == 0:
                print("Buzz")
            else:
                # remove square brackets []
                print(number)

    # import random
    # import maths
    #
    #
    # def mutate(a_list):
    #     b_list = []
    #     new_item = 0
    #     for item in a_list:
    #         new_item = item * 2
    #         new_item += random.randint(1, 3)
    #         new_item = maths.add(new_item, item)
    #         b_list.append(new_item)
    #     print(b_list)
    #
    #
    # mutate([1, 2, 3, 5, 8, 13])