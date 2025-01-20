import os
import re

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(3)


# Part 1

def calculate_mul_sum(samp):
    exp = []
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"  

    exp = re.findall(pattern, samp)

    res = []
    for o in exp:
        t = []
        for i in o:
            t.append(int(i))
        res.append(t)

    results = []
    for pair in res:
        results.append(pair[0] * pair[1])
    result = sum(results)
    return result

print(calculate_mul_sum(inp)) # => 173517243


# Part 2

def process_single_mul(test_string):    
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"  
    exp = re.findall(pattern, test_string)

    res = []
    for o in exp:
        t = []
        for i in o:
            t.append(int(i))
        res.append(t)

    results = None
    for pair in res:
        results = pair[0] * pair[1]
    return results

def solve3b(samp):
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"

    matches = []
    for match in re.finditer(pattern, samp):
        matches.append({"position": match.start(), "group": match.group()})

    for match in re.finditer(dont_pattern, samp):
        matches.append({"position": match.start(), "group": match.group()})

    for match in re.finditer(do_pattern, samp):
        matches.append({"position": match.start(), "group": match.group()})
    
    sorted_matches = sorted(matches, key=lambda x: x['position'])

    indicator = True
    total = 0
    for sm in sorted_matches:
        if sm['group'] == "don't()":
            indicator = False
        elif sm['group'] == "do()":
            indicator = True 
        elif indicator and 'mul' in sm['group']:
            total += process_single_mul(sm['group'])
    return total

print(solve3b(inp)) # => 100450138