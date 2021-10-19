n = int(input())
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))

MOD = 998244353

diff = [y-x+1 for x,y in zip(a,b)]
print(diff)

vals = []
for i in range(n-1):
    if b[i] > a[i+1]:
        vals.append(b[i]-a[i+1])
    else:
        vals.append(0)

print(vals)
new_diff = [0] + diff 
print(new_diff)

total_nums = [diff[0]]
for i in range(1,n):
    tmp = total_nums[i-1]*diff[i]
    extra = sum(range(1,vals[i-1]+1))
    print(extra,new_diff[i-1])
    tmp -= extra * (new_diff[i-1])
    total_nums.append(tmp)

print(total_nums)

print(total_nums[-1] % MOD)