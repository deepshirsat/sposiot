# -------------------- PASS TWO --------------------

# Given Intermediate Code (output from Pass One)
intermediate_code = [
    "(AD,01) (C,100)",
    "(IS,09) (S,X)",
    "(IS,01) (RG,01) (L,1)",
    "(DL,02) (C,2)",
    "(DL,01) (C,1)",
    "(AD,04) (S,X)",
    "(AD,02)"
]

# Symbol Table and Literal Table from Pass One
symtab = {"X": 101, "Y": 102, "Z": 101}
littab = [("5", 103)]

# -------------------- PASS TWO PROCESS --------------------
machine_code = []

for ic in intermediate_code:
    # Remove brackets and split tokens
    tokens = ic.replace('(', '').replace(')', '').replace(',', ' ').split()
    
    # Handle Imperative Statements (IS)
    if "IS" in tokens:
        opcode = tokens[tokens.index("IS") + 1]
        reg = tokens[tokens.index("RG") + 1] if "RG" in tokens else "00"
        
        # Find address for symbols, literals, or constants
        if "S" in tokens:
            sym = tokens[tokens.index("S") + 1]
            addr = symtab.get(sym, 0)
        elif "L" in tokens:
            lit_index = int(tokens[tokens.index("L") + 1]) - 1
            addr = littab[lit_index][1]
        elif "C" in tokens:
            addr = tokens[tokens.index("C") + 1]
        else:
            addr = "000"
        
        machine_code.append(f"{opcode} {reg} {addr}")
    
    # Handle Declarative Statements (DL)
    elif "DL" in tokens:
        if "C" in tokens:
            val = tokens[tokens.index("C") + 1]
            machine_code.append(f"00 00 {val}")
    
    # Handle Assembler Directives (AD)
    elif "AD" in tokens:
        # AD instructions (like START, END, EQU) do not generate machine code
        machine_code.append("// Assembler Directive")
    
    else:
        machine_code.append("// No operation")

# -------------------- OUTPUT --------------------
print("MACHINE CODE (Pass Two Output):")
for mc in machine_code:
    print(mc)
