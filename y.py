n=int(input("enter number"))
i=1
while i<=n:
    j=5
    while j>=i:
        print("",end=" ")
        j=j-1
    l=1
    while l<=i:
        print("*",end=" ")
        l=l+1
    print()
    i=i+2