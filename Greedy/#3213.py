# No. 3213
# 피자
# https://www.acmicpc.net/problem/3213

# -문제
# 오늘은 상근이의 생일이다. 상근이는 친구들과 피자를 먹으러 갔다.
#
# 상근이의 친구들은 매우 어려서 피자 한 판을 먹을 수 없다.
# 하지만, 각 친구들은 자신이 먹을 수 있는 피자의 양을 알고 있다.
#
# 친구들이 먹을 수 있는 피자의 양은 항상 1/4, 1/2, 3/4 중 하나이다.
#
#  피자를 최소 몇 판 시키면 모든 친구들이 각자 피자를 자신이 먹을 수 있는 양만큼 먹을 수 있는지 구하시오.
#  상근이는 피자를 먹지 않으며, 모든 친구들이 정확히 한 조각씩 피자를 가져야 한다.

# -입력
# 첫째 줄에 친구의 수 N이 주어진다. (1 ≤ N ≤ 10,000)
#
# 다음 N개 줄에는 각 친구가 먹을 수 있는 피자의 양이 주어진다.
# 이 값은 항상 분수이며, 1/4, 1/2, 3/4중 하나이다.

# -출력
# 피자를 최소 몇 판 시키면 모든 친구들이 자신이 먹을 수 있는 양만큼 먹는지 출력한다.

# example input
#
# 3
# 1/2
# 3/4
# 3/4

# -Solution
# 1/4 와 3/4 를 1판으로 만든다.
# 1/4를 올림으로 합쳐서 1/2로 만든다.
# 1/2를 올림으로 합쳐서 1판으로 만든다.

import math

def minval(a, b):
    if a < b:
        return a
    else:
        return b

n = int(input())
pieces = [0, 0, 0]

for i in range(n):
    piece = str(input())
    if piece == '1/2':
        pieces[0] += 1
    elif piece == '1/4':
        pieces[1] += 1
    elif piece == '3/4':
        pieces[2] += 1

tmp = minval(pieces[1], pieces[2])
pieces[1] -= tmp
pieces[2] -= tmp
ans = tmp + pieces[2]

pieces[0] += math.ceil(pieces[1]/2)

ans += math.ceil(pieces[0]/2)

print(ans)











