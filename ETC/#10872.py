# No. 10872
# 팩토리얼
# https://www.acmicpc.net/problem/10872

# -문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# -출력
# 첫째 줄에 N!을 출력한다.

# example input
#
# 10

# -Solution
# 0과 1인 경우에만 1로 출력, 나머지는 팩토리얼의 규칙에 맞게 출력

n = int(input())
ans = 1

if n != 0:
    while 1 < n:
        ans *= n
        n -= 1

print(ans)
