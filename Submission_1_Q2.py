"""

 Suppose S= “AUGCUUCGAAUGCUGUAUGAUGUC” is an RNA sequence.

	(a) Find the number of A’s, U’s, G’s, and T’s in S.
	(b) Substitute U’s with T’s to get back DNA sequence
	(Note: DNA has ATGC alphabets and RNA has AUGC alphabets).
	(c) Read about the codon table (Search for “codon table for amino acids” on the internet),
	 create a codon table, and write which amino acids correspond to the three-letter codes in
	  the DNA sequence from step (b).

Note: I want you to create a dictionary for the complete codon table, and not simply assign
the three-letter code with the Amino acid symbol. There are 64 codons for 20 amino acids,
your dictionary should have all the 64 codons.
"""


def check_sequence_validity(sequence, allowed_characters):
    for ch in sequence:
        if ch not in allowed_characters:
            print(ch)
            return False
    return True


def calculate_frequency(sequence, sequence_type):
    try:
        sequence.upper()
        if sequence_type.upper() == 'RNA':
            allowed_characters = ['A', 'G', 'U', 'C']
        elif sequence_type.upper() == 'DNA':
            allowed_characters = ['A', 'G', 'U', 'T']
        else:
            raise Exception("Invalid sequence type")
            return
        if not check_sequence_validity(sequence, allowed_characters):
            raise ValueError("Invalid input")
            return
        f = {}
        for code in allowed_characters:
            f[code] = sequence.count(code)
        return f

    except ValueError:
        print("ERROR: Invalid RNA/DNA sequence. The sequence consists of only following characters: ", allowed_characters)
    except Exception:
        print("ERROR: sequence_type value can be \'RNA\' or \'DNA\'")


def print_frequency(f):
    print('\n\n\t The frequency dictionary is ', f)


def convert_sequence_RNA_to_DNA(RNA_sequence):
    RNA_sequence.upper()
    allowed_characters = ['A', 'G', 'U', 'C']
    try:
        if not check_sequence_validity(RNA_sequence, allowed_characters):
            raise ValueError("Invalid input")
            return
        DNA_sequence = RNA_sequence.replace('U', 'T')
        return DNA_sequence

    except ValueError:
        print("ERROR: Invalid RNA sequence. The RNA sequence consists of only following characters: ", allowed_characters)


def create_codon_table():
    codon = {'UUU': ('Phe', 'phenylalanine'),
             'UUC': ('Phe', 'phenylalanine'),
             'UUA': ('Phe', 'phenylalanine'),
             'UUG': ('Phe', 'phenylalanine'),

             'UCU': ('Ser', 'serine'),
             'UCC': ('Ser', 'serine'),
             'UCA': ('Ser', 'serine'),
             'UCG': ('Ser', 'serine'),

             'UAU': ('Tyr', 'tyrosine'),
             'UAC': ('Tyr', 'tyrosine'),
             'UAA': None,
             'UAG': None,

             'UGU': ('Cys', 'serine'),
             'UGC': ('Cys', 'serine'),
             'UGA': None,
             'UGG': ('Trp', 'serine'),



             'CUU': ('Leu', 'leucine'),
             'CUC': ('Leu', 'leucine'),
             'CUA': ('Leu', 'leucine'),
             'CUG': ('Leu', 'leucine'),

             'CCU': ('Pro', 'proline'),
             'CCC': ('Pro', 'proline'),
             'CCA': ('Pro', 'proline'),
             'CCG': ('Pro', 'proline'),

             'CAU': ('His', 'histidine'),
             'CAC': ('His', 'histidine'),
             'CAA': ('Gln', 'glutamine'),
             'CAG': ('Gln', 'glutamine'),

             'CGU': ('Arg', 'arginine'),
             'CGC': ('Arg', 'arginine'),
             'CGA': ('Arg', 'arginine'),
             'CGG': ('Arg', 'arginine'),



             'AUU': ('Ile', 'isoleucine'),
             'AUC': ('Ile', 'isoleucine'),
             'AUA': ('Ile', 'isoleucine'),
             'AUG': ('Ile', 'isoleucine'),

             'ACU': ('Thr', 'threonine'),
             'ACC': ('Thr', 'threonine'),
             'ACA': ('Thr', 'threonine'),
             'ACG': ('Thr', 'threonine'),

             'AAU': ('Asn', 'asparagine'),
             'AAC': ('Asn', 'asparagine'),
             'AAA': ('Lys', 'lysine'),
             'AAG': ('Lys', 'lysine'),

             'AGU': ('Ser', 'serine'),
             'AGC': ('Ser', 'serine'),
             'AGA': ('Arg', 'arginine'),
             'AGG': ('Arg', 'arginine'),



             'GUU': ('Val', 'valine'),
             'GUC': ('Val', 'valine'),
             'GUA': ('Val', 'valine'),
             'GUG': ('Val', 'valine'),

             'GCU': ('Ala', 'alanine'),
             'GCC': ('Ala', 'alanine'),
             'GCA': ('Ala', 'alanine'),
             'GCG': ('Ala', 'alanine'),

             'GAU': ('Asp', 'aspartic acid'),
             'GAC': ('Asp', 'aspartic acid'),
             'GAA': ('Glu', 'glutamic acid'),
             'GAG': ('Glu', 'glutamic acid'),

             'GGU': ('Gly', 'glycine'),
             'GGC': ('Gly', 'glycine'),
             'GGA': ('Gly', 'glycine'),
             'GGG': ('Gly', 'glycine'),
             }
    return codon


def print_codon_table():
    codon = create_codon_table()
    letters = ['U', 'C', 'A', 'G']
    print('\n\n===========================================================================')
    print('\t\t\t\t>>>>    Codon Table   <<<<<')
    print('===========================================================================\n')
    print('\tCode: \tAmino Acid Code\t\tAmino Acid Name')
    print('____________________________________________________________________________\n')
    for c1 in letters:
        for c2 in letters:
            for c3 in letters:
                s = c1 + c2 + c3
                if codon[s] is None:
                    print('\t', s, ': \tStop\t\t\t-----')
                else:
                    print('\t', s, ': \t', codon[s][0], '\t\t\t', codon[s][1])
            print()
        print('===========================================================================\n')


if __name__ == "__main__":
    RNA_sequence = 'AUGCUUCGAAUGCUGUAUGAUGUC'
    print_frequency(calculate_frequency(RNA_sequence, 'RNA'))
    print('\n\n\tRNA sequence: ', RNA_sequence, ' and converted DNA sequence: ', convert_sequence_RNA_to_DNA(RNA_sequence))
    print_codon_table()
