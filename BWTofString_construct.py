"""Burrows wheeler Transform
    -- form the rotations of suffixes
    --sort them in lexicographic order
    --concatenate the last character of each suffix into a string"""

def BWT_of_string(str):
    BWT_str_rot = []

    #Suffix rotations of a string
    for i in range(len(str)):
        BWT_str_rot.append(str[i:]+str[:i])
    BWT_str_rot.sort()
    BWT_str =""
    for i in range(len(BWT_str_rot)):
        BWT_str += BWT_str_rot[i][-1]
    print BWT_str

if __name__ == "__main__":

    #sample_str = "GCGTGCCTGGTCA$"
    sample_str = open('datasets/rosalind_ba9i.txt').read().strip()
    BWT_of_string(sample_str)