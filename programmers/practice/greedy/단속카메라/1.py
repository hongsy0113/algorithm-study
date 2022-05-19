def solution(routes):
    # routes를 진출 시점 순서대로 정렬
    routes.sort(key = lambda x : x[1])
    cur_camera = routes[0][1]
    # 가장 앞에 있는 차량의 진출 지점에 카메라를 설치

    idx = 1
    answer = 1
    # 해당 카메라로 커버 불가능할때까지 하나씩 확인
    # 기존 카메라로 커버 불가능해지면 새롭게 해당 차량의 진출 지점으로 카메라 설치
    for i in range(1, len(routes)):
        start, end = routes[i][0], routes[i][1]
        # 현재 카메라로 커버 가능하면 skip
        if start<=cur_camera<=end:
            continue
        # 현재 카메라로 커버 불가능하면 새로 카메라 설치
        else:
            answer += 1
            cur_camera = end

    return answer


if __name__ == '__main__':
    routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]

    solution(routes)