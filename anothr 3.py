a=int(input("enter number"))
i=1
while i<=a:
    n=a-i
    while n>0:
        print("",end=" ")
        n=n-1
    j=1
    while j<=i:
        if j==i  or j==1 :
            print("*",end=" ")
        elif j<=i and i==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1
