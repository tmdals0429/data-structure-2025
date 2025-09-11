import bisect
import sys

input = sys.stdin.readline

Waitroom = [] #2차원 구조의 의자
k = 0

def binary_f(x):    # Waitroom 에 있는 각 리스트의 첫번째 값을 통해 이진 탐색한 후 들어가야할 곳의 index 값 찾는 함수
    lo, hi = 0, len(Waitroom)
    while lo < hi:
        mid = (lo + hi) // 2
        if Waitroom[mid][0] > x: hi = mid
        else: lo = mid + 1
    return lo

def split_v(idx): # 만약 waitroom 안의 리스트길이가 2k가 되면 k이후 요소들은 right 변수에 넣어놓고 k이전 요소들은 그대로 waitroom[idx]에 두고 right 변수를 waitroom[idx+1]에 주면서 split 하게하는 함수
    if len(Waitroom[idx]) == 2 * k:
        right = Waitroom[idx][k:]
        Waitroom[idx] = Waitroom[idx][:k]
        Waitroom.insert(idx + 1, right)

def append_n(x): # waitroom 이 비어잇으면 그냥 append 하고 이진 탐색하여 어디 들어갈지 찾고 bisect.insort_left 을 이용해 자동정렬하면서 그 리스트에 넣어버리기
    if not Waitroom: 
        Waitroom.append([x])
        split_v(0)
        return
    j = binary_f(x)
    idx = j - 1 if j > 0 else 0
    bisect.insort_left(Waitroom[idx], x)
    split_v(idx)

def erase_n(x): #waitroom에 없으면 걍 넘겨, 위치 찾아서 그 값 없애, 그 의자 자리에 아무도 없으면 그 자리 삭제까지
    if not Waitroom: return
    j = binary_f(x)
    idx = j - 1 if j > 0 else 0
    b = Waitroom[idx]
    pos = bisect.bisect_left(b, x)
    if b[pos] == x:
        b.pop(pos)
        if not b: Waitroom.pop(idx)

N, k = map(int, input().split())

for _ in range(N):
    pm, num = input().split()
    num = int(num)
    if pm == '+': append_n(num)
    else: erase_n(num)

for ans in Waitroom:
    if ans: print(ans[0])


# runtime_error 을 없애기 위해 def append_n(x): 에서  split_v(0), return 로 똑같은 값 삽입하는 것 방지
# 인덱스 초과 방지를 위해 erase_n 에 if pos < len(b) pos 의 범위 체크까지 해줘야함
# 이거 안하면 20점, 13점