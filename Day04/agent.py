from calculator import add,substract,multiply,divide,power
def agent(operation,a,b):
    if operation.lower()=="add":
        return add(a,b)
    elif operation.lower()=="substract":
        return substract(a,b)
    elif operation.lower()=="multiply":
        return multiply(a,b)
    elif operation.lower()=="divide":
        return divide(a,b)
    elif operation.lower()=="power":
        return power(a,b)
operation=str(input("What operation do you want?"))
a=int(input("Enter the first number:"))
b=int(input("Enter second number:"))
result=agent(operation,a,b)
print("Agent result:",result)


#challenge 1
calc=[]
def agent1(calculation):
    calc=calculation.split()
    operation=calc[1]
    a=int(calc[0])
    b=int(calc[2])
    if operation=="+":
        return add(a,b)
    if operation=="-":
        return substract(a,b)
    if operation=="*":
        return multiply(a,b)
    if operation=="/":
        return divide(a,b)
calculation=input("Enter your calculation:")
result=agent1(calculation)    
print(result)


#challenge 2
def agent2(operation,a,b):
    if operation.lower()=="add":
        return add(a,b)
    if operation.lower()=="substract":
        return substract(a,b)
    if operation.lower()=="multiply":
        return multiply(a,b)
    if operation.lower()=="divide":
        return divide(a,b)
while True:
    operation=str(input("What operation do you want?"))
    if operation.lower()=="exit":
        exit(0)
    a=int(input("Enter the first number:"))
    b=int(input("Enter second number:"))
    result=agent2(operation,a,b)
    print("Agent result:",result)