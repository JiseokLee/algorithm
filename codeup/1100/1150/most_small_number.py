
num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if(num1 < num2):
    if(num1 <= num3):
        print(num1)
    else:
        print(num3)
else:
    if(num2 <= num3):
        print(num2)
    else:
        print(num3)
