import os

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(1)


# Part 1

def sol(inp):
    lines = inp.splitlines()
    numbers = [int(line) for line in lines]
    total = 0
    for num in range(1, len(numbers)):
        if numbers[num] > numbers[num-1]:
            total += 1
    return total

print(sol(inp)) # => 1766


# Part 2

def sol2(inp):
    lines = inp.splitlines()
    numbers = [int(line) for line in lines]
    sum_windows = []
    for i in range(len(numbers) -2):
        window = numbers[i:i+3]
        sum_window = sum(window)
        sum_windows.append(sum_window)
    total = 0
    for num in range(1, len(sum_windows)):
        if sum_windows[num] > sum_windows[num-1]:
            total += 1
    return total

print(sol2(inp)) # => 1797