# No. 1427
# 소트인사이드
# https://www.acmicpc.net/problem/1427

# -문제
# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# -입력
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# -출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

# example input
#
# 2143

# -Solution
# str로 입력 받은 이후에 정렬 후 출력

n = list(str(input()))
n.sort(reverse=True)

print(''.join(n))