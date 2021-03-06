# No. 1789
# 수들의 합
# https://www.acmicpc.net/problem/1789

# -문제
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# -입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# -출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

# example input
#
# 200

# -Solution
# 1~2 -> N=1, 3~5 => N=2, 6~9 => N=4, 10 ~ 15 => N=5, ...
#
# S >= 1, 1+2, 1+2+3, 1+2+3+4, 1+2+3+4+5, ...

s = int(input())

n = 0
sum = 0
i = 0

while s >= sum:
    i += 1
    sum += i

print(i-1)