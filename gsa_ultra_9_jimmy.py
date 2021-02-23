#naive solution actually passed 6 test cases... not bad!
naive_solution = lambda a, qs: sum(max(a[i:j]) for i,j in qs)


#try with memory: passed 8 test cases, 7 the second time :/
def dict_solution(a, qs):
    mem = {} #maps (i,j) range to (max_index, max)
    out = []
    for i,j in qs:
        for mi, mj in mem:
            if i >= mi and j <= mj: #within
                max_index, max_val = mem[(mi,mj)]
                if i <= max_index < j:
                    out.append(max_val)
                    break
        else: #new case
            new_val = max(a[i:j])
            mem[(i,j)] = a.index(new_val), new_val
            out.append(new_val)
    return sum(out)


#try with sorted list instead of dictionary
#list is sorted by j-i range, reversed, so longest range first
#passes all 10 test cases!
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

def solution(a, qs):
    mem = [] # stores tuples of (i,j, max_i, max)
    mem_lengths = [] #stores j-i values
    out = []
    for i,j in qs:
        for mi, mj, max_i, max_val in mem:
            if mi <= i <= max_i and max_i < j <= mj: #within
                out.append(max_val)
                break
        else: #new case
            new_val = max(a[i:j])
            new_dex = i + a[i:j].index(new_val)
            insert_index = len(mem) - get_insert_index(j-i, mem_lengths)
                #reversed list order
            mem.insert(insert_index, (i,j,new_dex,new_val))
            mem_lengths.insert(insert_index, j-i)
            out.append(new_val)
    #print('out', out)
    return sum(out)


print('example 20, result:', solution([3, 6, 6, 1, 9, 8, 4, 7, 1, 1], [(1, 7), (5, 7), (0, 1)]))