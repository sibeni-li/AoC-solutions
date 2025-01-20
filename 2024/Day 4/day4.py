import os

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(4)


# Part 1

def find_x_positions(grid):
    positions = []
    for row_id in range(len(grid)):
        for col_id in range(len(grid[0])):
            if grid[row_id][col_id] == "X":
                positions.append((row_id, col_id))
    return positions

def count_all(grid):
    x_positions = find_x_positions(grid)  
    count = 0
    for row, col in x_positions:
        # Horizontal
        if col + 3 < len(grid[0]):  # right
            if (grid[row][col+1] == 'M' and 
                grid[row][col+2] == 'A' and 
                grid[row][col+3] == 'S'):
                count +=1
        if col >= 3:  # left
            if (grid[row][col-1] == 'M' and 
                grid[row][col-2] == 'A' and 
                grid[row][col-3] == 'S'):
                count +=1
        # Vertical
        if row + 3 < len(grid):  # down
            if (grid[row+1][col] == 'M' and 
                grid[row+2][col] == 'A' and 
                grid[row+3][col] == 'S'):
                count +=1
        if row >= 3:  # up
            if (grid[row-1][col] == 'M' and 
                grid[row-2][col] == 'A' and 
                grid[row-3][col] == 'S'):
                count +=1
        # Diagonals
        if (row + 3 < len(grid) and
            col + 3 < len(grid[0])):  # down-right
            if (grid[row+1][col+1] == 'M' and 
                grid[row+2][col+2] == 'A' and 
                grid[row+3][col+3] == 'S'):
                count +=1
        if (row >= 3 and
            col >= 3):  # up-left
            if (grid[row-1][col-1] == 'M' and 
                grid[row-2][col-2] == 'A' and 
                grid[row-3][col-3] == 'S'):
                count +=1
        if (row + 3 < len(grid) and
            col >= 3):  # down-left
            if (grid[row+1][col-1] == 'M' and 
                grid[row+2][col-2] == 'A' and 
                grid[row+3][col-3] == 'S'):
                count +=1
        if (row >= 3 and
            col + 3 < len(grid[0])):  # up-right
            if (grid[row-1][col+1] == 'M' and 
                grid[row-2][col+2] == 'A' and 
                grid[row-3][col+3] == 'S'):
                count +=1
    return count

def solve4a(inp):
    lines = inp.splitlines()
    grid = [[xs for xs in line] for line in lines]
    return count_all(grid)

print(solve4a(inp)) # => 2557


# Part 2

def find_a_positions(grid):
    positions = []
    for row_id in range(len(grid)):
        for col_id in range(len(grid[0])):
            if grid[row_id][col_id] == "A":
                positions.append((row_id, col_id))
    return positions

def count_all_x_mas(grid):
    a_positions = find_a_positions(grid)
    count = 0
    for row_a, col_a in a_positions:
        if (row_a >= 1 and
            row_a + 1 < len(grid) and
            col_a >= 1 and
            col_a + 1 < len(grid[0])):
            if (((grid[row_a-1][col_a-1] == 'M' and
                grid[row_a+1][col_a+1] == 'S') or
                (grid[row_a-1][col_a-1] == 'S' and
                grid[row_a+1][col_a+1] == 'M')) and
                ((grid[row_a+1][col_a-1] == 'M' and
                grid[row_a-1][col_a+1] == 'S') or
                (grid[row_a+1][col_a-1] == 'S' and
                grid[row_a-1][col_a+1] == 'M'))):
                count +=1
    return count

def solve4b(inp):
    lines = inp.splitlines()
    grid = [[xs for xs in line] for line in lines]
    return count_all_x_mas(grid)

print(solve4b(inp)) # => 1854