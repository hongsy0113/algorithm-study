# 단어 변환
from collections import deque

def is_connected(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            if count == 2: return False
    if count == 1:
        return True

def bfs(words, start, visited, target):
    visited[start] = True
    queue = deque([(start, 0)])
    while queue:
        word, depth = queue.popleft()
        for w in words:
            if not w in visited and is_connected(word, w):
                if w == target:
                    return depth+1 
                queue.append((w, depth+1))


def solution(begin, target, words):
    answer = 0
    if not target in words:
        return 0
    visited = {}
    answer = bfs(words, begin, visited, target)
    return answer

words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin = "hit"
target = "cog"	
print(solution(begin, target, words))