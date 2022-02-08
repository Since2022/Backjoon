# No. 16953
# A -> B
# https://www.acmicpc.net/problem/16953

# -문제
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
#
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# -입력
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

# -출력
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

# example input
#
# 2 162

# -Solution
# B를 A로 변환한다.
# B의 1의 자리가 1일경우 1을 뺀다.
# B가 2의 배수이면 나눗셈을 한다.
# 둘 다 할 수 없을 경우 -1을 출력한다.

a, b = map(int, input().split())
cnt = 0

while a < b:
    cnt += 1
    if b%10 == 1:
        b //= 10
    elif b%2 == 0:
        b //= 2
    else:
        break

if a != b:
    print(-1)
else:
    print(cnt+1)
