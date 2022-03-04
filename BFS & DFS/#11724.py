# No. 11724
# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

# -문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# -출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# example input
#
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# -Solution
# 입력 받은 값을 그래프에 대칭으로 넣는다.
# queue를 통해 bfs를 구현하여 visit을 체크하고 풀이한다.

from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


ans = 0
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)

