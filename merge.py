# python3

import math
import sys

class Answer(object):

    def __init__(self,value):
        self.answer = value


def Parent(value):

    if value != parent[value]:
        parent[value] = Parent(parent[value])

    return parent[value]

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1]*n
parent = list(range(0, n))
ans = Answer(max(lines))


def merge(destination, source):

    dest = Parent(destination)
    sour = Parent(source)

    if dest == sour:
        print(ans.answer)

    elif rank[dest] > rank[sour]: # was if

        parent[sour] = dest
        lines[dest] = lines[sour] + lines[dest]
        lines[sour] = 0
        ans.answer = max(ans.answer, lines[dest])
        print(ans.answer)
    else:

        parent[dest] = sour
        lines[sour] = lines[sour] + lines[dest]
        lines[dest] = 0
        ans.answer = max(ans.answer, lines[sour])
        print(ans.answer)

        if rank[dest] == rank[sour]:
            rank[sour] += 1

    # print(ans.answer)
    

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    # print(ans.answer)
