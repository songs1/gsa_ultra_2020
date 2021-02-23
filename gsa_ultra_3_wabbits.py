# GSA ultra 3-down (Wabbits)

from fractions import Fraction

def tri_power(n):
    '''Return a list of all base 3 numbers with n digits'''
    if n is 1:
        return [str(i) for i in range(2,-1,-1)]
    return [str(i)+sub for sub in tri_power(n-1) for i in range(2,-1,-1)]
#print(tri_power(2))

def valid_rows(phenos):
    '''Return a list corresponding to the relevant rows in the wabbits table'''
    elims = set()
    for i, ph in enumerate(phenos):
        if ph == 'R':
            elims = elims | set(cut+group for cut in range(3**i) for group in range(2*3**i, 3**len(phenos), 3**(i+1)))
            # eliminate the next 3^i rows (var "cut") every 3^i+1 rows (var "group") starting at row 2*3^i
        if ph == 'G':
            elims = elims | set(cut+group for cut in range(2*3**i) for group in range(0, 3**len(phenos), 3**(i+1)))
            # eliminate the next 2*3^i rows (var "cut") every 3^i+1 rows (var "groups") starting at row 0
    return [row for i,row in enumerate(tri_power(len(phenos))) if i not in elims]
#print(valid_rows(['?', 'R']))

def prob_table(n,d):
    '''Return a dictionary mapping (parent_genome, child_genome) tuples to probabilities'''
    p = Fraction(n,d)
    return {('2','2') : (1-p)**2,
            ('1','2') : p*(1-p),
            ('0','2') : p**2,
            ('2','1') : 2*p*(1-p),
            ('1','1') : p**2+(1-p)**2,
            ('0','1') : 2*p*(1-p),
            ('2','0') : p**2,
            ('1','0') : p*(1-p),
            ('0','0') : (1-p)**2}
#print(prob_table(1,5))

FIRST = {'0': Fraction(1,4), '1':Fraction(1,2), '2':Fraction(1,4)}

def naive_row_prob(row, table):
    '''Given a genome row (base 3 string), calculate its probability
    Assume the there is only one child per wabbit'''
    output = FIRST[row[0]]
    for i in range(len(row)-1):
        #print('i',i, type(i))
        output *= table[(row[i], row[i+1])]
    return output

def naive_answer(wab, n, d):
    '''Assume there is only one child per wabbit'''
    wab = sorted(wab, key=lambda a: a[0]) #sort by parent index
    table = prob_table(n,d)
    rows = valid_rows([ph for _,ph in wab])
    n, d = 0, 0
    for row in rows:
        greens = row.count('0') #how many green-eyed wabbits are in a row
        nrp = naive_row_prob(row, table)
        #print('for row', row, 'nrp', nrp, 'greens', greens)
        n += nrp * greens
        d += nrp
    return Fraction(n,d)

# FOR THE TRUE PROBLEM,
# CANNOT ASSUME THAT THE WABBITS INPUT WILL BE IN ORDER NOR THAT EACH WABBIT HAS ONLY A SINGLE CHILD
# THUS EACH ROW DOES NOT CORRESPOND TO A DIRECT LINEAGE
# WE WILL HAVE TO JUMP FROM INDEX TO INDEX

# HOWEVER, FOR NOW, TRY A NAIVE SOLUTION ASSUMING THAT THERE IS ONLY ONE WABBIT PER GENERATION,
# SO THAT EACH ROW DOES CORRESPOND TO A DIRECT LINEAGE

def solution(wab, n, d):
    out = str(naive_answer(wab, n, d)).split('/')
    return out[0]+out[1]

#print(solution([(-1, '?'), (0, 'R')], 1, 5)) # Example problem passed!

# EVEN THE NAIVE SOLUTION FAILED TO EARN ANY POINTS BC THE SERVER THREW AN ERROR (too much memory usage)
# PROBABLY BECAUSE I'M CREATING THE ENTIRE 3^n POWERSET... SIGH GUESS THAT DOESN'T WORK