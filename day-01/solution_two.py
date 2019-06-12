final_frequency = 0
frequencies = list()
frequencies.append(final_frequency)
found_frequency = False
text = list()
eof_reached = False
text.append(int(input()))
counter = 0
while not eof_reached and not found_frequency:
    final_frequency += text[counter]
    if final_frequency in frequencies:
        found_frequency = True
    frequencies.append(final_frequency)
    try:
        text.append(int(input()))    
        counter += 1    
    except EOFError:
        eof_reached = True
counter = 0
n = len(text)
while not found_frequency:
    final_frequency += text[counter]
    if final_frequency in frequencies:
        found_frequency = True
    frequencies.append(final_frequency)
    counter = (counter + 1) % n
print(final_frequency)