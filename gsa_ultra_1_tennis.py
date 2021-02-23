from fractions import Fraction

def get_combos(elems, k):
    '''Given a list of elements (elems) and a specified combo size k (non-neg int),
    Return a set of tuples representing every unique k-length-combo of elements'''
    #Base cases
    if k == 1:
        return set((e,) for e in elems)
    #Recursive case
    n = len(elems)
    output = set()
    for i in range(n-k+1):
        for subcombo in get_combos(elems[i+1:],k-1):
            output.add( tuple( sorted( (elems[i],)+subcombo ) ) )
    return output

#t = lambda a, b, skills: Fraction(skills[a],skills[a]+skills[b])
def t(a,b,skills,mem):
    if (a,b) in mem:
        return mem[(a,b)], mem
    output = Fraction(skills[a],skills[a]+skills[b])
    mem[(a,b)] = output
    return output, mem

def tn(L,n,skills,mem):
    a, rest = L[0], L[1:]
    if n == 2: # Base case
        return t(a, rest[0], skills, mem)
    groupings = get_combos(rest, int((n/2)-1))
    output = 0
    for A_group in groupings:
        a_win, mem = tn([a]+list(A_group), n/2, skills, mem)
        B_group = [i for i in rest if i not in A_group]
        for b in B_group:
            B_losers = [j for j in B_group if j != b]
            b_win, mem = tn([b]+list(B_losers), n/2, skills, mem)
            ab, mem = t(a,b, skills, mem)
            output += ab * a_win * b_win
    return output/len(groupings), mem

def solution(skills):
    #print(f'skills input: {skills}')
    if 'Andy' not in skills:
        return '01'
    rest = [key for key in skills if key != 'Andy']
    out = str(tn(['Andy']+rest, len(skills), skills, {})[0]).split('/')
    return out[0]+out[1]

print('expect 2940764800, result:', solution({'Andy': 7, 'Novak': 5, 'Roger': 3, 'Rafael': 2}))