from collections import Counter

def solution(N, stages):
    answer = [(i,0) for i in range(1, N+1)] #[(,0)] * (N+1)
    stage_count = Counter(stages)
    stage_count = sorted(stage_count.items())
    n = len(stages)
    for stage, count in stage_count:
        if stage >N:
            continue
        answer[stage-1] = (stage, count / n)
        n -= count
    answer.sort(key = lambda x: -x[1])
    answer = [answer[i][0] for i in range(len(answer))]
    return answer