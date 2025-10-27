import math
print("Shrinanda Shivprasad Dinde")
print("1BM23CS324")

class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children or []
        self.value = value

def alpha_beta(node, alpha, beta, maximizing, trace):
    if not node.children:
        trace.append(f"Reached leaf {node.name} → value = {node.value}")
        return node.value

    if maximizing:
        max_eval = -math.inf
        trace.append(f"MAX node {node.name} starts with α={alpha}, β={beta}")
        for child in node.children:
            eval_val = alpha_beta(child, alpha, beta, False, trace)
            max_eval = max(max_eval, eval_val)
            alpha = max(alpha, eval_val)
            trace.append(f"MAX node {node.name} updated α={alpha}, β={beta}")

            if beta <= alpha:
                trace.append(f"⚠️ PRUNED remaining children of {node.name} (α={alpha}, β={beta})")
                break
        return max_eval
    else:
        min_eval = math.inf
        trace.append(f"MIN node {node.name} starts with α={alpha}, β={beta}")
        for child in node.children:
            eval_val = alpha_beta(child, alpha, beta, True, trace)
            min_eval = min(min_eval, eval_val)
            beta = min(beta, eval_val)
            trace.append(f"MIN node {node.name} updated α={alpha}, β={beta}")

            if beta <= alpha:
                trace.append(f"⚠️ PRUNED remaining children of {node.name} (α={alpha}, β={beta})")
                break
        return min_eval

def build_tree():
    num_levels = int(input("Enter the number of levels in the tree (including leaf level): "))

    if num_levels < 2:
        print("Tree must have at least 2 levels (root and leaves).")
        return None

    level_types = []
    for i in range(num_levels - 1):
        t = input(f"Is level {i+1} a MAX or MIN level? (Enter MAX/MIN): ").strip().upper()
        level_types.append(t)

    num_leaves = int(input("Enter number of leaf nodes: "))
    leaf_values = []
    for i in range(num_leaves):
        v = int(input(f"Enter value for leaf node L{i+1}: "))
        leaf_values.append(Node(f"L{i+1}", value=v))

    current_level = leaf_values
    for depth in range(num_levels - 2, -1, -1):
        new_level = []
        level_type = level_types[depth]
        node_prefix = f"{level_type[0]}{depth+1}"
        for i in range(0, len(current_level), 2):
            children = current_level[i:i + 2]
            node_name = f"{node_prefix}_{i//2 + 1}"
            new_level.append(Node(node_name, children))
        current_level = new_level

    root = current_level[0]
    print("\n✅ Tree built successfully!\n")
    return root


if __name__ == "__main__":
    root = build_tree()
    if root:
        trace_output = []
        print("\nStarting Alpha-Beta Pruning...\n")
        best_value = alpha_beta(root, -math.inf, math.inf, True, trace_output)

        print("\n===== TRACE OUTPUT =====")
        for step in trace_output:
            print(step)

        print("\n===== FINAL RESULT =====")
        print(f"Best value at root: {best_value}")
