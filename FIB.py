# rosalind bioinformatics stronghold FIB task
# Fibonaci

print("Hello! \n This programe helps with breeding rabbits and with Fibonacci sequence. Enjoy!\n")

months = int(input("How many months do you want to breed the rabbits? "))
offspring = int(input("How many litter does a pair of rabits reproduce? "))

rabbits = [1,1]

for i in range(2, months):
    rabbits.append(rabbits[i-1] + rabbits[i-2]*(offspring))
#1 1 4 7


print(rabbits[months-1])


