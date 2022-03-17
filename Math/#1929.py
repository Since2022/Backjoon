# No. 1929
# 소수 구하기
# https://www.acmicpc.net/problem/1929

# -문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# -출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# example input
#
# 3 16

# -Solution
# 에라토스테네스의 체를 이용.
# * 제일 작은 소수인 2부터 2의 배수가 되는 수들을 삭제,
# * a라는 소수가 아닌 수를 b * c로 만들 수 있을 때 (b <= c),
#   b와 c가 가장 큰 값을 갖기 위해서는 b <= a^-2 <= c를 만족하게 되므로,
#   2부터 a^-2 까지만 체크.
# 이후 해당되는 범위만 출력.

m, n = map(int, input().split())
prime = [True] * (n+1)
prime[0] = False
if m == 1:
    prime[1] = False

for i in range(2, int(n**0.5)+1):
    if prime[i]:
        for j in range(i+i, n+1, i):
            prime[j] = False

for i in range(m, n+1):
    if prime[i]:
        print(i)
