N = list(str(input()))

ans = 0

from itertools import combinations

for c in combinations(N,len(N)//2):
    tmp = list(c)
    n1,n2 = [],[]
    for x in N:
        if x in tmp:
            n1.append(x)
            tmp.remove(x)
        else:
            n2.append(x)
    n1.sort(reverse=True)
    n2.sort(reverse=True)
    if n1[0] == '0' or n2[0] == '0':
        continue 
    ans = max(ans,int(''.join(n1)) * int(''.join(n2)))
print(ans)

# use_nums = []
# for x in nums:
#     if x != 0:
#         use_nums.append(x)

# cnt = len(nums) - len(use_nums)

# use_nums.sort(reverse=True)

# if len(use_nums) % 2 == 0:
#     #useful nums has even counts half makes the maximum num 
#     h1,h2 = '',''
#     for i in range(0,len(use_nums),2):
#         h1 += str(use_nums[i])
#     for j in range(1,len(use_nums),2):
#         h2 += str(use_nums[j])
    
#     mulnum = int(h1) * int(h2)
#     print(int(str(mulnum)+'0'*cnt))
# else:
#     h1,h2 = '',''
#     for i in range(0,len(use_nums)-1,2):
#         h1 += str(use_nums[i])
#     for j in range(1,len(use_nums)-1,2):
#         h2 += str(use_nums[j])
    
#     maxval1 = int(h1+str(use_nums[-1])) * int(h2)
#     maxval2 = int(h1) * int(h2+str(use_nums[-1]))
#     maxval = max(maxval1,maxval2)
#     print(int(str(maxval)+'0'*cnt))


