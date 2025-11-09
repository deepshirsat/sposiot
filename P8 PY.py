# Priority CPU Scheduling (Non-Preemptive)

# Input number of processes
n = int(input("Enter the number of processes: "))

bt = []     # Burst Time
pr = []     # Priority
pid = []    # Process ID
wt = [0] * n
tat = [0] * n

# Input burst time and priority
for i in range(n):
    print(f"\nProcess P{i+1}")
    b = int(input("Enter Burst Time: "))
    p = int(input("Enter Priority (lower number = higher priority): "))
    bt.append(b)
    pr.append(p)
    pid.append(i + 1)

# Sort processes by priority (ascending order)
for i in range(n - 1):
    for j in range(i + 1, n):
        if pr[i] > pr[j]:
            # Swap priority
            pr[i], pr[j] = pr[j], pr[i]
            # Swap burst time
            bt[i], bt[j] = bt[j], bt[i]
            # Swap process ID
            pid[i], pid[j] = pid[j], pid[i]

# Waiting time for first process is 0
wt[0] = 0

# Calculate waiting time
for i in range(1, n):
    wt[i] = wt[i-1] + bt[i-1]

# Calculate turnaround time
for i in range(n):
    tat[i] = bt[i] + wt[i]

# Calculate averages
avg_wt = sum(wt) / n
avg_tat = sum(tat) / n

# Display result
print("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{pid[i]}\t{pr[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
