"""Rabbits remaining:
    month : n th month for which the rabbit count has to be calculated
    life : no. of months a rabbit can live
    if a rabbit > life, subtract the no. of rabbits from the count"""

def rabbits_remaining(month , life):
    rab = []
    rab.append(1)
    rab.append(1)
    i=2
    for i in range(2,month):
        if i < life:
            val = rab[i-1] + rab[i-2]
            rab.append(val)
        if i == life:
            val = rab[i-1] + rab[i-2] - 1
            rab.append(val)
        if i > life:
            rab.append((rab[i-1] + rab[i-2]) - rab[i-life-1])
    return rab.pop()

if __name__ == "__main__":

    """after_n = 6
    live_m = 3"""

    sample_dataset = open('datasets/rosalind_fibd.txt').read().strip().split()
    month = int(sample_dataset[0])
    life = int(sample_dataset[1])
    print rabbits_remaining(month,life)

