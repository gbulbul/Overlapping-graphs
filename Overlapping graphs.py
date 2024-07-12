dict_rosalind_to_dna_seq={}
dict_rosalind_to_dna_seq['Rosalind_0498']='AAATAAA'
dict_rosalind_to_dna_seq['Rosalind_2391']='AAATTTT'
dict_rosalind_to_dna_seq['Rosalind_2323']='TTTTCCC'
dict_rosalind_to_dna_seq['Rosalind_0442']='AAATCCC'
dict_rosalind_to_dna_seq['Rosalind_5013']='GGGTGGG'
class possible_pairs:
    def pairs_for_values(dict_rosalind_to_dna_seq):
        pairs_of_values_=[]
        for value1 in dict_rosalind_to_dna_seq.values():
            for value2 in dict_rosalind_to_dna_seq.values():
                if value1!=value2 and ((value2,value1)) not in pairs_of_values_:
                   pairs_of_values_.append((value1,value2))
        return pairs_of_values_
    def pairs_for_keys(dict_rosalind_to_dna_seq):
        pairs_of_keys_=[]
        for key1 in dict_rosalind_to_dna_seq.keys():
            for key2 in dict_rosalind_to_dna_seq.keys():
                if key1!=key2 and ((key2,key1)) not in pairs_of_keys_:
                   pairs_of_keys_.append((key1,key2))
        return pairs_of_keys_
   
    def pairs_satisfy_condition(dict_rosalind_to_dna_seq,pairs_of_seq,pairs_of_keys):
        for pair in pairs_of_seq:
            if pair[0][3:]==pair[1][:-3] or pair[0][4:]==pair[1][:-4]:
               for keys in pairs_of_keys:
                   if dict_rosalind_to_dna_seq[keys[0]]==pair[0] and dict_rosalind_to_dna_seq[keys[1]]==pair[1]:
                      print(keys)
if __name__=="__main__":
   pairs_of_seq=possible_pairs.pairs_for_values(dict_rosalind_to_dna_seq)
   pairs_of_keys=possible_pairs.pairs_for_keys(dict_rosalind_to_dna_seq)
   possible_pairs.pairs_satisfy_condition(dict_rosalind_to_dna_seq,pairs_of_seq,pairs_of_keys)
