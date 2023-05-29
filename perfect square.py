import math
Num = int(input("Enter the Number to check "))
root = math.sqrt(Num)
if int(root) ** 2 == Num:
    print(Num, "is a perfect square")
else:
    print(Num, "is not a perfect square")