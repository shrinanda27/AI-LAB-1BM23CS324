import itertools
print("Shrinanda Shivprasad Dinde")
print("1BM23CS324")
def truth_table_example():
    
    symbols = ["A", "B", "C"]
    
    entails = True
    
    header = ["A", "B", "C", "A∨C", "B∨¬C", "KB", "α"]
    print(" | ".join(f"{h:6}" for h in header))
    print("-" * (9 * len(header)))

    for values in itertools.product([False, True], repeat=3):
        A, B, C = values
      
        A_or_C = A or C
        B_or_notC = B or (not C)
        KB = A_or_C and B_or_notC
        alpha = A or B
      
        row = [A, B, C, A_or_C, B_or_notC, KB, alpha]
        print(" | ".join(f"{str(r):6}" for r in row))
        
        if KB and not alpha:
            entails = False
    
    print("\nFinal Result:")
    if entails:
        print("KB entails α ✅ (KB ⊨ α)")
    else:
        print("KB does NOT entail α ❌ (KB ⊭ α)")

truth_table_example()
