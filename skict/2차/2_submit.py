# process 를 읽어서 정보를 리턴한다.

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
        if working: count += 1
        if len(working) == 0 and len(waiting) == 0 and process_idx == len(processes):
            break
    answer_dict = sorted(answer_dict.items())
    for _, value in answer_dict:
        answer.append(value)
    answer.append(str(count))
    return answer
