str1 = str(input())
str2 = str(input())
str3 = str(input())

d = {
  '1': str1,
  '2': str2,
  '3': str3,
}

t = str(input())
ans = ''
for x in t:
  ans += d[x]
  
print(ans)
