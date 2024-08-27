#this program is to generate random DNA sequence upto a specific length
#we will be using the random module with the help of "import"
import random
#this it to get random number picker
nuc_tid = ['A', 'C', 'G', 'T'] #these are the nucleobases of DNA. DNA sequences are made of these.
dna_seq = "" #this is the sequence. here we create an empty string (initialize)
x = int(input("lenght of DNA sequence: ")) #we have to make this an int because we cannot use int<str in line 8.
while len(dna_seq) < x:
    dna_seq += random.choice(nuc_tid)
#+= is basically assignment operator. this is basically dna_seq= dna_seq+..
#random.choice(nuc_tid) selects a nucleotide randomly. It is a part of random function.
print("The DNA sequence is: "+ dna_seq)
