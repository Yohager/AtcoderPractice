s = str(input())
t = str(input())

if len(s) != len(t):
    print('No')

n = len(s)

pos = -1
for i in range(n):
    if s[i] != t[i]:
        pos = i 
        break 

if pos == -1:
    print('Yes')
else:
    arr = s[:i] + s[i+1] + s[i] + s[i+2:]           

    if arr == t:
        print('Yes')
    else:
        print('No')
