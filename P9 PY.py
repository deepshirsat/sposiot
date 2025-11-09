# Memory Placement Strategies: First Fit and Best Fit

def first_fit(blocks, process_sizes):
    allocation = [-1] * len(process_sizes)
    block_sizes = blocks.copy()

    for i in range(len(process_sizes)):
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                allocation[i] = j
                block_sizes[j] -= process_sizes[i]
                break

    print("\n--- First Fit Allocation ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_sizes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{process_sizes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{process_sizes[i]}\t\tNot Allocated")


def best_fit(blocks, process_sizes):
    allocation = [-1] * len(process_sizes)
    block_sizes = blocks.copy()

    for i in range(len(process_sizes)):
        best_index = -1
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if best_index == -1 or block_sizes[j] < block_sizes[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            block_sizes[best_index] -= process_sizes[i]

    print("\n--- Best Fit Allocation ---")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(process_sizes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{process_sizes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{process_sizes[i]}\t\tNot Allocated")


# -------------------- MAIN PROGRAM --------------------
n = int(input("Enter number of memory blocks: "))
blocks = []
for i in range(n):
    size = int(input(f"Enter size of Block {i+1}: "))
    blocks.append(size)

m = int(input("\nEnter number of processes: "))
process_sizes = []
for i in range(m):
    size = int(input(f"Enter size of Process {i+1}: "))
    process_sizes.append(size)

first_fit(blocks, process_sizes)
best_fit(blocks, process_sizes)
