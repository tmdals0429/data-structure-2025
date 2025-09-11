from bisect import bisect_right,bisect_left

K = int(input())
cnt = 0
lst = [0]
arr = [list(map(int, input().split())) for _ in range(K)]
row = (arr[0][1] == arr[1][1])

for i in range(K-1):
    if i==0:
        if row: l = abs(arr[1][0] - arr[0][0])
        else: l = abs(arr[1][1] - arr[0][1])
    elif i%2==0:
        if row: l=abs(arr[i+1][0] - arr[i-1][0])
        else: l = abs(arr[i+1][1] - arr[i-1][1])
    else:
        if row: l = abs(arr[i+1][1] - arr[i-1][1])
        else: l = abs(arr[i+1][0] - arr[i-1][0])
    cnt += l
    lst.append(cnt)

cnt += abs(arr[K - 1][1] - arr[0][1]) if arr[K - 1][0] == arr[0][0] else abs(arr[K - 1][0] - arr[0][0])
lst.append(cnt)

t = int(input())

def pos(second):
    second %= cnt
    idx = bisect_right(lst, second) - 1 
    plus = second - lst[idx]
    if arr[idx][1] == arr[(idx+1)%K][1]:
        x = 1 if arr[(idx+1)%K][0] > arr[idx][0] else -1
        return arr[idx][0] + x*plus, arr[idx][1]
    else: 
        y = 1 if arr[(idx+1)%K][1] > arr[idx][1] else -1
        return arr[idx][0], arr[idx][1] + y*plus

p1 = 0
p2 = lst[K//2-1]

s1 = pos(p1 + t)
s2 = pos(p2 - t)

d = (p2-p1)

#c_cnt -> 만난 횟수
if 2*t < d:
    c_cnt = 0
else:
    c_cnt = 1 + (2*t - d) // cnt

if c_cnt % 2 == 1:
    print(s2[0],s2[1])
    print(s1[0],s1[1])
else:
    print(s1[0],s1[1])
    print(s2[0],s2[1])