# FCFS (First Come First Serve) CPU Scheduling

# Input number of processes
n = int(input("Enter the number of processes: "))

bt = []  # Burst Time
wt = [0] * n  # Waiting Time
tat = [0] * n  # Turnaround Time

# Input burst times
for i in range(n):
    b = int(input(f"Enter Burst Time for Process P{i+1}: "))
    bt.append(b)

# Calculate Waiting Time
for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

# Calculate Turnaround Time
for i in range(n):
    tat[i] = bt[i] + wt[i]

# Calculate averages
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n

# Display results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{i+1}\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
