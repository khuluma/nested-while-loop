a=int(input("enter number"))
i=65
k=65
while i<=a:
    j=65
    while j<=i:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1