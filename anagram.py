str1=input('enter  the string:')
str2=input("enter the 2nd string:")
def anagram(str1,str2):
    

    str1=sorted(str1)
    str2=sorted(str2)
    if(str1!=str2):
        return 0
    return 1
if(anagram(str1,str2)):
    print('the two string are anagram')
else:
    print("not anagram")
