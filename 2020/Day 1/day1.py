import os

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(1)


# Part 1

def solve1a(inp):
    lines = inp.splitlines()

    numbers = []
    for line in lines:
        numbers.append(int(line))

    the_numbers = []
    for number in numbers:
        x = 0
        for num in numbers:
            x = number+num
            if x == 2020:
                the_numbers.append(number)
                the_numbers.append(num)
                break

    result = the_numbers[0]*the_numbers[1]
    return result

print(solve1a(inp)) # => 776064


# Part 2

def solve1b(inp):
    lines = inp.splitlines()

    numbers = []
    for line in lines:
        numbers.append(int(line))

    the_numbers = []
    for n in numbers:
        for number in numbers:
            x = 0
            for num in numbers:
                x = n+number+num
                if x == 2020:
                    the_numbers.append(number)
                    the_numbers.append(num)
                    the_numbers.append(n)
                    break

    result = the_numbers[0]*the_numbers[1]*the_numbers[2]
    return result

print(solve1b(inp)) # => 6964490