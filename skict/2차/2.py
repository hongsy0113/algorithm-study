# process 를 읽어서 정보를 리턴한다.
from torch import result_type


def parse_process(process):
    splited = process.split(' ')
    command = splited[0]
    t1 = int(splited[1])
    t2 = int(splited[2])
    A = int(splited[3])
    B = int(splited[4])
    C = int(splited[5]) if command == 'write' else -1
    
    return command, t1, t2, A, B, C

#
def is_possible(command, working, waiting):
    if command == 'read':
        for p in waiting:
            if p.command == 'write':
                return False
        if len(working) == 0:
            return True
        else:
            for p in working:
                if p.command == 'write':
                    return False
            return True
        # elif len(working)==1 and working[0].command == 'write':
        #     return False
        # elif len(working)==1 and working[0].command == 'read':
        #     return True
    elif command == 'write':
        return not (len(working) > 0)

class Process:
    def __init__(self, process):
        splited = process.split(' ')
        self.command = splited[0]
        self.t1 = int(splited[1])
        self.t2 = int(splited[2])
        self.A = int(splited[3])
        self.B = int(splited[4])
        self.C = (splited[5]) if self.command == 'write' else -1
        self.status = 'not_started'
        self.finish_time = -1
        self.read_value = ''

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.command, self.t1, self.t2, self.A, self.B, self.C)

    def get_status(self):
        return self.status    

    def get_command(self):
        return self.command 

    def to_work(self, working, time):
        self.status = 'working'
        self.finish_time = time + self.t2
        working.append(self)

    def to_wait(self, waiting):
        self.status = 'waiting'
        waiting.append(self)
    
    def work (self, arr, answer_dict):
        if self.command == 'read':
            result = arr[self.A:self.B+1]
            self.read_value = ''.join(result)
            answer_dict[self.t1] = self.read_value
        elif self.command == 'write':
            for i in range(self.A, self.B+1):
                arr[i] = self.C
        return arr



def solution(arr, processes):
    answer = []
    answer_dict ={}

    working = []
    waiting = []
    time = 0
    count = 0 
    process_idx = 0
    while True:
        time+=1
        if process_idx < len(processes):
            process = Process(processes[process_idx])
            if process.t1 <= time:
                if is_possible(process.get_command(), working, waiting):
                    process.to_work(working, time)
                else:
                    process.to_wait(waiting)
                process_idx += 1
        work_remove= []
        wait_remove= []
        for work_process in working:
            if work_process.finish_time == time:
                arr = work_process.work(arr,answer_dict)
                work_remove.append(work_process)
                # working.remove(work_process)
        for work_process in work_remove:
            working.remove(work_process)
        for wait_process in waiting:
            if is_possible(wait_process.get_command(), working, waiting):
                wait_process.to_work(working, time)
                wait_remove.append(wait_process)
                #waiting.remove(wait_process)
        for wait_process in wait_remove:
            waiting.remove(wait_process)
        print('time:', time)
        print('working:', [(work.command, work.t1, work.t2) for work in working])
        print('waiting:', [(wait.command, wait.t1, wait.t2) for wait in waiting])
        if working: count += 1
        if len(working) == 0 and len(waiting) == 0 and process_idx == len(processes):
            break
    answer_dict = sorted(answer_dict.items())
    for key, value in answer_dict:
        answer.append(value)
    answer.append(str(count))
    return answer














arr = ["1","2","4","3","3","4","1","5"]
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]

arr = ["1","1","1","1","1","1","1"]
processes = ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
print(solution(arr, processes))