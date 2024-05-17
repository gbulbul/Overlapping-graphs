dict_rosalind_to_dna_seq={}
dict_rosalind_to_dna_seq['Rosalind_0498']='AAATAAA'
dict_rosalind_to_dna_seq['Rosalind_2391']='AAATTTT'
dict_rosalind_to_dna_seq['Rosalind_2323']='TTTTCCC'
dict_rosalind_to_dna_seq['Rosalind_0442']='AAATCCC'
dict_rosalind_to_dna_seq['Rosalind_5013']='GGGTGGG'

from itertools import combinations
pairs_of_seq = list(combinations(dict_rosalind_to_dna_seq.values(), 2))
pairs_of_keys =list(combinations(dict_rosalind_to_dna_seq.keys(), 2))
print("All possible pairs : " + str(pairs_of_seq))
for pair in pairs_of_seq:
    #print(pair)
    if pair[0][3:]==pair[1][:-3] or pair[0][4:]==pair[1][:-4]:
       for keys in pairs_of_keys:
           if dict_rosalind_to_dna_seq[keys[0]]==pair[0]:
              if dict_rosalind_to_dna_seq[keys[1]]==pair[1]:
                  print(keys)