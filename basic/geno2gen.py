import sys

def sars2(pos):
    gene = ""
    gene_pos = 0

    if pos <= 265:
        gene = "5UTR"
        gene_pos = pos
    elif pos > 265 and pos <= 21562:
        gene = "1ab"
        gene_pos = pos - 265
    elif pos > 21562 and pos <= 25384:
        gene = "s"
        gene_pos = pos - 21562
    elif pos > 25392 and pos <= 26220:
        gene = "3a"
        gene_pos = pos - 25392
    elif pos > 26244 and pos <= 26472:
        gene = "E"
        gene_pos = pos - 26244
    elif pos > 26523 and pos <= 27191:
        gene = "M"
        gene_pos = pos - 26523
    elif pos > 27202 and pos <= 27387:
        gene = "6"
        gene_pos = pos - 27202
    elif pos > 27394 and pos <= 27759:
        gene = "7a"
        gene_pos = pos - 27394
    elif pos > 27894 and pos <= 28259:
        gene = "8"
        gene_pos = pos - 27894
    elif pos > 28274 and pos <= 29533:
        gene = "N"
        gene_pos = pos - 28274
    elif pos > 29558 and pos <= 29674:
        gene = "10"
        gene_pos = pos - 29558
    elif pos > 29675 and pos <= 29903:
        gene = "3UTR"
        gene_pos = pos - 29675

    return gene, gene_pos

def ev_aa(pos):
    gene = ""
    gene_pos = 0

    if pos <= 69:
        gene = "VP4"
        gene_pos = pos
    elif pos > 69 and pos <= 317:
        gene = "VP2"
        gene_pos = pos - 69
    elif pos > 317 and pos <= 552:
        gene = "VP3"
        gene_pos = pos - 317
    elif pos > 552 and pos <= 861:
        gene = "VP1"
        gene_pos = pos - 552
    elif pos > 861 and pos <= 1008:
        gene = "2A"
        gene_pos = pos - 861
    elif pos > 1008 and pos <= 1107:
        gene = "2B"
        gene_pos = pos - 1008
    elif pos > 1107 and pos <= 1437:
        gene = "2C"
        gene_pos = pos - 1107
    elif pos > 1437 and pos <= 1526:
        gene = "3A"
        gene_pos = pos - 1437
    elif pos > 1526 and pos <= 1548:
        gene = "3B"
        gene_pos = pos - 1526
    elif pos > 1548 and pos <= 1761:
        gene = "3C"
        gene_pos = pos - 1548
    elif pos > 1761 and pos <= 2188:
        gene = "3D"
        gene_pos = pos - 1761

    return gene, gene_pos


def e11_aa(pos):
    gene = ""
    gene_pos = 0

    if pos <= 69:
        gene = "VP4"
        gene_pos = pos
    elif pos > 69 and pos <= 331:
        gene = "VP2"
        gene_pos = pos - 69
    elif pos > 331 and pos <= 569:
        gene = "VP3"
        gene_pos = pos - 331
    elif pos > 569 and pos <= 861:
        gene = "VP1"
        gene_pos = pos - 569
    elif pos > 861 and pos <= 1011:
        gene = "2A"
        gene_pos = pos - 861
    elif pos > 1011 and pos <= 1110:
        gene = "2B"
        gene_pos = pos - 1011
    elif pos > 1110 and pos <= 1439:
        gene = "2C"
        gene_pos = pos - 1110
    elif pos > 1439 and pos <= 1528:
        gene = "3A"
        gene_pos = pos - 1439
    elif pos > 1528 and pos <= 1550:
        gene = "3B"
        gene_pos = pos - 1528
    elif pos > 1550 and pos <= 1733:
        gene = "3C"
        gene_pos = pos - 1550
    elif pos > 1733 and pos <= 2195:
        gene = "3D"
        gene_pos = pos - 1733

    return gene, gene_pos

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python geno2gen.py sars2/ev_aa/e11_aa geno_pos")
        sys.exit(1)

    pos = int(sys.argv[2])

    if sys.argv[1] == "sars2":
        gene, gene_pos = sars2(pos)
    elif sys.argv[1] == "ev_aa":
        gene, gene_pos = ev_aa(pos)
    elif sys.argv[1] == "e11_aa":
        gene, gene_pos = e11_aa(pos)
    else:
        print("Usage: python geno2gen.py virus geno_pos")
        sys.exit(1)        

    print(f"{gene}-{gene_pos}")
