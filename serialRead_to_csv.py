import pandas

letter = ['A', 'B', 'C', 'D', 'E', 'F']
status = ['Clean', 'Tomato']
current_letter = 5
current_status = 1


with open(f'{letter[current_letter]} {status[current_status]}.txt') as f:
    lines = f.readlines()

time = []
a0 = []
a1 = []
a2 = []

for i in range(len(lines)):
    lines[i] = lines[i].replace("b'", '').replace(
        '\\t', '').replace("\\r\\n'\t\n", '').split()

    time.append(lines[i][0])
    a0.append(lines[i][1][3:])
    a1.append(lines[i][2][3:])
    a2.append(lines[i][3][3:])

df = pandas.DataFrame({'Time': time, f'{letter[current_letter]}0': a0,
                       f'{letter[current_letter]}1': a1, f'{letter[current_letter]}2': a2})
df.to_csv(f'{letter[current_letter]} {status[current_status]}.csv', index=False)
