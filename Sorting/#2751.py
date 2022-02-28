# No. 2751
# 수 정렬하기 2
# https://www.acmicpc.net/problem/2750

# -문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 수가 주어진다.
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# -출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# example input
#
# 5
# 5
# 2
# 3
# 4
# 1

# -Solution
# 입력 받은 이후에 정렬 후 출력

import sys
input = sys.stdin.readline

n = int(input())
ans = []

for i in range(n):
    ans.append(int(input()))

ans.sort()

for i in ans:
    print(i)