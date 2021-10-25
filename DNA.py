# rosalind DNA task from bioinformatics stronghold
# counting nt occurance in given sequence.txt

input_file = open("sequence.txt")
sequence = input_file.read()
input_file.close()
input_length = len(sequence)

letter = ["A","C","G","T"]
count_letter = [0, 0, 0, 0] 

for j in range(4):
    for i in range(input_length-1):
      if sequence[i] == letter[j]:
         count_letter[j] += 1

#print(sequence)
#print(count_letter)

results_file = open("DNA_results.txt", "w+").write(str(count_letter).strip("[]"))
