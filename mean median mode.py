list1=[2,1,3,1,2]

def mean():
    print('mean')
    print('the mean of the list is:',sum(list1)/len(list1))
mean()


def mode():
    l2=[]
    l3=[]
    for i in list1:
        if i not in l2:
            l2.append(i)
        else :
            l3.append(i)
    print(list(l3))
mode()