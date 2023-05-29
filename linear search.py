list=[]
n=int(input('enter the number of elements in the list:'))
for i in range(n):
    x=int(input('enter the number:'))
    list.append(x)
e=int(input("enter the elements to search:"))
pos=0
for i in range(n):
    if(list[n]==e):
        pos=i
        print('element is found at position %d in the list'%(pos+1))
    break
else:
    print('enter no element is found')

