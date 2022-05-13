# [1차] 추석 트래픽
#from datetime import datetime
import datetime
# 요청 class 정의
class Request:
    # line 로그를 인자로 받아
    # 시작 시간, 종료 시간, 처리 시간 datatime으로 저장
    def __init__(self, line):
        splited = list(line.split())
        finished_at = splited[1]
        duration = splited[2][:-1]
        datetime_obj = datetime.datetime.strptime(finished_at, '%H:%M:%S.%f')
        self.finished_at = datetime_obj
        self.duration = float(duration)
        self.started_at = self.finished_at - datetime.timedelta(seconds=self.duration-0.001)

    # 입력 구간에 해당 작업이 포함되는지 여부를 반환하는 함수
    def in_interval(self, start, end):
        # 시작 시간이 구간 안에 존재하는 경우
        if self.finished_at > start and self.finished_at <= end:
            return True
        # 종료 시간이 구간안에 존재하는 경우
        elif self.started_at >= start and self.started_at < end:
            return True
        # 시작 시간과 종료 시간이 모두 구간 밖에 존재하는 경우
        elif self.started_at <= start and self.finished_at >= end:
            return True
        else:
            return False

    def __str__(self):
        return f"start: {self.started_at} finished: {self.finished_at}  duration: {self.duration}"

def solution(lines):
    n = len(lines)
    # todo : 각 작업의 시작시간과 끝시간을 저장한다
    # lines를 분석해 시작 시간, 끝시간을 분석하는 함수 사용
    # 각 요청에 대한 요청 클래스를 만들어서 리스트로 관리
    requests = []
    for line in lines:
        request = Request(line)
        requests.append(request)
        print(request)
    # todo: 각 작업에 대해서 끝시간에 걸치도록 1초 구간을 설정하고 처리량을 구해본다
    max_amount = 0
    for i in range(n):
        amount = 0
        request = requests[i]
        # 각 작업에 끝시간 - 0.001초를 시작으로 하는 1초 구간을 설정
        start = request.finished_at - datetime.timedelta(seconds = 0.001)
        end = start + datetime.timedelta(seconds = 1.001)
        print(start, end)
        for j in range(n):

            if requests[j].in_interval(start, end):
                amount += 1

        max_amount = max(amount, max_amount)


    return max_amount

if __name__ == '__main__':

    lines =  [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
    lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    print(solution(lines))