
facts = set([
    "holiday(Darjeeling)",
    "highly_visited(Munnar)",
    "highly_visited(Darjeeling)",
    "Darjeeling!=Munnar"
])

rules = [
    
    ("holiday(X)", "icecream(X)")
]

query = "icecream(Darjeeling)"

def match(pattern, fact):
    """Check if a rule pattern matches a fact; return substitution if yes."""
    if "(" not in pattern or "(" not in fact:
        return None
    pred_p, arg_p = pattern.split("(")
    pred_f, arg_f = fact.split("(")
    arg_p, arg_f = arg_p.strip(")"), arg_f.strip(")")
    
    if pred_p != pred_f:
        return None
    
    if arg_p.isupper():  
        return {arg_p: arg_f}
    elif arg_p == arg_f:
        return {}
    else:
        return None

def substitute(expr, subs):
    """Replace variables in expression according to substitution dictionary."""
    for var, val in subs.items():
        expr = expr.replace(var, val)
    return expr

def forward_chain(facts, rules):
    new_facts = set(facts)
    added = True
    steps = []
    
    while added:
        added = False
        for pattern, conclusion in rules:
            for fact in list(new_facts):
                subs = match(pattern, fact)
                if subs is not None:
                    new_fact = substitute(conclusion, subs)
                    if new_fact not in new_facts:
                        new_facts.add(new_fact)
                        steps.append(f"Derived '{new_fact}' from '{fact}' using rule ({pattern} → {conclusion})")
                        added = True
    return new_facts, steps

derived_facts, reasoning_steps = forward_chain(facts, rules)

print("STEP-BY-STEP REASONING:\n")
for s in reasoning_steps:
    print("•", s)

print("\nFINAL FACTS DERIVED:")
for f in sorted(derived_facts):
    print("-", f)

if query in derived_facts:
    print(f"\n QUERY PROVED: '{query}' is TRUE.")
else:
    print(f"\n QUERY COULD NOT BE PROVED.")
