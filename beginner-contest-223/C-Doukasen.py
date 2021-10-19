n = int(input())
arr = [] * n
nums = [] * n
for i in range(n):
  x,y = list(map(int,input().split(' ')))
  arr.append(x/y)
  nums.append((x,y))


time = sum(arr) / 2
cur = 0
idx = 0

while time >= 0:
  if time - arr[idx] < 0:
    break 
  time -= arr[idx]
  cur += nums[idx][0]
  idx += 1

cur += time * nums[idx][1]

print(cur)
