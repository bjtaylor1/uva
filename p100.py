import sys

cache = dict()

def cl(n):
    if not n in cache:
        res = cl_i(n)
        cache[n] = res
    else:
        res = cache[n]
        
    return res
    
    
def cl_i(n):
    if n == 1:
        return 1
    elif n % 2 == 1:
        return 1 + cl(3*n+1)
    else:
        return 1 + cl(n/2)

inputs = list()        
try:
    while(True):    
        vals = input().strip()
        inputs.append(vals)
except EOFError:
    for vals in inputs:
        if vals:    
            (i_s,j_s) = vals.split()
            try:
                i = int(i_s)
                j = int(j_s)
            except:
                break
                
            if i > j:
                (i,j) = (j,i)
            maxcl = 0
            for k in range(i, j+1):
                kcl = cl(k)
                if kcl > maxcl:
                    maxcl = kcl
            print(str(i_s) + " " + str(j_s) + " " + str(maxcl))
