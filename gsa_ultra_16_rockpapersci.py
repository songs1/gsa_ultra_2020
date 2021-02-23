type_adv = {'R':'P', 'P':'S', 'S':'R'}

def solution(a, b):
    '''first element = bottom of stack; last element = top of stack'''
    turn = 0
    a, b = list(a), list(b)
    while all((len(a), len(b))):
        turn += 1
        a_play, b_play = a.pop(), b.pop()
        if a_play is b_play: #draw
            a.insert(0, a_play)
            b.insert(0, b_play)
        elif a_play is type_adv[b_play]: # a wins
            a.insert(0, b_play)
            a.insert(0, a_play)
        else: #b wins
            b.insert(0, a_play)
            b.insert(0, b_play)
    return turn

print(solution('SRR', 'PPS'))