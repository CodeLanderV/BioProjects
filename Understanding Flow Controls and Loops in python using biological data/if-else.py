#this is a program to check if the amino acid is essential or not
#let ess_amine be the set of essential amino acids

es_amin = ["Histidine","Lysine","Threonine","Tryptophan","Valine"]

#let ent_amin be the entry of the amino
ent_amin = input("Please enter the amino acid: ")
if ent_amin in es_amin:
    print("The entered acid is an amino acid")
else:
    print("The entered acid is not an amino acid")
