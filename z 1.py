n=int(input("enter number"))
i=1
while i<=n:
    b=n
    while b>i:
        print("",end=" ")
        b=b-1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+2
i=2
while i<=n:
    b=1
    while b<=i:
        print("",end=" ")
        b=b+1
    j=n
    while j>i:
        print("*",end=" ")
        j=j-1
    print()
    i=i+2