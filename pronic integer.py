def pronic_number():
    number=int(input("enter the pronic number:"))
    f=0
    for i in range(number):
        if i*(i+1)==number:
            f=1
    if f==1:
        print("it it a pronic number")
    else:
        print("it is not a pronic number")
pronic_number()

