from collections import Counter

data = open('/home/rzli/biostatistic/new.fa', "r", encoding=None)
list = []

for line in data:
    if line.startswith(">"):
        continue
    else:
        str = line.upper()
        for i in range(0,11):
            sub = str[i:i+6]
            list.append(sub)

print(Counter(list).most_common(6))
