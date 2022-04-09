# 멀쩡한 사각형

## 최대공약수 구하는 함수 넣자
def gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지를 y에 대입
        x, y = y, x % y
    return x

## w, h 가 서로소라고 가정
# w,h 직사각형에서 대각선에 의해 제외되는 개수 반환
def _solution (w,h):
    res = 0
    mid_w = (w+1) // 2 
    mid_h = (h+1) // 2 
    cur_w , cur_h = 1, 1
    if w==h:
        return 1
    elif w == 1: return h
    elif h == 1: return w
    else:
        if w>h:
            # turn 0 이면 가로 차례, 1이면 세로
            turn = 0 
            step = w // h 
            while cur_w <= mid_w and cur_h <= mid_h:
                if turn == 0:
                    cur_w += step
                    res += step
                else:
                    cur_h += 1
                    res += 1
                turn = (turn + 1) % 2
        else:
            # turn 0 이면 가로 차례, 1이면 세로
            turn = 1
            step = h // w 
            while cur_w <= mid_w and cur_h <= mid_h:
                if turn == 0:
                    cur_w += 1
                    res += 1
                else:
                    cur_h += step
                    res += step
                turn = (turn + 1) % 2
        if w % 2 == 0 or h % 2 ==0 :
            res *=2 
        else:
            res = res*2 - 1
    return res

def solution(w,h):
    
    answer = 1
    # w, h의 최대공약수 구한다
    g = gcd(w,h)
    nw = w//g
    nh = h // g
    # w,h 가 같은 경우
    answer = w*h - (_solution(nw, nh) * g)
    return answer