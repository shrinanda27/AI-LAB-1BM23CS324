print("Shrinanda Shivprasad Dinde")
print("USN: 1BM23CS324")
class Fact:
    def __init__(self, predicate, *args):
        self.predicate = predicate
        self.args = args
    
    def __repr__(self):
        return f"{self.predicate}({', '.join(self.args)})"
    
    def __eq__(self, other):
        return isinstance(other, Fact) and self.predicate == other.predicate and self.args == other.args
    
    def __hash__(self):
        return hash((self.predicate, self.args))

class Rule:
    def __init__(self, premises, conclusion):
        # premises: list of Fact objects
        # conclusion: Fact object
        self.premises = premises
        self.conclusion = conclusion
    
    def __repr__(self):
        premises_str = " ∧ ".join(map(str, self.premises))
        return f"{premises_str} ⇒ {self.conclusion}"

# Initialize facts (atomic sentences)
facts = {
    Fact("American", "Robert"),
    Fact("Enemy", "A", "America"),
    Fact("Missile", "T1"),
    Fact("Owns", "A", "T1"),
}

# Rules (implications)
rules = [
    Rule([Fact("Missile", "x")], Fact("Weapon", "x")),  # Missile(x) ⇒ Weapon(x)
    Rule([Fact("Enemy", "x", "America")], Fact("Hostile", "x")),  # Enemy(x, America) ⇒ Hostile(x)
    Rule([Fact("Missile", "x"), Fact("Owns", "A", "x")], Fact("Sells", "Robert", "x", "A")),  # ∀x Missile(x) ∧ Owns(A,x) ⇒ Sells(Robert, x, A)
    Rule([Fact("American", "p"), Fact("Weapon", "q"), Fact("Sells", "p", "q", "r"), Fact("Hostile", "r")], Fact("Criminal", "p"))  # American(p) ∧ Weapon(q) ∧ Sells(p,q,r) ∧ Hostile(r) ⇒ Criminal(p)
]

def match(fact1, fact2):
    """Match two facts allowing variables (starting with lowercase) to be replaced."""
    if fact1.predicate != fact2.predicate or len(fact1.args) != len(fact2.args):
        return None
    substitution = {}
    for arg1, arg2 in zip(fact1.args, fact2.args):
        if arg1.islower():  
            if arg1 in substitution and substitution[arg1] != arg2:
                return None
            substitution[arg1] = arg2
        else:
            if arg1 != arg2:
                return None
    return substitution

def substitute(fact, substitution):
    """Substitute variables in fact according to substitution dict."""
    new_args = [substitution.get(arg, arg) for arg in fact.args]
    return Fact(fact.predicate, *new_args)

def forward_chaining(facts, rules):
    inferred = set(facts)
    new_inferred = True
    while new_inferred:
        new_inferred = False
        for rule in rules:
            
            substitutions_list = [{}]  
            for premise in rule.premises:
                new_substitutions = []
                for substitution in substitutions_list:
                   
                    substituted_premise = substitute(premise, substitution)
                    matched = False
                    for fact in inferred:
                        match_substitution = match(substituted_premise, fact)
                        if match_substitution is not None:
                           
                            combined_substitution = substitution.copy()
                            combined_substitution.update(match_substitution)
                            new_substitutions.append(combined_substitution)
                            matched = True
                   
                substitutions_list = new_substitutions
        
            for substitution in substitutions_list:
                conclusion_fact = substitute(rule.conclusion, substitution)
                if conclusion_fact not in inferred:
                    print(f"Inferred new fact: {conclusion_fact} using rule: {rule}")
                    inferred.add(conclusion_fact)
                    new_inferred = True
    return inferred

final_facts = forward_chaining(facts, rules)

criminal_fact = Fact("Criminal", "Robert")

print("\nFinal Facts in Knowledge Base:")
for fact in final_facts:
    print(fact)

print("\nIs Robert Criminal?")
print(criminal_fact in final_facts)
