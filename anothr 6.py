n=int(input("enter number"))
i=1
while i<=n:
    j=1
    while j<=5:
        if i==3 or i+j==4 or j-i==2 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1