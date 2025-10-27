print("Shrinanda Shivprasad Dinde")
print("USN:1BM23CS324")

from copy import deepcopy

# ---------- Unification Utilities ----------
def is_variable(term):
    return term[0].islower()

def unify(x, y, subs=None):
    if subs is None:
        subs = {}
    if x == y:
        return subs
    if is_variable(x):
        return unify_var(x, y, subs)
    if is_variable(y):
        return unify_var(y, x, subs)
    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x) != len(y):
            return None
        for a, b in zip(x[1:], y[1:]):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs
    return None

def unify_var(var, x, subs):
    if var in subs:
        return unify(subs[var], x, subs)
    elif x in subs:
        return unify(var, subs[x], subs)
    elif occurs_check(var, x, subs):
        return None
    else:
        subs[var] = x
        return subs

def occurs_check(var, x, subs):
    if var == x:
        return True
    elif isinstance(x, tuple):
        return any(occurs_check(var, xi, subs) for xi in x[1:])
    elif x in subs:
        return occurs_check(var, subs[x], subs)
    return False

def substitute(clause, subs):
    new_clause = []
    for lit in clause:
        pred, *args = lit
        new_args = tuple(subs.get(arg, arg) for arg in args)
        new_clause.append((pred, *new_args))
    return new_clause

# ---------- Resolution ----------
proof_steps = []  # store proof history

def resolve(ci, cj):
    for li in ci:
        for lj in cj:
            if li[0] == '~' + lj[0] or lj[0] == '~' + li[0]:
                subs = unify(li[1:], lj[1:])
                if subs is not None:
                    new_ci = [l for l in ci if l != li]
                    new_cj = [l for l in cj if l != lj]
                    resolvent = substitute(list(set(new_ci + new_cj)), subs)
                    step = {
                        "parents": (ci, cj),
                        "sub": subs,
                        "result": resolvent
                    }
                    proof_steps.append(step)
                    print(f"Resolved {ci} and {cj} with {subs} -> {resolvent}")
                    return resolvent
    return None

def resolution(KB):
    new = set()
    while True:
        n = len(KB)
        for i in range(n):
            for j in range(i + 1, n):
                resolvent = resolve(KB[i], KB[j])
                if resolvent == []:
                    print(f"\n✅ Contradiction found between {KB[i]} and {KB[j]}")
                    print("✅ Contradiction found. Therefore, John likes peanuts is PROVED.")
                    proof_steps.append({
                        "parents": (KB[i], KB[j]),
                        "sub": {},
                        "result": []
                    })
                    return True
                if resolvent is not None:
                    new.add(tuple(sorted(resolvent)))
        new_clauses = [list(c) for c in new if list(c) not in KB]
        if not new_clauses:
            return False
        KB.extend(new_clauses)

def parse_clause(text):
    text = text.replace(" ", "")
    literals = text.split("|")
    clause = []
    for lit in literals:
        neg = lit.startswith("~")
        lit = lit[1:] if neg else lit
        pred, args = lit.split("(")
        args = args.strip(")").split(",")
        pred = "~" + pred if neg else pred
        clause.append((pred, *args))
    return clause

# ---------- Proof Tree Printing ----------
def print_proof_tree():
    print("\n\n--- RESOLUTION PROOF TREE ---")
    for i, step in enumerate(proof_steps):
        p1, p2 = step["parents"]
        subs = step["sub"]
        result = step["result"]
        print(f"\nStep {i+1}:")
        print(f"  From {p1} and {p2}")
        print(f"  Substitution: {subs}")
        print(f"  ⇒ {result}")
    if proof_steps and proof_steps[-1]["result"] == []:
        print("\n{ }  Hence proved.")

# ---------- MAIN EXECUTION ----------
print("\n========= FOL Resolution Prover =========")
n = int(input("Enter number of clauses in KB: "))
KB = []
for i in range(n):
    text = input(f"Enter clause {i+1} in CNF form (use | for OR, ~ for NOT): ")
    KB.append(parse_clause(text))

goal = input("Enter query to prove (e.g., Likes(John,Peanut)): ")
neg_goal = "~" + goal if not goal.startswith("~") else goal[1:]
KB.append(parse_clause(neg_goal)[0:1])  # add negated goal

print("\nKnowledge Base:")
for i, c in enumerate(KB, 1):
    print(f"{i}. {c}")

print("\n--- Resolution Process ---")
if resolution(KB):
    print_proof_tree()
else:
    print("\n❌ No contradiction found. Query cannot be proved.")
