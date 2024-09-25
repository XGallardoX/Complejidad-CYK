import matplotlib.pyplot as plt
import numpy as np
# Non-terminal symbols
non_terminals = ["NP", "Nom", "Det", "AP", "Adv", "A"]
terminals = ["book", "orange", "man", "tall", "heavy", "very", "muscular"]

# Grammar rules
R = {
    "NP": [["Det", "Nom"]],
    "Nom": [["AP", "Nom"], ["book"], ["orange"], ["man"]],
    "AP": [["Adv", "A"], ["heavy"], ["orange"], ["tall"]],
    "Det": [["a"]],
    "Adv": [["very"], ["extremely"]],
    "A": [["heavy"], ["orange"], ["tall"], ["muscular"]]
}

# CYK Algorithm with separate operation counts
def cykParse(w):
    n = len(w)
    
    # Operation counters
    init_ops = 0
    terminal_ops = 0
    table_ops = 0
    
    # 1. Initialize the table
    T = [[set() for _ in range(n)] for _ in range(n)]
    init_ops = n**2  # O(n^2) for initializing the table
    
    # 2. Filling in the diagonal with terminal matches
    for j in range(n):
        for lhs, rule in R.items():
            for rhs in rule:
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)
                    terminal_ops += 1  # Counting an operation

    # 3. Filling in the rest of the table
    for length in range(2, n + 1):  # length of the span
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)
                            table_ops += 1  # Increment operation count for each successful addition
    
    return init_ops, terminal_ops, table_ops

# Testing the function for different sizes of input strings
def run_cyk_for_lengths(max_len):
    init_ops_list = []
    terminal_ops_list = []
    total_ops_list = []
    
    for n in range(1, max_len + 1):
        # Create an input string of length n (using the word 'book' n times for simplicity)
        w = ["book"] * n
        init_ops, terminal_ops, table_ops = cykParse(w)
        total_ops = init_ops * terminal_ops 
        
        # Append the operation counts
        init_ops_list.append(init_ops)
        terminal_ops_list.append(terminal_ops)
        #table_ops_list.append(table_ops)
        total_ops_list.append(total_ops)
    
    return init_ops_list, terminal_ops_list, total_ops_list

# Run the analysis for input strings of length 1 to 10
init_ops_list, terminal_ops_list, total_ops_list = run_cyk_for_lengths(10)


#######################################################################################################################
# Graficar los resultados

# 1. Inicialización de la tabla
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), init_ops_list, label="Initializations (O(n^2))", marker='o')
plt.xlabel("Length of Input String (n)")
plt.ylabel("Number of Operations")
plt.title("CYK Algorithm - Table Initialization Complexity")
plt.grid(True)
plt.legend()
plt.show()

# 2. Llenado de la diagonal con terminales
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), terminal_ops_list, label="Terminal Matches (O(n))", color='orange', marker='o')
plt.xlabel("Length of Input String (n)")
plt.ylabel("Number of Operations")
plt.title("CYK Algorithm - Terminal Matching Complexity")
plt.grid(True)
plt.legend()
plt.show()

# 3. Comparativa total de operaciones
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), total_ops_list, label="Total Operations", color='red', marker='o')
plt.xlabel("Length of Input String (n)")
plt.ylabel("Number of Operations")
plt.title("CYK Algorithm - Total Operations")
plt.grid(True)
plt.legend()
plt.show()


# Function to create a cubic function for comparison
def cubic_function(n):
    return n**3

# Run the analysis for input strings of length 1 to 10
init_ops_list, terminal_ops_list, total_ops_list = run_cyk_for_lengths(10)

# Prepare data for the cubic function
n_values = range(1, 11)
cubic_ops_list = [cubic_function(n) for n in n_values]

# Graficar total de operaciones y O(n^3)
plt.figure(figsize=(10, 6))
plt.plot(n_values, total_ops_list, label="Total Operations", color='red', marker='o')
plt.plot(n_values, cubic_ops_list, label="O(n^3)", color='blue', linestyle='--')
plt.xlabel("Length of Input String (n)")
plt.ylabel("Number of Operations")
plt.title("CYK Algorithm - Total Operations vs O(n^3)")
plt.grid(True)
plt.legend()
plt.show()
