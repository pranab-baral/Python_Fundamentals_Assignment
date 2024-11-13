def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y == 0:
        return "you can't enter zero"
    return x/y

def calculator():
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    choice = input("Enter your choice:")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if choice == 'a':
        calc=add(num1,num2)
        print("The calc is: ",calc)
    elif choice == 'b':
        calc=sub(num1,num2)
        print("The calc is: ",calc)
    elif choice == 'c':
        calc=mul(num1,num2)
        print("The calc is: ",calc)
    elif choice == 'd':
        calc=div(num1,num2)
        print("The calc is: ",calc)

calculator()

input("")

    