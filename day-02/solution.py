text = list()
eof_reached = False
text.append(input())
while not eof_reached:
    try:
        text.append(input())    
    except EOFError:
        eof_reached = True
text = sorted(text)
t = ""
num_diff = -1
for t in text:
    num_diff = -1
    found = False
    e = ""
    for e in text:
        if t != e:
            n = len(t)
            for i in range(n):
                if t[i] != e[i]:
                    if num_diff == -1:
                        num_diff = i
                    else:
                        num_diff = -1
                        break
            if num_diff != -1:
                found = True
                break
    if found:
        break
print(t[:num_diff]+t[num_diff+1:])        