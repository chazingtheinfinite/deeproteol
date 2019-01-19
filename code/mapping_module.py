import math

# Amino Acid Codon Mapping: https://www.mathworks.com/help/bioinfo/ref/aa2nt.html
AA2DNA = {
        'A': ['GCT', 'GCC', 'GCA', 'GCG'], # Alanine
        'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], # Arginine
        'N': ['AAT', 'AAC'], # Asparagine
        'D': ['GAT', 'GAC'], # Aspartic Acid (Aspartate)
        'C': ['TGT', 'TGC'], #Cysteine
        'Q': ['CAA', 'CAG'], # Glutamine
        'E': ['GAA', 'GAG'], # Glutamic acid (Glutamate)
        'G': ['GGT', 'GGC', 'GGA', 'GGG'], # Glycine
        'H': ['CAT', 'CAC'], # Histidine
        'I': ['ATT', 'ATC', 'ATA'], # Isoleucine
        'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], # Leucine
        'K': ['AAA', 'AAG'], # Lysine
        'M': ['ATG'], # Methionine
        'F': ['TTT', 'TTC'], # Phenylalanine
        'P': ['CCT', 'CCC', 'CCA', 'CCG'], # Proline
        'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], # Serine
        'T': ['ACT', 'ACC', 'ACA', 'ACG'], # Threonine
        'W': ['TGG'], # Tryptophan
        'Y': ['TAT', 'TAC'], # Tyrosine
        'V': ['GTT', 'GTC', 'GTA', 'GTG'], # Valine
        'U': ['UAG', 'UAA', 'UGA'], # Stop Codons
        'B': ['GAT', 'GAC', 'AAT', 'AAC'], # Aspartic Acid or Asparagine
        'Z': ['GAA', 'GAG', 'CAA', 'CAG'], # Glutamic Acid or Glutamine
        'X': ['GCT', 'GCC', 'GCA', 'GCG', 'CGT', 'CGC', # Any Amino Acid
              'CGA', 'CGG', 'AGA', 'AGG','AAT', 'AAC', 
              'GAT', 'GAC','TGT', 'TGC','CAA', 'CAG',
              'GAA', 'GAG','GGT', 'GGC', 'GGA', 'GGG',
              'CAT', 'CAC','ATT', 'ATC', 'ATA','TTA', 
              'TTG', 'CTT', 'CTC', 'CTA', 'CTG','AAA', 
              'AAG','TTT', 'TTC','CCT', 'CCC', 'CCA', 
              'CCG','TCT', 'TCC', 'TCA', 'TCG', 'AGT', 
              'AGC','ACT', 'ACC', 'ACA', 'ACG','TGG',
              'TAT', 'TAC','GTT', 'GTC', 'GTA', 'GTG']
        }

# For consistent plotting purposes
colour_map = {
            'hsapiens': '#53408F',
            'scerevisiae': '#CFB94F',
            'athaliana': '#78B846',
            'mmusculus': '#BB4768',
            'celegans': '#333333'
            }

# Series of variables and functions for plotting Amino Acids
def create_icosagon_dict(radius):
    """ create_icosagon_dict
        Generates a dictionary with coordinates
        for each amino acid position.
        Input : radius, assumed to be the central pixel of the image
        Output: icosagon_dict, a mapping of amino acid to pixel coordinates (as 2-tuple)
    """
    icosagon_dict = {}
    # Counterclockwise ordering of amino acids, sstarting at degree 0 (Eastwards)
    aa_order = ['A', 'P', 'V', 'L', 'I', 'M', 'F', 'W', 'D', 'E', 'S', 'T', 'C', 'N', 'Q', 'Y', 'K', 'H', 'R', 'G']
    degree = 0
    for aa in aa_order:
        # Must ensure to add radius to each to translate the origin
        x_pixel = int(radius * math.cos(degree)) + radius
        y_pixel = int(radius * math.sin(degree)) + radius
        icosagon_dict[aa] = (x_pixel, y_pixel)
        degree += 18
    return icosagon_dict



def create_icosagon(radius):
    icodict = {'M' : (radius, 0), # North Cardinal
               'F' : (radius - math.cos(108), ),
            
            }
    # Quadrant 1:
    



