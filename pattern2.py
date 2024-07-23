def pattern(N):
    for i in range(1,N+1):
        stars=i
        print("*"*stars)
    for k in range(N-1,0,-1):
        star=k
        print("*"*star)
num=int(input())
res=pattern(num)
