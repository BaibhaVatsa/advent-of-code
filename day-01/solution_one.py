final_frequency = 0
text = int(input())
eof_reached = False
while not eof_reached:
    final_frequency += text
    try:
        text = int(input())
    except EOFError:
        eof_reached = True
print(final_frequency)