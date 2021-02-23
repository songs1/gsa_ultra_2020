#dist_2 = lambda a, b: sum([abs(ai - b[i]) ** 2 for i, ai in enumerate(a)])
#midpoint = lambda a, b: tuple((ai+b[i])/2 for i, ai in enumerate(a))

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

def solution(masses, locs):
    # First, sort masses and locs by lowest mass
    locs = sorted(locs, key = lambda l: masses[locs.index(l)])
    masses = sorted(masses)

    # N-1 fights occur
    for turn in range(len(masses) - 1):

        small_mass = masses.pop(0)
        small_loc = locs.pop(0)

        big_i = locs.index(min(locs, key=lambda l:\
            sum([abs(li - small_loc[i]) ** 2 for i, li in enumerate(l)]) )) #distance squared
        big_mass = masses.pop(big_i)
        big_loc = locs.pop(big_i)

        new_mass = small_mass + big_mass
        new_loc = tuple(int((si+big_loc[i])/2) for i, si in enumerate(small_loc)) #midpoint

        new_i = get_insert_index(new_mass, masses)
        masses.insert(new_i, new_mass)
        locs.insert(new_i, new_loc)

    #print('masses', masses, '\nlocs', locs)
    return sum(locs[0])

exm = [2, 5, 4]
exlocs = [(1, 4), (3, 1), (2, 6)]
print(solution(exm, exlocs))