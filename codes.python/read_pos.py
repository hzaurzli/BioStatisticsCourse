files = open('/home/lirz/biostatistic/ABI5-pos.fasta', "r", encoding=None)

with open('/home/lirz/biostatistic/pos','w') as f:
    for eachline in files:
        if eachline.startswith(">"):
            f.write(eachline)
