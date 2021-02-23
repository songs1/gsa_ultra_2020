def get_insert_index(x, L, i=0):
    if len(L) == 0: return 0
    if len(L) == 1:
        if x <= L[0]:
            return i
        return i + 1
    mid = len(L) // 2
    if x == L[mid]: return i + mid
    elif x < L[mid]: return get_insert_index(x, L[:mid], i)
    else: return get_insert_index(x, L[mid:], i + mid)

def solution(a, b):
    agenda = [(0,0,0,0)] # position, cost, a_index, b_index
    heurs = [0]

    while agenda:
        #print(terms, costs)
        t, c, ai, bi = agenda.pop(0)
        h = heurs.pop(0)

        if (ai is len(a)) and (bi is len(b)): # Win
            return c

        if ai < len(a):
            ca = c + abs(t - a[ai])
            ha = ca + abs(a[ai] - a[-1])
            i = get_insert_index(ha, heurs)
            agenda.insert(i, (a[ai], ca, ai+1, bi))
            heurs.insert(i, ha)

        if bi < len(b):
            cb = c + abs(t - b[bi])
            hb = cb + abs(b[bi] - b[-1])
            i = get_insert_index(hb, heurs)
            agenda.insert(i, (b[bi], cb, ai, bi+1))
            heurs.insert(i, hb)

'''
def greedy(a, b):
    time, pos = 0, 0
    while len(a) and len(b):
        if abs(pos-a[0]) < abs(pos-b[0]):
            time += abs(pos-a[0])
            pos = a.pop(0)
        else:
            time += abs(pos-b[0])
            pos = b.pop(0)
        while len(a):
            time += abs(pos - a[0])
            pos = a.pop(0)
        while len(b):
            time += abs(pos - b[0])
            pos = b.pop(0)
    return time
'''

ex_a = [5, 3, 10, 6]
ex_b = [9, 7, 12]
print('expected 24')
#print('greedy', greedy(ex_a, ex_b))
print('search', solution(ex_a, ex_b))