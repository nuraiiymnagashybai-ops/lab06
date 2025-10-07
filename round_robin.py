processes = ['P1', 'P2', 'P3', 'P4']
arrival = [0, 1, 2, 3]
burst = [8, 4, 9, 5]
quantum = 3

n = len(processes)
remaining = burst[:]
time = 0
waiting = [0]*n
turnaround = [0]*n
queue = []

while True:
    done = True
    for i in range(n):
        if arrival[i] <= time and remaining[i] > 0:
            done = False
            if remaining[i] > quantum:
                time += quantum
                remaining[i] -= quantum
            else:
                time += remaining[i]
                waiting[i] = time - burst[i] - arrival[i]
                remaining[i] = 0
    if done:
        break

for i in range(n):
    turnaround[i] = burst[i] + waiting[i]

print("Процесс | Күту уақыты | Айналым уақыты")
for i in range(n):
    print(f"{processes[i]}       | {waiting[i]:>10} | {turnaround[i]:>14}")

print("\nОрташа күту уақыты =", sum(waiting)/n)
print("Орташа айналым уақыты =", sum(turnaround)/n)
