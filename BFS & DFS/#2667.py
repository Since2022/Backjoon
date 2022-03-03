# No. 2667
# 단지 번호 붙이기
# https://www.acmicpc.net/problem/2667

# -문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.

# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# -입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# -출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# example input
#
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# -Solution
# 데이터를 입력받고, queue를 통해 BFS로 완전탐색을 한다.
# 좌표 이동하는데 있어서 값이 벗어날 경우 탐색을 취소한다.

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    if graph[x][y] == '0':
        return False

    queue = deque()
    queue.append([x,y])
    cnt = 0

    while queue:
        x, y = queue.popleft()
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        if graph[x][y] == '0':
            continue
        else:
            graph[x][y] = '0'
            cnt += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if [nx,ny] not in queue:
                    queue.append([nx,ny])

    if cnt:
        ans.append(cnt)


n = int(input())
graph = []
ans = []

for i in range(n):
    graph.append(list(map(str, input().strip())))

for i in range(n):
    if '1' in graph[i]:
        for j in range(n):
            if graph[i][j] == '1':
                bfs(i, j)

ans.sort()
print(len(ans))
for i in ans:
    print(i)