from bisect import bisect_right

K = int(input())
cnt = 0 #한바퀴 거리
lst = [] # 각 꼭짓점 갈때마다 거리
arr = [list(map(int,input().split())) for _ in range(K)]
row = (arr[0][1] == arr[1][1]) #오른쪽으로 가는지, 위로가는지
for i in range(K-1):
    if i==0:
        if row:
            l = abs(arr[1][0] - arr[0][0])
        else:
            l = abs(arr[1][1] - arr[0][1])
    elif i%2==0:
        if row:
            l=abs(arr[i+1][0] - arr[i-1][0])
        else:
            l = abs(arr[i+1][1] - arr[i-1][1])
    else:
        if row:
            l = abs(arr[i+1][1] - arr[i-1][1])
        else:
            l = abs(arr[i+1][0] - arr[i-1][0])
    cnt += l
    lst.append(cnt)

cnt += abs(arr[K-1][1] - arr[0][1]) if arr[K-1][0] == arr[0][0] else abs(arr[K-1][0] - arr[0][0])

lst.append(cnt)

t = map(int,input().split())
for i in t:
    second = i % cnt
    id = bisect_right(lst, second) #이분탐색

    if id == 0:
        plus = second
    else:
        plus = second - lst[id-1]

    lap = (id+1)%K

    if (id%2==1) ^ row:
        if arr[id][0] > arr[lap][0]:
            s= arr[id][0] - plus
        else:
            s= arr[id][0] + plus
        print(s,arr[id][1])
    else:
        if arr[id][1] > arr[lap][1]:
            s = arr[id][1] - plus
        else:
            s = arr[id][1] + plus
        print(arr[id][0],s)