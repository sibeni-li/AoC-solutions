import os

def get_data(day):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'day{day}.txt')
    with open(file_path, 'r') as file:
        return file.read()
    
inp = get_data(5)

# Part 1

def find_applicable_rules(rules, sequences):
    all_applicable_rules = [] 
    for sequence in sequences:
        applicable_rules = []
        for rule in rules:
            both_present = rule[0] in sequence and rule[1] in sequence
            if both_present:
                applicable_rules.append(rule)
        all_applicable_rules.append(applicable_rules)
        applicable_rules = []
    return all_applicable_rules 

def find_valid_sequences(rules, sequences):
    valid_sequences = []
    for i, sequence in enumerate(sequences):
        applicable_rules = find_applicable_rules(rules, sequences)[i]
        rules_followed = []
        for rule in applicable_rules:
            pos_a = sequence.index(rule[0])
            pos_b = sequence.index(rule[1])
            rules_followed.append(pos_a < pos_b)
        if all(rules_followed):
            valid_sequences.append(sequence)
    return valid_sequences

def sum_mid_num(rules, sequences):
    valid_seqs = find_valid_sequences(rules, sequences)
    middle_numbers = []
    for seq in valid_seqs:
        middle_index = len(seq) // 2
        middle_number = seq[middle_index]
        middle_numbers.append(middle_number)
    return sum(middle_numbers)

def solve5a(inp):
    lines = inp.split('\n\n')
    r,s = [line.splitlines() for line in lines]
    rules = [[int(i) for i in o.split('|')] for o in r]
    sequences = [[int(i) for i in o.split(',')] for o in s]
    return sum_mid_num(rules, sequences)

print(solve5a(inp)) # => 4766


# Part 2

def find_invalid_sequences(rules, sequences):
    invalid_sequences = []
    for i, sequence in enumerate(sequences):
        applicable_rules = find_applicable_rules(rules, sequences)[i]
        rules_unfollowed = []
        for rule in applicable_rules:
            pos_a = sequence.index(rule[0])
            pos_b = sequence.index(rule[1])
            rules_unfollowed.append(pos_a < pos_b)
        if not all(rules_unfollowed):
            invalid_sequences.append(sequence)
    return invalid_sequences

def make_valid_sequences(rules, sequences):
    invalid_sequences = find_invalid_sequences(rules, sequences)
    new_applicable_rules = find_applicable_rules(rules, invalid_sequences)
    sorted_sequences = []
    for i, sequence in enumerate(invalid_sequences):
        its_rules = new_applicable_rules[i]
        must_come_before = {num: 0 for num in sequence}
        for rule in its_rules:
            must_come_before[rule[1]] += 1
        sorted_pairs = sorted(must_come_before.items(), key=lambda x: x[1])
        sorted_sequence = [pair[0] for pair in sorted_pairs]
        sorted_sequences.append(sorted_sequence)
    return sorted_sequences

def solve5b(inp):
    lines = inp.split('\n\n')
    r,s = [line.splitlines() for line in lines]
    rules = [[int(i) for i in o.split('|')] for o in r]
    sequences = [[int(i) for i in o.split(',')] for o in s]
    return sum_mid_num(rules, make_valid_sequences(rules, sequences))

print(solve5b(inp)) # => 6257