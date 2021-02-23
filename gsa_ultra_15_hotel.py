def hotel(rs):
    filled = [] # vacant rooms have value None or are beyond the last index
    parties = set()
    next_id = 0
    for action, number in rs:
        #print('filled', filled, 'before action', (action, number))
        if action == 'I':
            filled = check_in(number, filled, next_id)
            parties.add(next_id)
            next_id += 1
        else:
            filled = check_out(number, filled)
            parties.remove(number)
    return filled, parties

def check_in(req, filled, id):
    '''req = number of rooms requested'''
    for i in range(len(filled)):
        if not any (type(f) == int for f in filled[i:i+req]):
            filled[i:i+req] = [id]*req
            break
    else:
        filled.extend([id]*req)
    return filled

def check_out(id, filled):
    '''the room is officially checked out once the room cleaner cleans it'''
    cleaner = filled.index(id)
    while cleaner < len(filled) and filled[cleaner] is id:
        filled[cleaner] = None
        cleaner += 1
    while filled[-1] is None:
        filled.pop()
    return filled

def solution(n, rs):
    '''n is irrelevant since all requests are guaranteed possible'''
    filled, parties = hotel(rs)
    output = 0
    for p in parties:
        #print('add', p, '*', filled.index(p))
        output += p * filled.index(p)
    return output

print('example')
ex = [('I', 3), ('I', 3), ('O', 0), ('I', 4), ('I', 2), ('O', 2), ('I', 2)]
print(hotel(ex))
print(solution(10, ex))