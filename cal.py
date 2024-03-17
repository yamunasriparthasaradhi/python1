def addition(P,Q):
    return P + Q
def subtraction(P,Q):
    return P - Q
def multiplication(P,Q):
    return P * Q
def division(P,Q):
    return P / Q
def floordivision(P,Q):
    return P // Q
print("please select the operation you need:")
print("a.Add")
print("b.Sub")
print("c.Mul")
print("d.Div")
print("e.Floordiv")
user_choice=input("enter the choice(a/b/c/d/e):")
num1=int(input("you are requested to enter first number:"))
num2=int(input("you are requested to enter second number:"))
if user_choice == 'a':
    print(num1,"+",num2,"=",addition(num1,num2))
elif user_choice == 'b':
    print(num1,"-",num2,"=",subtraction(num1,num2))
elif user_choice == 'c':
    print(num1,"*",num2,"=",multiplication(num1,num2))
elif user_choice == 'd':
    print(num1,"/",num2,"=",division(num1,num2))
elif user_choice == 'e':
    print(num1,"//",num2,"=",floordivision(num1,num2))
else:
    print("sorry!! The given number is INVALID")

          
    
