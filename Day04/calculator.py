def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    else:
        return a/b
def power(a,b):
    if b==0:
        return 1
    else:
        return a**b