'''
print("what is your name")
var1=input()
print("your name is:",var1)
print("enter your age")
age=int(input())
if age > 18:
    print("your are eligible")
elif age == 18:
    print("we must deside on that")
elif age < 18:
    print("your are not eligible")
print("what is your gender")
gender=input()
    
'''
t = int(input())       
#run a loop to accept 't' inputs
for i in range(t):     
    #accept 2 integers on the 1st line of each test case
    A, B = map(int,input().split())      
    #accept 3 integers on the 2nd line of each test case
    C, D, E = map(int,input().split())   
    #output the 5 integers on a single line for each test case    
    print(A, B, C, D, E)