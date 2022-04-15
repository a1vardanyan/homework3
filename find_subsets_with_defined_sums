import numpy as np 
import time 
start_time = time.time() 
N = np.random.randint(1,10**3,1) #10*1-10**5 
M = np.random.randint(1,10**3,1) #10*0-10*9 
V = np.random.randint(1, 10**5, N) 
P = np.random.randint(1, 10**7, M)
c = []
j = -1
for i in P:
    j += 1
    start = 0 
    end = 0 
    listx = V 
    needed = i
    len_V = len(V)
    x = V[0]
    while True:
        if start == len_V: 
            print("Not found", j)
            break 
        if x == needed: 
            print([start, end+1]) 
            break  
        elif x < needed: 
            end += 1
            if end < len_V:
                x += V[end]
                #print(start, end, x, needed, 1) 
            else:
                print("Not found", j)
                break
        elif x > needed: 
            x -= V[start]
            start += 1
            #print(start, end, x, needed, 2)
            if start > end: 
                end += 1
                if end < len_V:
                    x += V[end]
                else:
                    print("Not found", j)
                    break
            #print(start, end, x, needed, 3) 

print(f"{(time.time() - start_time)} seconds or {(time.time() - start_time)/60} minutes")
