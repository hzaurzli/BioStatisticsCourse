import argparse

def k_mer(file ,k):
    files = open(file , "r", encoding=None)
    l = []
    for eachline in files:
        if eachline.startswith(">"):
            continue
        else:
            dna = eachline
            chr = 'N'
            if chr in dna:
                continue
            else:
                for i in range(len(dna)):
                    t = dna[i:i + k].replace('\n' ,'')
                    if (len(t)) == k:
                        l.append(t)
    return l

def all_list(file, k):
    arr = k_mer(file, k)
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

def write(file,finalfile,k):
    path = finalfile
    f = open(path, 'w', encoding='utf-8')
    D = all_list(file, k)
    for k, v in D.items():
        s2 = str(v)
        f.write(k + '\t')
        f.write(s2 + '\n')
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="To calculate count of kmers")
    parser.add_argument("-i", "--i", required=True, type=str, help="Input file")
    parser.add_argument("-o", "--o", required=True, type=str, help="Output file")
    parser.add_argument("-k", "--k", required=True, type=int, help="Number of kmer")
    Args = parser.parse_args()
    write(Args.i,Args.o,Args.k)
