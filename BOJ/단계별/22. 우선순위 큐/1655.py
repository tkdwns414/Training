import sys
import heapq

N = int(sys.stdin.readline())
left_h, right_h = [], []  # left_h는 최대 힙, right_h는 최소 힙

for i in range(N):
    x = int(sys.stdin.readline())

    # 두 힙의 길이가 최대한 같게 유지하기 위한 과정
    if len(left_h) == len(right_h):
        heapq.heappush(left_h, -x)
    else:
        heapq.heappush(right_h, x)

    if (left_h and right_h) and (-left_h[0] > right_h[0]):
        # 중앙값을 왼쪽 힙(최대 힙) 첫번째로 옮기기 위한 과정
        left_pop = -heapq.heappop(left_h)
        right_pop = heapq.heappop(right_h)

        heapq.heappush(left_h, -right_pop)
        heapq.heappush(right_h, left_pop)
    print(-left_h[0])


"""
중간값을 기준으로 나눠 넣어주는거임
숫자를 넣을 때 최대한 두 힙의 크기가 같게, 이미 같다면 왼쪽부터 채우기
근데 왼쪽 힙의 최상단에 있는 애가 오른쪽 힙의 최상단에 있는 애보다 크면 바꿔
(현재 수의 개수가 짝수일 때는 중간 두개 중 작은 수를 불러야 함 + 우리는 왼쪽 힙에 중간값을 저장할거거든)
다음게 들어왔을 때 크기 맞춰주는 작업을 먼저 하고 힙 정렬이 완료된 상태에서
중앙값을 갱신하기 위해서(작은 값을 왼쪽 힙으로 보내기 위해서)
둘이 비교하고 넘기는거임
그렇게 되면 왼쪽 힙에는 중간값보다 작은 값 + 중간값, 오른쪽 힙에는 중간값보다 큰 값만 남음
"""