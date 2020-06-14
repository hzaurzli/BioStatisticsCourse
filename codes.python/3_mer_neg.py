import pandas as pd
from pandas import *
import argparse,re

files = open('/home/lirz/biostatistic/ABI5-neg.fasta', "r", encoding=None)
all = ['AAA', 'AAC', 'AAG', 'AAT']

# 'ACA', 'ACC', 'ACG', 'ACT',
# 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT',
# 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT',
# 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT',
# 'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT',
# 'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT',
# 'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT',
# 'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT']
name = []
for t in range(1,2989):
    u = '>neg' + ' ' + str(t)
    name.append(u)

data = DataFrame(index=[x for x in name], columns=[y for y in all])

for eachline in files:
    if eachline.startswith(">"):
        row = eachline.replace('\n' ,'')
    else:
        l = []
        dna = eachline
        for o in all:
            pattern = re.compile(o)
            count = pattern.findall(dna)
            for e in count:
                l.append(e)
                result = {}
                for i in set(l):
                    result[i] = l.count(i)
                    for key in result.keys():
                        for n in all:
                            if key == n:
                                data.loc[row,n] = result[key]

data.to_csv('/home/lirz/biostatistic/neg.csv')
