# No. 1213
# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213

# -문제
# 임한수와 임문빈은 서로 사랑하는 사이이다.
#
# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에,
# 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
#
# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데,
# 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
#
# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

# -입력
# 첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.

# -출력
# 첫째 줄에 문제의 정답을 출력한다.
# 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다.
# 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

# example input
#
# AABB

# -Solution
# 정렬, A~Z의 갯수를 파악 후 name_cnt[i] // 2 만큼 저장,
# 홀수일 경우 odd 값에 넣고 odd_cnt++
# odd_cnt의 값이 1개 이하일 경우 palin + odd + palin[::-1] 출력
# 아닐 경우 "I'm Sorry Hansoo" 출력

import sys
name = list(sys.stdin.readline().strip())

name_cnt = [0 for _ in range(26)]
odd = ''
odd_cnt = 0
palin = ''

name.sort()

for i in name:
    name_cnt[ord(i)-65] += 1

for i in range(26):
    palin += chr(i + 65) * (name_cnt[i] // 2)
    if name_cnt[i]%2 != 0:
        odd_cnt += 1
        odd = chr(i+65)

if odd_cnt <= 1:
    print(palin + odd + palin[::-1])
else:
    print("I'm Sorry Hansoo")