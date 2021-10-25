input_file1 = open("sequence1.txt")
sequence1 = input_file1.read()
input_file1.close()
length1 = len(sequence1) - 1

input_file2 = open("sequence2.txt")
sequence2 = input_file2.read()
input_file2.close()
length2 = len(sequence2) - 1

mutations = 0

if (length1 == length2):
    for i in range(length1):
        if (sequence1[i] != sequence2[i]):
            mutations += 1
else:
   print("sekwencje są różnej długości! \n")

print(mutations)
