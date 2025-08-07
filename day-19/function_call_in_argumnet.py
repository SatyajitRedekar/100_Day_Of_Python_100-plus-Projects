def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def div(n1,n2):
    return n1 / n2
def mul(n1,n2):
    return n1 * n2

def calculate(n1,n2,fun):# it directly converts fun -> passed val
    return fun(n1, n2)

print(calculate(5,10,mul)) # mul is trigger the function