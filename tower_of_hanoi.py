'''def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print(f'Move disk 1 from rod {source} to rod {target}.')  
        return  
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print(f'Move disk {disks} from rod {source} to rod {target}.')  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
disks = int(input('Enter the number of disks: '))  
tower_of_hanoi(disks, 'A', 'B', 'C')
'''


def tower_of_hanoi(n,source,target,auxiliary):
    if n==1 :
        print(f"Move disk 1 from{source}to{target}")
        return
    tower_of_hanoi(n-1,source,auxiliary,target)
    print(f"move disk{n} from{source}to{target}")
    tower_of_hanoi(n-1,auxiliary,source,target)
tower_of_hanoi(3,'A','B','C')
        


'''
def search(list,tar):
    for ind,ele in enumerate(list):
        if ele == tar:
            return ind
    return -1
list=[1,2,3]
tar_ele=2

res=search(list,tar_ele)
if res!= -1:
    print(f"the ele{tar_ele}is found at index{res}")
else:
    print(f"element{tar_ele}is not")
'''