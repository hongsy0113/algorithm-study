def solution(p):
    answer = ''
    
    # 1.
    if not p:
        return p
    # 2. 
    left_cnt = 0
    right_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_cnt += 1
        elif p[i] == ')':
            right_cnt += 1
        if left_cnt == right_cnt:
            break
    u = p[:i+1]
    v = p[i+1:]
    
    #  u가 올바른 괄호인지 확인
    u_cnt = 0
    u_correct = True
    for i in range(len(u)):
        if u[i] == '(':
            u_cnt += 1
        elif u[i] == ')':
            u_cnt -= 1
        if u_cnt < 0:        
            u_correct = False
            break
    # 3. u가 올바른 괄호라면
    if u_correct :
        return u + solution(v)
    # 4. u가 올바른 괄호가 아니라면
    else:
        new_str = '(' + solution(v) + ')'
        for i in range(1, len(u)-1):
            if u[i] == '(':
                new_str += ')'
            else:
                new_str += '('
        return new_str
