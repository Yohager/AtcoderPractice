new_dict = list(str(input()))
N = int(input())
arr = []
for i in range(N):
  arr.append(str(input()))

old_dict = list(chr(i+96) for i in range(1,27))

d = dict(zip(new_dict,old_dict))
print(d)

new_arr = []

for elem in arr:
    tmp = ''
    for a in elem:
        tmp += d[a]
    new_arr.append(tmp)

total_arr = list(zip(new_arr,arr))

total_arr.sort(key=lambda x:x[0])

for x in total_arr:
    print(x[1])