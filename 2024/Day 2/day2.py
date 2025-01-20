import os

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(2)


# Part 1 

def increasing(xs):
    incr = []
    for lst in xs:
        inc_int = []
        for n in range(len(lst)-1):
            act = lst[n]
            nextt = lst[n+1]
            if act < nextt and abs(act - nextt) <= 3:
                inc_int.append(True)
            else:
                inc_int.append(False)
        if all(inc_int) is True:
            incr.append(lst)
    return incr

def decreasing(xs):
    decr = []
    for lst in xs:
        dec_int = []
        for n in range(len(lst)-1):
            act = lst[n]
            nextt = lst[n+1]
            if act > nextt and abs(act - nextt) <= 3:
                dec_int.append(True)
            else:
                dec_int.append(False)
        if all(dec_int) is True:
            decr.append(lst)
    return decr

def solve2a(samp):
    lines = samp.splitlines()
    line = [line.split() for line in lines]
    xs = []
    for o in line:
        x = []
        for i in o:
            x.append(int(i))
        xs.append(x)
        x = []
    total = len(increasing(xs))+len(decreasing(xs))
    return total

print(solve2a(inp)) # => 314

# Part 2

def increasing2(xs):
    incr = []
    inc_fs = []
    for lst in xs:
        inc_int = []
        for n in range(len(lst)-1):
            act = lst[n]
            nextt = lst[n+1]
            if act < nextt and abs(act - nextt) <= 3:
                inc_int.append(True)
            else:
                inc_int.append(False)
        if all(inc_int) is True:
            incr.append(lst)
        else:
            inc_fs.append(lst)
    return incr, inc_fs


def decreasing2(xs):
    decr = []
    dec_fs = []
    for lst in xs:
        dec_int = []
        for n in range(len(lst)-1):
            act = lst[n]
            nextt = lst[n+1]
            if act > nextt and abs(act - nextt) <= 3:
                dec_int.append(True)
            else:
                dec_int.append(False)
        if all(dec_int) is True:
            decr.append(lst)
        else:
            dec_fs.append(lst)
    return decr, dec_fs


def subs(lst):
    lsts = []
    for j in range(len(lst)):
        lsts.append(lst[:j] + lst[j+1:])
    return lsts


def solve2b(samp):
    lines = samp.splitlines()
    line = [line.split() for line in lines]
    xs = []
    for o in line:
        x = []
        for i in o:
            x.append(int(i))
        xs.append(x)
        x = []

    inc, incfs = increasing2(xs)
    dec, decfs = decreasing2(xs)
    tot1 = len(inc) + len(dec)

    tot2 = 0
    for i in incfs:
        xss = subs(i)
        inc2, _ = increasing2(xss)
        if len(inc2) >= 1:
            tot2 += 1

    tot3 = 0
    for i in decfs:
        xss = subs(i)
        dec2, _ = decreasing2(xss)
        if len(dec2) >= 1:
            tot3 += 1

    total = tot1 + tot2 + tot3
    return total

print(solve2b(inp)) # => 373
