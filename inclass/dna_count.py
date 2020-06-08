s='CCACATGTTTGTAGGAATCGAATACTATGAGGGGGAAATAGTTGACCCGTGTCAGGCACGGAGTCGAATGGCCGAAGTCCTTCGCATAGACAAGGACTGTCCTCTTTCGGATAGGCGCATGGGGCCTCACTTACACGGCAGGGATCCTAGCGCCGCCCCTAGACCAAGAGTGTAAGCGGACTGGGTGCGACTATTTGAAGTTTGGGGCAGATCGATAGTAAAACGGGACCACGCAATAAGGGGAGTTATTAAAGTTCGACTAGCTTAACGCTATCTGACGAATAAGCGACATAACTGATCGCACTCATGATTATCGAGAGCCTTGCGACGATAACCTTCGAGTCATACACGCGGCCGATGGAATAAACAAATAAGCATGTTCCGTATGAGCACACCTTACATCGTGCTCTGCCGTAGCAGACTGGTGCACGCGTAGAGGAACTCGACCGGAGCAAACCGCGGGTATGCCAGATTGGGCCGCGGGTTACGATGCGATCGCGAGCATGGGCGTTGCTAAAAGAGCCGCGCGCGTTGCTGAATGTCGACGACCCCTTTGGGATGATTCACCTGTCTGAGTTGTCGATCCACCATCGCGTTGACTCAGGAGTTCAAAACCAGAACTTCGGTTCGGGAAGGTCAGGGTGGAAAAATGTTAATCTTTGTTTTTCAAGAGTATAAAGTATAGCTCTTCCAAGATGGTAACTCCTGTGGACGGACTAGCTAGTCGCATTGCCTAGCACGGCCCGTGCCGACATACAAGATCAGAAGGCCTGCCCAGTGGTCATTCGACCGGGGCAACTAGCGTTATGCTCTCCT'

L=['A','C','G','T']
cA,cC,cG,cT=0,0,0,0
for i in s:
   if i=='A':
       cA+=1
   elif i=='C':
        cC+=1
   elif i=='G':
        cG+=1
   else:
        cT+=1
print('A',cA,' C ',cC,' G ',cG,' T ',cT)


#ALTERNATIVE #2
def qt(s):
      return s.count("A"), s.count("G"), s.count("C"), s.count("T")

#ALTERNATIVE  #3
print(*[s.count(x) for x in ['A', 'C', 'G', 'T']])

#ALTERNATIVE  #4
print(*map(input('DNA: ').count, "ACGT"))
#map generates an Iterator. The * Operator expands the iterator to function arguments to the print function.
 
#ALTERNATIVE  #5
#!/usr/bin/python

# Open a data file.
fo = open("dna_count.txt", "r+")
s=fo.read()
fo.close()
print(s)
s1="A"
s2="C"
s3="G"
s4="U"
num1 = s.count(s1, 0, len(s))
num2 = s.count(s2, 0, len(s))
num3 = s.count(s3, 0, len(s))
num4 = s.count(s4, 0, len(s))
print(num1, num2, num3, num4)

#ALTERNATIVE  #6
file = open('./dna_count.txt', 'r')
string1 = file.read()
file.close()
freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in string1:
    freq[i] = freq[i] + 1
print(freq['A'], freq['C'], freq['G'], freq['T'])

#ALTERNATIVE  #7
ACGT = "ACGT"
count = [0,0,0,0]
for bp in open("dna_count.txt").read():
    count[ACGT.index(bp)] += 1
print(count)

#ALTERNATIVE  #8
f = open("dna_count.txt", "r") 
str = f.read()
f.close()
print(str.count('A'),str.count('C'),str.count('G'),str.count('T'))

#ALTERNATIVE  #9
s = open('dna_count.txt').read()
for c in 'ACGT':
    print(s.count(c))

#ALTERNATIVE  #10
dna = open('dna_count.txt', 'r').read()
print(" ".join([str(dna.count(x)) for x in 'ACGT']))

#ALTERNATIVE  #11
with open('dna_count.txt', 'r') as f1:
    s = f1.read()
    for c in 'ACGT': print(s.count(c))

#ALTERNATIVE  #12
with open('dna_count.txt') as fopen:
    dna  = next(fopen).strip()

counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for nt in dna:    
    counts[nt] += 1

print(counts['A'], counts['C'], counts['G'], counts['T'])

#ALTERNATIVE  #13
def count_base_rna(input_file):
    base_count_dict = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
    with open(input_file) as f:
        rna_str = f.read()
    for ch in rna_str:
        base_count_dict[ch] += 1
    print(base_count_dict['A'], base_count_dict['C'], base_count_dict['G'], base_count_dict['T'])

count_base_rna("dna_count.txt")

#ALTERNATIVE  #14 command line argument
#!/usr/bin/env python

import sys
from collections import defaultdict

def count_nuc(infile):
    nuc_count = defaultdict(int)
    inline = infile.readline()
    for c in inline:
        nuc_count[c] += 1
    return nuc_count

if __name__ == '__main__':
    ncount = count_nuc(open(sys.argv[1]))
    print(ncount['A'], ncount['C'], ncount['G'], ncount['T'])

#ALTERNATIVE   #15
#!/usr/bin/env python

dna = input('DNA :').strip()
out = []

for i in 'ACGT':
    out.append(str(dna.count(i)))

print(' '.join(out))

#ALTERNATIVE   #16
#!/usr/bin/env python
S = input('DNA :').rstrip()
print("%d %d %d %d" % tuple([S.count(X) for X in "ACGT"]))


# Generalized for reading and outputing character counts for sets of arbitrary length
#!/usr/bin/env python3

with open('dna_count.txt', 'r') as f:
    s = f.read().rsplit()
    count = {}
    for nt in set(s):
        count[nt] = s.count(nt)
    print(count_nts(s))
    
