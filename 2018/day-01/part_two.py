# Opens file, initialises the variable and list
fil = open("input.txt", "r")
frequency = [0]
final_frequency_found = False

# While there is no double frequency
while final_frequency_found != True:
    # Loops over the file, calculating the sum, and storing it in the list
    for line in fil:
        frequency.append(frequency[-1] + int(line))
        # If the last frequency is in the list
        if frequency[-1] in frequency[:-1]:
            # Set the condition so it leaves the while loop
            final_frequency_found == True  
            break  
    # Reset the seek        
    fil.seek(0) 

# Print the last value, which is the duplicate values
print(frequency[-1])

# Close the file
fil.close()