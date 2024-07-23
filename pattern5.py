def pattern(n):
    current=1
    for i in range(0,n+1):
        for j in range(i):
            print(current,end=" ")
            current+=1
        print()
        
    
num=int(input())
res=pattern(num)
