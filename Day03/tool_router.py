from calculator import add,substract,multiply,divide
def calculator(operation,a,b):
    if operation=="add":
        return add(a,b)
    if operation=="substract":
        return substract(a,b)
    if operation=="multiply":
        return multiply(a,b)
    if operation=="divide":
        return divide(a,b)
op=str(input("Enter operation:"))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Result:",calculator(op,a,b))