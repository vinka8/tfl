import random
T = [
    ("fgh", "fff"),
    ("fgh", "ggg"),
    ("fgh", "hhh"),
    ("hh", "hfhgh"),
    ("gggg", "")
]
T1 = [
    ("fh", ""),
    ("hh", "f"),
    ("hf", ""),
    ("ff", "h"),
    ("g", "")
]
alphabet = ["f", "g", "h"]

def random_word():
    return "".join(random.choice(alphabet) for _ in range(17))

def apply_random_rules(word):
    for _ in range(8):
        applicable = []
        for lhs, rhs in T:
            positions = []  
            for i in range(len(word) - len(lhs) + 1):  
                substring = word[i:i+len(lhs)] 
                if substring == lhs:  
                    positions.append(i) 
            if positions:
                applicable.append((lhs, rhs, positions))
        if not applicable:
            continue
        lhs, rhs, positions = random.choice(applicable)
        pos = random.choice(positions)
        word = word[:pos] + rhs + word[pos+len(lhs):]
    return word

def apply_rules(word, rules):
    results = set()
    for lhs, rhs in rules:
        for i in range(len(word) - len(lhs) + 1):
            if word[i:i+len(lhs)] == lhs:
                new_word = word[:i] + rhs + word[i+len(lhs):]
                results.add(new_word)
    return results

def words(start, rules):
    seen = set([start])
    s = [start]
    while s:
        new_s = []
        for w in s:
            new_words = apply_rules(w, rules)
            for nw in new_words:
                if nw not in seen:
                    seen.add(nw)
                    new_s.append(nw)
        s = new_s
    return seen


w0 = random_word()
print("w =", w0)
w1 = apply_random_rules(w0)
print("w' = ", w1)

words1 = words(w0, T1)
words2 = words(w1, T1)

intersect = words1 & words2
if intersect:
    print("True")
else:
    print("False")

