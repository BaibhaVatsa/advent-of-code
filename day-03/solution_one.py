from numpy import zeros

fabric = zeros((1000, 1000), dtype=int)
eof_reached = False
num_overlapped = 0
while not eof_reached:
    try:
        text = str(input())
        at = int(text.find('@'))
        comma = int(text.find(','))
        colon = int(text.find(':'))
        xs = int(text.find('x'))
        ids = int(text[1 : at-1])
        xcoord = int(text[at+2 : comma])
        ycoord = int(text[comma+1 : colon])
        w = int(text[colon+2 : xs])
        h = int(text[xs+1 : ])
        for a in range(w):
            for b in range(h):
                num = fabric[xcoord+a][ycoord+b]
                if num == 0:
                    fabric[xcoord+a][ycoord+b] = ids
                elif num != -1:
                    fabric[xcoord+a][ycoord+b] = -1
                    num_overlapped += 1
    except EOFError:
        eof_reached = True
for a in range(1000):
    for b in range(1000):
        print(fabric[a][b], end=' ')
    print()
print(num_overlapped)