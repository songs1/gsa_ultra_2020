# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:01:13 2020

@author: Samuel
"""
#GSA Ultra 2020 2-down (Parkour)

# See field of smiles problems from 6.009 Practice Quiz 1C

def jump(platform, last, fin):
    '''fin = 0 for the final jump, 1 otherwise
    
    return a tuple of 
        - the lowest time to get to the platform from the last col
        - the pace after moving'''
    output = []
    for h, (time, pace, _) in last.items():
        
        if 0 < h - platform < 6: #lower
            faster = pace - 1*(pace>1)
            output.append((time + faster, faster, h))
            
        elif 0 < platform - h < 6: #higher
            slower = pace + 1*(pace<10)
            output.append((time + slower, slower, h))
            
        elif platform == h:
            output.append((time + pace, pace, h))
    
    if not output:
        return None
    return min(output, key=lambda a: a[0]+fin*a[1])
            

def solution(ps):
    last = {s:(5,5,None) for s in ps[0]} #maps platform to best time, pace
    for i, col in enumerate(ps[1:]):
        #print('column:', col)
        this = {}
        for platform in col:
            j = jump(platform, last, i != len(ps)-1)
            if j:
                this[platform] = j
                #print(platform, j)
        last = this
    return min(this.values(), key=lambda a: a[0])[0]

# UNIFORM COST SEARCH IS TOO SLOW!
"""
def get_insert_index(x, L, i=0):
    '''Given a number x and a non-empty sorted list of numbers L,
    Return the index at which x should be inserted
    using a recursive binary search process
    Parameter i stores the index of the first element of L in the original L'''
    
    #Base case
    if len(L) in {0,1}:
        if len(L) == 1:
            if x <= L[0]: #break ties by preferring new insert
                return i
            return i+1
        return i

    #Recursive case
    mid = len(L)//2        
    if x == L[mid]:
        return i+mid
    elif x < L[mid]:
        return get_insert_index(x, L[:mid], i)
    else:
        return get_insert_index(x, L[mid:], i+mid)


def get_children_and_costs(col, terminal, pace, ps):
    '''terminal is height of current platform
    return a list of tuples of (child, childcost)'''
    output = []
    for i, child in enumerate(ps[col+1]):
        if 0 < terminal-child < 6: #lower/faster
            output.append(( child, pace - 1*(pace>1) ))
        elif 0 < child-terminal < 6: #higher/slower
            output.append(( child, pace + 1*(pace<10) ))
        elif terminal == child:
            output.append(( child, pace ))
    return output    


def uniform_cost_search(start, ps):
    '''Perform a uniform cost search to fine the least-cost path    
    Return the least-cost path and minimum total cost    
    '''
    verb = False #for debugging print statements
    path_ids, next_id = {0:[start]}, 1
    agenda = [ (0, 5, 5) ] # path id, path cost, pace
    agenda_vals = [5]
    #expanded = set()
    
    while len(agenda) > 0:
        if verb: print('\nagenda', agenda)
        
        #Consider path with lowest cost               
        path, pathcost, pace = agenda.pop(0)
        agenda_vals.pop(0)
        if verb: print('chose id', path)
        path = path_ids[path]
        terminal = path[-1]
        if verb: print('terminal', path[-1], 'cost', pathcost, pace)
        
        #Win Condition
        if len(path) == len(ps):
            if verb: print('win condition')
            return path, pathcost, path_ids
                  
        for child, childcost in \
        get_children_and_costs(len(path)-1, terminal, pace, ps):
            path_ids[next_id] = path+[child]
            totalcost = pathcost + childcost
            index = get_insert_index(totalcost, agenda_vals)
            agenda.insert(index, (next_id, totalcost, childcost))
            agenda_vals.insert(index, totalcost)
            next_id += 1
            #try insertion optimization later if not efficient enough
    if verb: print('\npath_ids:', path_ids)
                
def solution(ps):
    '''ps is a list of tuples of ints; return shortest time'''
    path, pathcost, path_ids = uniform_cost_search(max(ps[0]), ps) #start on highest
    #print('\npath_ids:', path_ids)
    #print('result:', path, pathcost)
    return pathcost
"""
ex = [(14,16,18), (17,18,19), (17,20,21), (10,19,20), (4,7,14),
      (3,4,11), (4,5,8,15), (2,3,4,6), (8,10,12), (0,2,10,11,16,17)]

print('\nexpected: 29, result:', solution(ex))
print('\n')
print('small example:', solution([(5,), (4,6), (3,)]))