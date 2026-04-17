piece =0
while piece < 6:

    if piece == 3:
        print(f"PEÇA NÚMERO {piece}")
        print("PEÇA DEFEITUOSA, DESCARTANDO...")
        print('-')
        piece += 1
        continue
    else:
        print(f"PEÇA NÚMERO {piece}")
        print("Inspecionando a peça...")
        print('-')
        piece += 1