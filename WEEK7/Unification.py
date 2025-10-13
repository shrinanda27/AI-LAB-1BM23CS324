print("Shrinanda Shivprasad Dinde")
print("USN: 1BM23CS324")

def occurs_check(var, term, subst):
 
    if var == term:
        return True
    elif isinstance(term, tuple):
        for t in term:
            if occurs_check(var, t, subst):
                return True
    elif term in subst:
        return occurs_check(var, subst[term], subst)
    return False

def apply_substitution(term, subst):
    if isinstance(term, str):
        return subst.get(term, term)
    elif isinstance(term, tuple):
        return tuple(apply_substitution(t, subst) for t in term)
    else:
        return term

def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    x = apply_substitution(x, subst)
    y = apply_substitution(y, subst)

    if x == y:
        return subst
    elif isinstance(x, str) and x.islower():  # variable
        if occurs_check(x, y, subst):
            return None  # failure
        subst[x] = y
        return subst
    elif isinstance(y, str) and y.islower():  # variable
        if occurs_check(y, x, subst):
            return None
        subst[y] = x
        return subst
    elif isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):
            return None
        for x_i, y_i in zip(x, y):
            subst = unify(x_i, y_i, subst)
            if subst is None:
                return None
        return subst
    else:
        return None

def is_unifiable(x, y):
    result = unify(x, y)
    return result is not None


# Example: knows(John, x) and knows(y, Bill)
term1 = ('knows', 'John', 'x')
term2 = ('knows', 'y', 'Bill')

result = unify(term1, term2)

if result is None:
    print("No unifier exists.")
else:
    print("MGU:", result)

print("Are terms unifiable?", is_unifiable(term1, term2))
