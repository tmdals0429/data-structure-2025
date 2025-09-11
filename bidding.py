N = int(input())

stack = []
compare= []

for _ in range(N):
    s, n = input().split()
    n=int(n)
    if n in [x[1] for x in stack]:
        compare.append((s, n))
    else:
        stack.append((s, n))

for i in stack[:]:
    for j in compare:
        if i[1] == j[1]:
            stack.remove(i)
            break

stack.sort(key = lambda x: (-x[1]))

if(len(stack)==0):  
    print("NONE")
else:
    print(stack[0][0])