import numpy as np 
def checker(x): 
    y = [x[j] for j in range(len(x))] 
    F = dict() 
    F['('] = ')' 
    F['{'] = '}' 
    F['['] = ']' 
    F['<'] = '>' 
    def fun(symb): 
        new = symb.copy() 
        temp = len(new) 
        if len(new) > 1: 
            for i in range(1, len(new)): 
                if new[i-1] in F.keys(): 
                    if F[new[i-1]] == new[i]: 
                        del new[i], new[i-1] 
                        break 
        if len(new) == temp: 
            return print('NO') 
        if len(new) > 0: 
            fun(new) 
        if len(new) == 0: 
            return print('YES') 
    return fun(y) 
checker('()[][0]')
