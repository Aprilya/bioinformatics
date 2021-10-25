# rosalind.info REVC task from bioinformatics stronghold
# complementing a strand of DNA

input_file = open("sequence.txt")
sequence = input_file.read()
input_file.close()



sequence_length = len(sequence) - 1
compl_rev = ""

nt_dict = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C"
        }


for i in range(sequence_length):
       compl_rev =  nt_dict.get(sequence[i],"x") + compl_rev

#print(sequence)
#print(compl_rev)

results_file = open("REVC_results.txt","w+").write(compl_rev)

