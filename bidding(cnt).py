from collections import Counter

N = int(input())
arr = []
only = []

for _ in range(N):
    s, n = input().split()
    arr.append((s, int(n))) 

cnt = Counter()
for name, score in arr:
    cnt[score] += 1

for name, score in arr:
    if cnt[score] == 1:
        only.append((name,score))

only.sort(key = lambda x: (-x[1]))

if len(only) == 0:
    print("None")
else:
    print(only[0][0])
