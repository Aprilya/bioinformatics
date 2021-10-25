# rosaling.info RNA task from bioinformatics stronghold
# transcribing coding DNA into RNA from sequence given in a sequence.txt

sequence = open('sequence.txt').read()
sequence_length = len(sequence)
RNA = ""

for i in range(sequence_length):
    if sequence[i] == "T":
        RNA += "U"
    else:
        RNA += sequence[i]

# print(sequence) #for comparision
# print(RNA)
result_file = open('RNA_results.txt', 'w+').write(RNA)




