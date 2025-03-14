num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the second number: "))
sign = (input("Enter an operator of your choice: "))
if sign == "+":
    ans = (num1 * num2)
elif sign == "-":
    ans =(num1 - num2)
elif  sign == "*":
    ans = ( num1 * num2)
elif sign == "/":
    ans = (num1/num2)
else:
    print("invalid operator")

print( num1, sign, num2, "=", ans)


