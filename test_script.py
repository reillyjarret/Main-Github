#!/usr/bin/ env python3 

#import pytest
import pytest 
from Final_Exam import kmer #Import kmer from Final_Exam script 
from Final_Exam import kmer_and_subsequent #Import kmer_and_subsequent from Final_Exam script 
from Final_Exam import find_smallest_k #Import find_smallest_k from Final_Exam script 

#Define a test function for testing the kmer function
def test_kmer():
    genome = "TAAGGGGTGTCAAGGGGTGTGAAGGGGTGTTAAGGGGTTACAAGGGGTTAGAAGGGGTTATAAGGGGTTCCAAGGGGTTCGAAGGGGTTCTAAGGGGTTGCAAGGGGTTGGAAGGGGTTGTAAGGGGTTTCAAGGGGTTTGAAGGGGTTT"
    k = 5
    expected_result = ['TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTC', 'TGTCA', 'GTCAA', 'TCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTG', 'TGTGA', 'GTGAA', 'TGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTT', 'TGTTA', 'GTTAA', 'TTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAC', 'TTACA', 'TACAA', 'ACAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAG', 'TTAGA', 'TAGAA', 'AGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAT', 'TTATA', 'TATAA', 'ATAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCC', 'TTCCA', 'TCCAA', 'CCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCG', 'TTCGA', 'TCGAA', 'CGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCT', 'TTCTA', 'TCTAA', 'CTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGC', 'TTGCA', 'TGCAA', 'GCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGG', 'TTGGA', 'TGGAA', 'GGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGT', 'TTGTA', 'TGTAA', 'GTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT', 'GTTTC', 'TTTCA', 'TTCAA', 'TCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT', 'GTTTG', 'TTTGA', 'TTGAA', 'TGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT']

    result = kmer(genome, k) #Call the kmer function with the genome and k value
    assert result == expected_result #Assert that the result matches the expected result 

#Define a test function for testing the kmer_and_subsequent function
def test_kmer_and_subsequent():
    file_path = "../../shared/439539/reads.fa" 
    k = 2
    expected_result = {
        'GA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'AA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GG', 'TT', 'CA', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'AT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'CA', 'GA', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'TT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'TC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'CA', 'GA', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'CT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'CG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'GT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'TT', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'TA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'TT', 'GG', 'TA', 'TG', 'GC', 'C', 'AG', 'AA', 'CT'}, 'CA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'GG', 'CA', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'TG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GG', 'TT', 'CA', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'AC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'GA', 'CA', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'AG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'GG', 'CA', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'GC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'TT', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'CC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GG', 'CA', 'TT', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'GG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}
    }

    result = kmer_and_subsequent #Call the function with kmer_and_subsequent 
    assert result == kmer_and_subsequent #Assert that the result is the expected result of kmer_and_subsequent strings

#Define a test function to determine the smallest possible value of k 
def test_find_smallest_k():
    filename = "test_input.txt"  # Create a test input file with known content
    with open(filename, 'w') as file:
        file.write("../../shared/439539/reads.fa")  

    expected_result = 15727890 #The expected result of the test 

    result = find_smallest_k(filename) #Call the function with the smallest k value in the file
    assert result == find_smallest_k(filename) #Assert that the result is the expected result
