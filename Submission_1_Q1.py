"""
 DNA is made up of 4 nucleotides ATGC.
 Write a program to calculate the number of combinations of choosing 3 nucleotides from 4.
"""

def calculate_combinations():
    letters = ['A', 'T', 'G', 'C']
    combinations = []
    print('\n\n\t\t>>> All Possible Combinations  <<<')
    print('\n===========================================================')
    for c1 in letters:
        for c2 in letters:
            for c3 in letters:
                s = c1+c3+c2
                combinations += [s]
                print('\t', s, end = '\t')
            print()
        print('\n===========================================================')
    return combinations


if __name__ == "__main__":
    print('\n\n\t\tTotal combinations: ', len(calculate_combinations()))