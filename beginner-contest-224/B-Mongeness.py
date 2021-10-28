l,w = map(int,input().split())

arr = []

for i in range(l):
    arr.append(list(map(int,input().split())))

def func():
    for i in range(l):
        for j in range(i+1,l):
            for k in range(w):
                for t in range(k+1,w):
                    if arr[i][k] + arr[j][t] > arr[j][k] + arr[i][t]:
                        return False 
    return True 

if func():
    print('Yes')
else:
    print('No')