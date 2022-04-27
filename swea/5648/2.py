### 정수 좌표가 아닌 칸에서 만나는 것도 고려하기 위해 좌표를 곱하기 2해서 고려
import sys

sys.stdin = open("input_big.txt", "r")

# 상(0), 하(1), 좌(2), 우(3)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 원자에 대한 클래스
class Atom:
    def __init__(self, x, y, d, k):
        self.x = x
        self.y = y
        self.d = d
        self.k = k

    # 1초동안 원자를 이동시키는 함수
    def move(self):
        self.x += dx[self.d]
        self.y += dy[self.d]

    # 원자 소멸시키는 함수
    # 에너지 총합을 증가시키고, 전체 atom에서 자신 지운다
    def disapper(self):
        global total_energy
        total_energy += self.k
        atom_set.remove(self)

    def __str__(self):
        return f"atom pos: ({self.x}, {self.y}), direction: {self.d}"

def solution(atom_set):
    # 최대 4000초 반복
    # 정확히는 4000초가 아니라 0.5초씩 2000번
    for _ in range(4000):
        ## atom_set이 비었다면, 즉 모든 원자가 소멸되었다면 break
        if len(atom_set) == 0:
            break

        ## 좌표에 대한 딕셔너리 정의 및 초기화
        pos_atom_dict = {}
        ## 각 초마다 atom을 이동시킨다
        for atom in atom_set:
            atom.move()
            nx, ny = atom.x, atom.y
            # 해당 좌표에 이미 원자가 있다면 list에 append
            if (nx, ny) in pos_atom_dict:
                pos_atom_dict[(nx, ny)].append(atom)
            # 해당 좌표에 원자 없다면 새로 리스트 만듬
            else:
                pos_atom_dict[(nx, ny)] = [atom]
        ### 이동 후 좌표를 key로 하고 class의 리스트를 value로 하는 dictionary를 만들어
        ### 겹치는 원소를 소멸시킨다
        # 딕셔너리를 반복문 돌면서 길이 2이상인 value list 있다면 소멸 작업한다
        for pos, atom_list in pos_atom_dict.items():
            if len(atom_list) >= 2:
                for atom in atom_list:
                    atom.disapper()



if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())

        # TODO: init 함수 필요!
        # 총 에너지, 원자들의 set을 전역변수로 관리
        total_energy = 0
        atom_set = set([])

        for _ in range(N):
            # 원자 입력 받기
            x, y, d, k = map(int, input().split())
            # 좌표 중간에서 만나는 것도 고려하기 위해 좌표계를 2배 확대해서 생각하기 위해 곱하기 2
            atom = Atom(2 * x, 2 * y, d, k)
            atom_set.add(atom)
            teme = atom

        ### solution 함수 호출
        solution(atom_set)
        # 결과 출력
        print(f'#{test_case} {total_energy}')
