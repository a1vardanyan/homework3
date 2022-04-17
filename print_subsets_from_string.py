from itertools import permutations 
a = 'abra' 
S = [a[j] for j in range(len(a))] 
comb = [1, 0, 0, 0, 0, 1, 1, 1] 
A = list(set(list(permutations(comb, 4)))) 

#create all subsets for a, call it all_here
all_here = [] 
for i in range(len(A)): 
    new = '' 
    for j in range(len(S)): 
        if A[i][j] == 1: 
            new = new + S[j] 
    all_here.append(new) 

#sorted all_here by length of elements to avoid intersected subset, call it all_here2
all_here2 = []
for i in all_here:
    all_here2.append(''.join(sorted(i)))
all_here2 = sorted(all_here2, key=len, reverse=True)

#removed repeating elements in subsets for next step, call it sets_here (same as all_here2, but as a set)
sets_here = []
for a in range(len(all_here2)): 
    a_as_list = [all_here2[a][j] for j in range(len(all_here2[a]))] 
    if len(a_as_list) == 0: 
        sets_here.append('') 
    else: 
        sets_here.append(list(set(a_as_list)))

#to remove intersections in the set I get indexes of equal subsets
should_be_deleted = [] 
for i in range(len(sets_here)): 
    if sets_here[i] in sets_here[i+1:]: 
        should_be_deleted.append(i) 

#indexes of unique subsets for the final set
unique_indexes = list(set(range(len(sets_here))).difference(should_be_deleted))

#print results sorted starting from the smallest subsets
for i in sorted(unique_indexes, reverse=True):
    print(all_here2[i])
