
num = [ ] 
for x in range(1, 21):
    num.append(x) 
print("The list of numbers from 1 to 20 = " , num) 
for index, i in enumerate(num):
    if(i % 3 == 0): 
     del num[index] 
print("The list after deleting numbers" , num)