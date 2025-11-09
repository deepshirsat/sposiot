MOT = {
    "STOP": "(IS,00)", "ADD": "(IS,01)", "SUB": "(IS,02)", "MULT": "(IS,03)",
    "MOVER": "(IS,04)", "MOVEM": "(IS,05)", "COMP": "(IS,06)", "BC": "(IS,07)",
    "DIV": "(IS,08)", "READ": "(IS,09)", "PRINT": "(IS,10)",
    "START": "(AD,01)", "END": "(AD,02)", "EQU": "(AD,04)",
    "DS": "(DL,01)", "DC": "(DL,02)",
    "AREG": "(RG,01)", "BREG": "(RG,02)", "CREG": "(RG,03)", "DREG": "(RG,04)"
}

program = [
    "START 100",
    "READ X",
    "ADD AREG, ='5'",
    "X DC 2",
    "Y DS 1",
    "Z EQU X",
    "END"
]

LC, symtab, intermediate_code, littab = 0, {}, [], []

for line in program:
    parts = line.replace(',', ' ').split()
    
    if parts[0] == "START":
        LC = int(parts[1])
        intermediate_code.append(f"{MOT['START']} (C,{LC})")
    
    elif parts[0] in ["READ", "PRINT"]:
        symtab[parts[1]] = symtab.get(parts[1], None) or None
        intermediate_code.append(f"{MOT[parts[0]]} (S,{parts[1]})")
        LC += 1
    
    elif len(parts) > 1 and parts[1] == "DC":
        symtab[parts[0]] = LC
        intermediate_code.append(f"{MOT['DC']} (C,{parts[2]})")
        LC += 1
    
    elif len(parts) > 1 and parts[1] == "DS":
        symtab[parts[0]] = LC
        intermediate_code.append(f"{MOT['DS']} (C,{parts[2]})")
        LC += int(parts[2])
    
    elif len(parts) > 1 and parts[1] == "EQU":
        symtab[parts[0]] = symtab[parts[2]]
        intermediate_code.append(f"{MOT['EQU']} (S,{parts[2]})")
    
    elif parts[0] in ["ADD", "SUB", "MULT", "DIV", "MOVER", "MOVEM", "COMP"]:
        operand = parts[2]
        if operand.startswith("='"):
            lit_val = operand[2:-1]
            littab.append(lit_val)
            operand = f"(L,{len(littab)})"
        intermediate_code.append(f"{MOT[parts[0]]} {MOT[parts[1]]} {operand}")
        LC += 1
    
    elif parts[0] == "END":
        intermediate_code.append(MOT["END"])

print("SYMBOL TABLE:")
for name, addr in symtab.items():
    print(f"{name} -> {addr}")

print("\nINTERMEDIATE CODE:")
for ic in intermediate_code:
    print(ic)
