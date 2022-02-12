# No. 1700
# 멀티탭 스케줄링
# https://www.acmicpc.net/problem/1700

# -문제
# 기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다.
# 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고,
# 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.
#
# 예를 들어 구멍이 세 개 달린 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면,
#
# 1. 키보드
# 2. 헤어드라이기
# 3. 핸드폰 충전기
# 4. 디지털 카메라 충전기
# 5. 키보드
# 6. 헤어드라이기

# 키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음
# 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로
# 플러그는 한 번만 빼면 된다.

# -입력
# 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다.
# 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다.
# 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다.

# -출력
# 하나씩 플러그를 빼는 최소의 횟수를 출력하시오.

# example input
#
# 2 7
# 2 3 2 3 1 2 7

# -Solution
# 플러그가 멀티탭에 꽂혀있는지 확인해서 n만큼 넣습니다.
# 멀티탭이 꽉 차있을 경우 멀티탭에 꽂힌 것들을 플러그에서의 인덱스값으로 찾고,
# 인덱스 값들이 큰 것부터 뽑도록 합니다.
# 멀티탭에서 제외할 때마다 카운트를 올립니다.

n, k = map(int,input().split())
plug = list(map(int, input().split()))
multitap = []
cnt = 0

for i in range(k):
    if plug[i] in multitap:
        continue

    if len(multitap) < n:
        multitap.append(plug[i])
        continue

    idxs = []
    for j in range(n):
        try:
            idx = plug[i:].index(multitap[j])
        except:
            idx = 101
        idxs.append(idx)

    del multitap[idxs.index(max(idxs))]
    multitap.append(plug[i])
    cnt += 1

print(cnt)




