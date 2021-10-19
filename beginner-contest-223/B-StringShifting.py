s = input()

res = set()
res.add(s)
n = len(s)
tmp1 = s
for i in range(n):
  tmp2 = tmp1[1:] + tmp1[0]
  tmp1 = tmp2
  res.add(tmp2)

ans = sorted(list(res))
print(ans[0])
print(ans[-1])