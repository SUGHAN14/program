def palindrome():
    string=input()
    reverse=string[::-1]
    print("string:",string)
    print("reverse:",reverse)
    if(string==reverse):
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
palindrome()
