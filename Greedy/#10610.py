# No. 10610
# 30
# https://www.acmicpc.net/problem/10610

# -문제
# 어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다.
# 미르코는 30이란 수를 존경하기 때문에,
# 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
#
# 미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

# -입력
# N을 입력받는다. N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

# -출력
# 미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

# example input
#
# 80875542

# -Solution
# 가지고 있는 수들을 재배열.
# if 0 in list(n): --> 10의 배수
# list의 합 %3 == 0 --> 3의 배수

n = list(map(int, input()))

sum = 0

for i in n:
    sum += i

if sum % 3 == 0 and 0 in n:
    for i in sorted(n,reverse=True):
        print(i,end='')
else:
    print(-1)