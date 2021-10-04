N = int(input())

a = list(map(int,input().split()))
A = [0] + a 

MOD = 998244353

from collections import Counter 

c = Counter()

'''
dp[1][j] = 1 when j == A1
dp[1][j] = 0 when j != A1

dp[i+1][j+A[i+1]%10] += dp[i][j]
dp[i+1][j*A[i+1]%10] += dp[i][j]

'''

dp = [[0] * (10) for _ in range(N+1)]

dp[1][A[1]] = 1 
for i in range(1,N):
    for j in range(10):
        dp[i+1][(j+A[i+1])%10] += dp[i][j]
        dp[i+1][(j+A[i+1])%10] %= MOD
        dp[i+1][(j*A[i+1])%10] += dp[i][j]
        dp[i+1][(j*A[i+1])%10] %= MOD 

for x in range(10):         
    print(dp[-1][x])

