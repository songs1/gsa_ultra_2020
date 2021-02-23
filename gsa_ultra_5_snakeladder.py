#Attempt a monte carlo simulation approach

import random
def solution(N, snakes, ladders, m=200):
    '''Simulate a snakes and ladders game m times;
    return the average game lenght, truncated to the nearest int'''
    results = []
    portals = {ss:se for ss,se in snakes}
    portals.update({ls:le for ls,le in ladders})
    portal_starts = set(s for s in portals)
    for i in range(m):
        turn, square = 0, 0
        while square < N-1:
            turn += 1
            square += random.choice(range(1,7))
            if square in portal_starts:
                square = portals[square]
        results.append(turn)
    return int(sum(results)/m)

for i in range(10):
    print(solution(100, [(4,1), (49, 48), (20, 10), (15, 5)], [(3, 45), (89, 96), (12, 47), (89, 102)]))