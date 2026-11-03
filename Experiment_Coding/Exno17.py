graph = {'Maths':['Programming','Networks'],
         'Programming':['Maths','Database'],
         'Networks':['Maths','Database'],
         'Database':['Programming','Networks']}
colors = {}
for node in graph:
    used = {colors[v] for v in graph[node] if v in colors}
    color = 0
    while color in used:
        color += 1
    colors[node] = color
print("Examination Timetable:")
for subject, color in colors.items():
    print(subject, "-> Slot", color+1)
print("Total Slots Used:", len(set(colors.values())))