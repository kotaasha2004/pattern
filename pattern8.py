def main(n):
     for i in range(0,n):
        for j in range(n-i,n+1):
            print(chr(64+j),end=' ')
        print()
n=int(input())
res=main(n)
