
def solution(n, k, num_str):
    num_list = []
    length = n//4
    # 시작 index를 어디로 할 것인지(rotate)
    for i in range(length):
        # 해당 rotation에서 몇번째 수인지
        for j in range(4):
            start_idx = i + (j * length)
            end_idx = start_idx + length
            num = int(num_str[start_idx:end_idx], 16)
            num_list.append(num)
    # 중복제거 및 정렬
    num_list = list(set(num_list))
    num_list.sort(reverse=True)
    # k번째 수 반환
    return num_list[k-1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    num_str = input()
    num_str = (num_str + num_str[:n//4]).lower()
    print(f'#{test_case} {solution(n, k, num_str)}')
