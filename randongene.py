import math


def find_prob(dna_str, p):

    log_val = 0
    for s in dna_str:
        if s in "GC":
            log_val += (math.log(p / 2, 10))
        else:
            log_val +=  (math.log((1 - p) / 2, 10))
    return log_val


if __name__ == "__main__":

    sample_dataset = open('datasets/rosalind_prob.txt').read()
    s = sample_dataset.split()
    prob_set = map(float, s[1:])
    print ' '.join(map(str,  [find_prob(s[0], p) for p in prob_set]))
