import random
from fractions import Fraction

alphabet = ["f", "g", "h"]
rules = {
    "fh": "",
    "hh": "f",
    "hf": "",
    "ff": "h",
    "g": ""
}

def generate_word(min_len, max_len):
    length = random.randint(min_len, max_len)
    return "".join(random.choice(alphabet) for _ in range(length))

def apply_rules_fixed_steps(word, rules, steps):
    for _ in range(steps):
        applicable = [(lhs, rhs) for lhs, rhs in rules.items() if lhs in word]
        if not applicable:
            break 
        lhs, rhs = random.choice(applicable)
        start_idx = random.choice([i for i in range(len(word)) if word.startswith(lhs, i)])
        word = word[:start_idx] + rhs + word[start_idx + len(lhs):]
    return word

def diff_mod3(word):
    return (word.count("f") - word.count("h")) % 3

def invariant_M(w):
    S = ['f','g','h','ff','fg','fh','gf','gg','gh','hf','hg',
         'hh','fff','ffg','ffh','fgf','fgg','fgh','fhf','fhg','fhh',
         'gff','gfg','gfh','ggf','ggg','ggh','ghf','ghg','ghh',
         'hff','hfg','hfh','hgf','hgg','hgh','hhf','hhg','hhh']
    alpha = [
        Fraction(1,13), Fraction(1,13), Fraction(1,26),
        Fraction(-1,13), Fraction(-1,13), Fraction(-1,26),
        Fraction(-1,13), Fraction(-1,13), Fraction(-1,26),
        Fraction(-1,26), Fraction(-1,26), Fraction(0,1),
        Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1),
        Fraction(-1,26), Fraction(-1,26), Fraction(-1,26),
        Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1),
        Fraction(-1,26), Fraction(-1,26), Fraction(-1,26),
        Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1), Fraction(0,1),
        Fraction(-1,26), Fraction(-1,26), Fraction(-1,26),
    ]
    def count_substring(s, w):
        count = 0
        L = len(s)
        for i in range(len(w) - L + 1):
            if w[i:i+L] == s:
                count += 1
        return count
    M = Fraction(0,1)
    for s,a in zip(S, alpha):
        M += a * count_substring(s, w)
    if w == "h" or w == "":
        M = Fraction(1, 13)
    return M

start = generate_word(15, 30)
start_val1 = diff_mod3(start)
start_val2 = invariant_M(start)
    
end = apply_rules_fixed_steps(start, rules, steps=15)
end_val1 = diff_mod3(end)
end_val2 = invariant_M(end)
a1 = start_val1 == end_val1
a2 = start_val2 == end_val2
if not (a1 and a2):
    print(start_val1 == end_val1)
    print(start_val2 <= end_val2, start_val2, end_val2)
    print(start, end)

