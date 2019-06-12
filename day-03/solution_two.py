from numpy import zeros

fabric = zeros((1000, 1000), dtype=int)
eof_reached = False
no_overlaps = list()
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
        num_overlaps = 0
        for a in range(w):
            for b in range(h):
                num = fabric[xcoord+a][ycoord+b]
                if num == 0:
                    fabric[xcoord+a][ycoord+b] = ids
                else:
                    fabric[xcoord+a][ycoord+b] = -1
                    num_overlaps += 1
        if num_overlaps == 0:
            no_overlaps.append((ids, xcoord, ycoord, w, h))
    except EOFError:
        eof_reached = True
for no_overlap in no_overlaps:
    (ids, xcoord, ycoord, w, h) = no_overlap
    num_overlaps = 0
    for a in range(w):
        for b in range(h):
            num = fabric[xcoord+a][ycoord+b]
            if num == -1:
                num_overlaps += 1
                break
        if num_overlaps > 0:
            break
    if num_overlaps == 0:
        print(ids)
        break