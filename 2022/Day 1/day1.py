# from aocd import get_data
# inp = get_data(day=1, year=2022)

import os

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(1)


# Part 1

def totcal(xs):
    total = 0
    for i in xs:
        total += i 
    return total

def answer(inp):
    lines = inp.splitlines()
    
    result = []
    l = []
    for o in lines:
        if o != "": 
            l.append(int(o))
        else: 
            result.append(l)
            l = []
    result.append(l) #Last elf added

    cals = []
    for e in result:
        cals.append(totcal(e))
    return max(cals)

print(answer(inp)) #=> 458397

# Part 2

def answer2(inp):
    lines = inp.splitlines()
    
    result = []
    l = []
    for o in lines:
        if o != "": 
            l.append(int(o))
        else: 
            result.append(l)
            l = []
    result.append(l) #Last elf added

    cals = []
    for e in result:
        cals.append(totcal(e))
    cals.sort()
    return totcal(cals[-3:])

print(answer2(inp))