n=int(input("enter number"))
i=65
while i<=n:
    j=65
    while j<=i:
        print(chr(j),end=" ")
        j=j+1
    print()
    i=i+1