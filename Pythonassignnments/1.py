''' Python Program for Menu based Calculator '''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Select operation.")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")

def add(x, y):
   return x + y

def sub(x, y):
   return x - y

def mul(x, y):
   return x * y
def div(x, y):
   return x / y

choice = input("Enter choice(1/2/3/4):")


if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", sub(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", mul(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", div(num1,num2))
else:
   print("Invalid input")