K = int(input())
arr = [list(map(int, input().split())) for _ in range(K)]

t = int(input())

c1_idx = 0
c2_idx = K // 2

dir1 = 1  # c1 시계방향
dir2 = -1  # c2 반시계방향

dist = []
for i in range(K):
    x1, y1 = arr[i]
    x2, y2 = arr[(i+1) % K]
    dist.append(abs(x1 - x2) + abs(y1 - y2))  # 맨해튼 거리 (1초에 1칸 이동 가정)

def robot_init(idx, direction):
    if direction == 1:
        next_idx = (idx + 1) % K
    else:
        next_idx = (idx - 1 + K) % K
    x1, y1 = arr[idx]
    x2, y2 = arr[next_idx]
    dx = 0
    dy = 0
    if x2 > x1:
        dx = 1
    elif x2 < x1:
        dx = -1
    if y2 > y1:
        dy = 1
    elif y2 < y1:
        dy = -1
    return {
        "pos": [x1, y1],
        "cur_idx": idx,
        "next_idx": next_idx,
        "dist_moved": 0,
        "dx": dx,
        "dy": dy
    }

c1 = robot_init(c1_idx, dir1)
c2 = robot_init(c2_idx, dir2)

def move_robot(robot, direction):
    robot["dist_moved"] += 1
    robot["pos"][0] += robot["dx"]
    robot["pos"][1] += robot["dy"]
    edge_length = dist[robot["cur_idx"]]
    if robot["dist_moved"] == edge_length:
        robot["cur_idx"] = robot["next_idx"]
        if direction == 1:
            robot["next_idx"] = (robot["cur_idx"] + 1) % K
        else:
            robot["next_idx"] = (robot["cur_idx"] - 1 + K) % K
        x1, y1 = arr[robot["cur_idx"]]
        x2, y2 = arr[robot["next_idx"]]
        dx = 0
        dy = 0
        if x2 > x1:
            dx = 1
        elif x2 < x1:
            dx = -1
        if y2 > y1:
            dy = 1
        elif y2 < y1:
            dy = -1
        robot["dx"] = dx
        robot["dy"] = dy
        robot["dist_moved"] = 0

def same_position(r1, r2):
    return r1["pos"][0] == r2["pos"][0] and r1["pos"][1] == r2["pos"][1]

for _ in range(t):
    move_robot(c1, dir1)
    move_robot(c2, dir2)
    if same_position(c1, c2):
        dir1 *= -1
        dir2 *= -1

print(c1["pos"][0], c1["pos"][1])
print(c2["pos"][0], c2["pos"][1])
