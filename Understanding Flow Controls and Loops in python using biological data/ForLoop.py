#now we will use For loop to count the number of Nucleobases in the DNA sequence.
dna_seq = input('Enter DNA sequence: ')

nuc_count={"A":0,"C":0,"G":0,"T":0} #here we are initializing the number of nucleotides.
for numb in dna_seq: #here numb is item.
    if numb in nuc_count:
        nuc_count[numb]+=1 #increment by 1 when it finds one

print(nuc_count)