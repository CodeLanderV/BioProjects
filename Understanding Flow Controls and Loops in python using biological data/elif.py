# This program detects if a nucleobase is found in DNA, RNA, or both.
# The two nucleic acids are DNA and RNA.

# Define nucleobases for DNA and RNA
dna_nuc = ["A", "T", "C", "G"]
rna_nuc = ["A", "U", "C", "G"]

# Take user input
nuc_inp = input("Please enter the nucleobase: ")

# Check the presence of nucleobase in DNA and RNA
if nuc_inp in dna_nuc and nuc_inp in rna_nuc:
    print(f"{nuc_inp} is found in both DNA and RNA.")
elif nuc_inp in dna_nuc:
    print(f"{nuc_inp} is found in DNA only.")
elif nuc_inp in rna_nuc:
    print(f"{nuc_inp} is found in RNA only.")
else:
    print(f"{nuc_inp} is not a valid nucleobase.")
