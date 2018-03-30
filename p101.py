import sys
count = int(input())
stacks = [[i] for i in range(0,count)]
linenum = 0

def getstackindex(n):
    for stackindex in range(0,count):
        if n in stacks[stackindex]:
            return stackindex

def clear(n, stackindex):
    pos = stacks[stackindex].index(n)
    to_clear = stacks[stackindex][pos:]
    stacks[stackindex] = stacks[stackindex][:n]
        
    for c in to_clear:
        stacks[c] += [c]

try:
    while(True):
        line = input()
        if(line == "quit"):
            break
            
        linenum += 1
        print(str(linenum) + ": " + line)
        if(linenum == 37):
            for n in range(0,count):
                print(str(n) + ": " + " ".join(str(b) for b in stacks[n]))
            print()
                
        parts = line.split()
        op = parts[0]
        source = int(parts[1])
        verb = parts[2]
        target = int(parts[3])
        sourcestack = getstackindex(source)
        targetstack = getstackindex(target)
        if(source == target or sourcestack == targetstack):
            continue
        
        if(op == "move"):
            clear(source, sourcestack)

        if(linenum == 37):
            for n in range(0,count):
                print(str(n) + ": " + " ".join(str(b) for b in stacks[n]))
            print("source = " + str(source) + ", sourcestack = " + str(sourcestack))
            print()
            
          
        if(verb == "onto"):
            clear(target, targetstack)
            
        sourceindex = stacks[sourcestack].index(source)
        to_move = stacks[sourcestack][sourceindex:]
        stacks[sourcestack] = stacks[sourcestack][:sourceindex]
        stacks[targetstack] += to_move
        print (line + " done")
        print()
        
except EOFError:
    x = 1
        
for n in range(0,count):
    print(str(n) + ": " + " ".join(str(b) for b in stacks[n]))