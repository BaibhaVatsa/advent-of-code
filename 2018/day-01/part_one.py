# Opens file and initialises variable for sum
fil = open("input.txt", "r")
final_frequency = 0

# Loops over the file, calculating the sum
for line in fil:
    final_frequency += int(line)

# Prints the final result
print(final_frequency)

# Closes the file
fil.close()