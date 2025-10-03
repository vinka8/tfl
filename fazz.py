import random
from collections import deque

def generate_random_word(length, alphabet):
    return ''.join(random.choice(alphabet) for _ in range(length))

def rule_T(word, rules):
    applicable_rules = []
    for lhs, rhs in rules:
        positions = []
        idx = 0
        while idx <= len(word) - len(lhs):
            if word[idx:idx+len(lhs)] == lhs:
                positions.append(idx)
            idx += 1
        for pos in positions:
            applicable_rules.append((lhs, rhs, pos))
    if not applicable_rules:
        return word, False
    lhs, rhs, pos = random.choice(applicable_rules)
    new_word = word[:pos] + rhs + word[pos+len(lhs):]
    return new_word, True

def apply_rules(word, rules):
    results = set()
    for lhs, rhs in rules:
        idx = 0
        while idx <= len(word) - len(lhs):
            if word[idx:idx+len(lhs)] == lhs:
                new_word = word[:idx] + rhs + word[idx+len(lhs):]
                results.add(new_word)
            idx += 1
        idx = 0
        while idx <= len(word) - len(rhs):
            if word[idx:idx+len(rhs)] == rhs:
                new_word = word[:idx] + lhs + word[idx+len(rhs):]
                results.add(new_word)
            idx += 1
    return results
def reachable(start, target, rules, max_len, max_steps):
    if start == target:
        return True
    f_queue = deque([(start, 0)])
    b_queue = deque([(target, 0)])
    f_visited = {start}
    b_visited = {target}
    while f_queue and b_queue:
        if len(f_queue) <= len(b_queue):
            current_queue, current_visited, other_visited = f_queue, f_visited, b_visited
        else:
            current_queue, current_visited, other_visited = b_queue, b_visited, f_visited
        word, steps = current_queue.popleft()
        if steps >= max_steps:
            continue
        for new_word in apply_rules(word, rules):
            if len(new_word) > max_len:
                continue
            if new_word in other_visited:
                return True
            if new_word not in current_visited:
                current_visited.add(new_word)
                current_queue.append((new_word, steps + 1))
    return False

alphabet = ['f', 'g', 'h']
T = [
    ("fgh", "fff"),
    ("fgh", "ggg"),
    ("fgh", "hhh"),
    ("hh", "hfhgh"),
    ("gggg", "")
]

T1 = [
    ("fgh", "fff"),
    ("ggg", "fgh"),
    ("fff", "hhh"),
    ("ghhh", "hhhg"),
    ("fh", "hf"),
    ("hh", "f"),
    ("fgf", "ff"),
    ("ghf", "hfg"),
    ("hf", ""),
    ("ff", "h"),
    ("g", "")
]
word = generate_random_word(30, alphabet)
sequence = [word]
steps = random.randint(15, 20)
for _ in range(steps):
    word, applied = rule_T(word, T)
    if not applied:
        break
    sequence.append(word)
f = True
for i in range(len(sequence) - 1):
    w_from = sequence[i]
    w_to = sequence[i + 1]
    if not reachable(w_from, w_to, T1, max_len=100, max_steps=15):
        f = False
        print(f"Невозможно переписать '{w_from}' в '{w_to}' в T'")
        break
if f:
    print("Слово достижимо в T'")
