import math #library to process the log command

#initialising the variables
AT = 0
GC = 0
array_b = []

#taking user input
dna_seq = input("Enter the DNA sequence:\n...").upper()

repeat = True
usr_input = ''
GC_content = []
while repeat==True:
    usr_input = input("Enter the GC-contents of the other strings. Enter 'finish' once you're done\n...")
    if usr_input == "finish":
        break
    else:
        GC_content.append(float(usr_input)) #float must be here otherwise 'finish' wont work

#counting AC and GC
AT = dna_seq.count("A") + dna_seq.count("T")
GC = dna_seq.count("G") + dna_seq.count("C")

#calculating log(probability)
def probability():
    for x in GC_content:
        array_b.append( math.log( ( (x/2)**GC ) * ( ( (1-x)/2)**AT ), 10 ) )
    return(array_b)

print(probability())





























