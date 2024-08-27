#this program is to check if the vitamine is fat soluble or not.
#the fat soluble vitamins are : A D E K
#let fatsol be the variable for the fatsoluble and inp be the input.

fatsol = ["A","D","E","K"]
inp = input("Enter the vitamin: ").strip().upper()

#now lets put the condition.

if inp in fatsol:
    print("The vitamine is fatsoluble.")