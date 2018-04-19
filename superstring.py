def superstr(input, con=''):
    if len(input) == 0:
        return con

    elif len(con) == 0:
        con = input.pop(0)
        return superstr(input, con)


    else:
        for i in range(len(input)):
            a = input[i]
            l = len(a)

            for x in range(l / 2):
                y = l - x

                "recursively calling superstr func to check the matching pattern"
                if con.startswith(a[x:]):
                    input.pop(i)
                    return superstr(input, a[:x] + con)

                if con.endswith(a[:y]):
                    input.pop(i)
                    return superstr(input, con + a[y:])


if __name__ == "__main__":

    sample_dataset = open('datasets/rosalind_long.txt').read()

    strings = []
    name = ""
    seq = ""
    strings = []
    for line in sample_dataset.strip().split():

        if line.startswith(">"):
            strings.append(''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    strings.append(''.join(seq))
    strings.pop(0)

    print superstr(strings)