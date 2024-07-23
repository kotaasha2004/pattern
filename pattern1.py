def pattern7(N):
    for i in range(1,N+1):
        leading_spaces=N-i
        stars=2*i-1
        row=" "*leading_spaces+"*"*stars
        print(row)
    for i in range(N,0,-1):
        leading_spaces=N-i
        stars=2*i-1
        row=" "*leading_spaces+"*"*stars
        print(row)
num=int(input())
res=pattern7(num)
