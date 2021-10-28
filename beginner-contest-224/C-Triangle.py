
def main():

    n = int(input())

    arr = []

    for i in range(n):
        arr.append(tuple(map(int,input().split())))

    ans = 0

    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                dy1 = arr[i][1] - arr[j][1]
                dy2 = arr[i][1] - arr[k][1]
                dx1 = arr[i][0] - arr[j][0]
                dx2 = arr[i][0] - arr[k][0]
                if dx1 * dy2 != dx2 * dy1:
                    ans += 1
    print(ans)  

if __name__ == '__main__':
    main()