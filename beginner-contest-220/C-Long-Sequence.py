N = int(input())

A  = list(map(int,input().split(' ')))

x = int(input())

sum1 = sum(A)

times = N * (x // sum1)
cnt = 0
res = x  % sum1 
for i in range(N):
    if res < A[i]:
        break 
    else:
        res -= A[i]
        cnt += 1
print(str(times+cnt+1))
    