import math
"""
 DNA is made up of 4 nucleotides ATGC.
 Write a program to calculate the number of combinations of choosing 3 nucleotides from 4.
 
 Solution:
 Here I have defined two different function. 
 1. calculate_combinations()
 It prints total possible combinations using the nCr formula, 
 total combinations here = 4C1 * 4C1 * 4C1 * (4C1)^3

 2. print_combinations()
 It prints all possible combinations
"""


def calculate_combinations():
    n = 4
    r = 1

    def nCr(n, r):
        ans = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        return ans

    return int(nCr(n, r)**3)


def print_combinations():
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
    print('\n\n\t\tTotal combinations using function 1: ', calculate_combinations())
    print('\n\n\t\tTotal combinations using function 2: ', len(print_combinations()))
