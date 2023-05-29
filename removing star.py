s = input()
ans =[]
for i in s:
    if i != '*':
        ans+=i
    else:
        ans.pop()
print(ans)
'''s = input()
ans = []
for i in s:
    if i == '*':
        ans.pop()
    else:
        ans += [i]
        
print("".join(ans))

s=input("enter the input:")
a=[]
for i in s:
    if i=='*':
        s.remove(a)
        s.remove()
    print(s)
'''

