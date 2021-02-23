def slow_bi_power(n):
    '''Return a list of all base 2 numbers with n digits'''
    if n is 1:
        return [str(i) for i in range(2)]
    return [str(i)+sub for i in range(2) for sub in bi_power(n-1)]

def bi_power(n):
    now, end = [0]*n, [1]*n
    while now != end:
        yield now
        for i in range(n-1, -1, -1):
            if now[i] is 0:
                now[i] = 1
                for j in range(i+1,n):
                    now[j] = 0
                break
    yield end

def fixed_prop(prop):
    '''replaces uppercase operators with lower case'''
    out = prop.replace('AND', 'and')
    out = out.replace('NOT', 'not')
    return out.replace('OR', 'or')

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solution(n, proposition):
    if n > 20:
        return 'skip ' + str(n)
    prop = fixed_prop(proposition)
    out = 0
    for assig in bi_power(n): #range over powerset
        #assig is a list
        for i, val in enumerate(assig): #assign variable values
            exec(f'{letters[i]} = {int(val)}')
        out += eval(prop)
    return out

ex = "A AND NOT NOT B OR C AND NOT (A OR B)"
#print(fixed_prop(ex))
print(solution(3, ex))

print('start')
for i in bi_power(20):
    pass
print('done')