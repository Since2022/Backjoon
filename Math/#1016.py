# No. 1016
# 제곱 ㄴㄴ 수
# https://www.acmicpc.net/problem/1016

# -문제
# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다.
# 제곱수는 정수의 제곱이다.
# min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

# -입력
# 첫째 줄에 두 정수 min과 max가 주어진다.

# -출력
# 첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

# example input
#
# 1 10

# -Solution
# 에라토스테네스의 체 이용.
# * 제일 작은 소수인 2의 제곱(i**2)인 4의 배수가 되는 수들을 먼저 구해야 함.
# * n <= x <= m 을 만족하는 x를 구하기위해, n을 i**2 로 나눈 몫을 tmp에 저장.
# * tmp 값을 늘려가며 수들을 하나씩 제거.
# * tmp * (i**2) 값이 m을 넘을 경우, i의 값을 늘려서 위의 동작을 반복.
# 이후 리스트의 합을 출력.


n, m = map(int, input().split())
squ_map = [1]*(m - n + 1)

i = 2
while i*i <= m:
    tmp = n // i**2
    while tmp * (i ** 2) <= m:
        if 0 <= tmp * (i ** 2) - n <= m - n:
            squ_map[tmp * (i ** 2) - n] = 0
        tmp += 1
    i += 1

print(sum(squ_map))
