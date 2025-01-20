import os

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(1)


# Part 1

def lrsort(lines):
    left = []
    right = []
    for line in lines:
        x = line.split()
        left.append(int(x[0]))
        right.append(int(x[1]))
    left.sort()
    right.sort()
    return left, right


def solve1a(inp):
    lines = inp.splitlines()
    l,r = lrsort(lines)
    
    diff = []
    for o in range(len(l)):
        abs_diff = abs(l[o] - r[o])
        diff.append(abs_diff)
    
    final_sum = sum(diff)
    return final_sum

print(solve1a(inp)) # => 1889772

# Part 2

def solve2a(inp):
    lines = inp.splitlines()
    l,r = lrsort(lines)
    
    sim = []
    for s in l:
        nb_in_r = 0
        for i in r:
            if s == i:
                nb_in_r += 1 
        sim.append(s * nb_in_r)
    
    final_sum = sum(sim)
    return final_sum

print(solve2a(inp)) # => 23228917