def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j),end=" ")
        print()
num=int(input())
res=pattern(num)
