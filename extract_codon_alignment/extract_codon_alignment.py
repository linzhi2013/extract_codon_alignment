#!/usr/bin/env python3
import sys
from Bio import SeqIO
import argparse


def get_para():
    desc = """
    To extract some codon positions (1st, 2nd, 3rd) from a CDS alignment.
    """
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--alignedCDS', metavar='<file>', required=True,
        help='The CDS alignment.')

    parser.add_argument('--aln_format', metavar='<format>', default='fasta',
        help='the file format for the CDS alignment. Anything accepted by BioPython is fine [%(default)s]')

    parser.add_argument('--codonPoses', type=int,
        choices=[1, 2, 3, 12, 13, 23], default=12,
        help='Codon position(s) to be extracted [%(default)s]')

    parser.add_argument('--outAln', metavar='<file>', required=True,
        help='output file name')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


def extract_codon_alignment(alignedCDS=None, aln_format='fasta', codonPoses=1, outAln='out.aln'):
    """
    To extract some codon positions (1st, 2nd, 3rd) from a CDS alignment.

    Parameters:
    alignedCDS : string
        The CDS alignment.
    aln_format: string
        the file format for the CDS alignment. Anything accepted by
        BioPython is fine
    codonPoses: int(s)
        extract which codon position(s), values can be: 1, 2, 3, or
        12, 13, 23

    Returns
    -------
    outAln: string
        the extracted alignment

    """
    if codonPoses not in [1, 2, 3, 12, 13, 23]:
        raise ValueError('codonPoses must be one of [1, 2, 3, 12, 13, 23]')

    codonPoses = list(str(codonPoses))
    codonPoses = [int(j) for j in codonPoses]

    fhout = open(outAln, 'w')
    for rec in SeqIO.parse(alignedCDS, aln_format):
        seqid = '>' + rec.description
        seq = str(rec.seq)
        new_seq = []
        for i in range(0, len(seq), 3):
            tup = seq[i:i+3]
            for pos in codonPoses:
                if pos <= len(tup):
                    base = tup[pos-1]
                    new_seq.append(base)
        new_seq = ''.join(new_seq)
        print(seqid, new_seq, sep='\n', file=fhout)

    fhout.close()

    return outAln


def main():
    arg = get_para()
    extract_codon_alignment(
        alignedCDS=arg.alignedCDS,
        aln_format=arg.aln_format,
        codonPoses=arg.codonPoses,
        outAln=arg.outAln)

if __name__ == '__main__':
    main()









