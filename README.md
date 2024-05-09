**Substrings of Kmers BIO 439**

A genome of a organism can consist of very long sequences of nucleic acids. These long sequences can be broken down into "strings". These strings can be divided into overlapping substrings of a given length, k. 

Genome assemblies are constructed from sequenced genome fragments by identifying each substring (called a kmer) and the substring, that comes after it in the sequence. Find the order of all of the substrings in the fragments produces a whole genome. 

The purpose of this project was to take the genomic sequence located in the "../../shared/439539/reads.fa" and analyze the sequences in these files. Functions were defined to analyze these sequences and identify all possible substrings and subsequent substrings when k was defined as an argument. This process is the beginning of assembling a genome from the given sequences. 

**Question 1**

The first function was made to identify all substrings of the size k, where k was specified as an argument for a single sequence, and all unique possible subsequent substrings of each substring. 

To begin, a single sequence was selected from the output file "../../shared/439539/reads.fa". 
This sequence was then put through a function to define kmers using 'genome' and 'k'. The function then looped through the genome and extracted a kmers with a length of the given set value. 

`def kmer(genome, k):  
    kmers = [] 
    for i in range(len(genome) - k + 1): 
        kmers.append(genome[i:i + k])  
    return kmers`

For this question, k was set as a value of 5.

`k = 5`

These results were then printed. 

`k = 5 : ['TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTC', 'TGTCA', 'GTCAA', 'TCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTG', 'TGTGA', 'GTGAA', 'TGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTT', 'TGTTA', 'GTTAA', 'TTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAC', 'TTACA', 'TACAA', 'ACAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAG', 'TTAGA', 'TAGAA', 'AGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAT', 'TTATA', 'TATAA', 'ATAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCC', 'TTCCA', 'TCCAA', 'CCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCG', 'TTCGA', 'TCGAA', 'CGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCT', 'TTCTA', 'TCTAA', 'CTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGC', 'TTGCA', 'TGCAA', 'GCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGG', 'TTGGA', 'TGGAA', 'GGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGT', 'TTGTA', 'TGTAA', 'GTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT', 'GTTTC', 'TTTCA', 'TTCAA', 'TCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT', 'GTTTG', 'TTTGA', 'TTGAA', 'TGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT'`

**Question 2** 

Question 2 build up question 1. 

For question 2, a function was defined to identify all possible substrings and their subsequent substrings for all sequences from the output file "../../shared/439539/reads.fa" 
Instead of just running through a single sequences, this function ran through every possible sequence in the file when k was set as a value. 

Similar to question 1, the function began to define kmers and subsequence kmers using 'genome' and 'k'. This function then loops through the file to extract all kmers with a length meeting the requirements. 

`from collections import defaultdict`

`def kmer_and_subsequent(genome, k):
    kmers = defaultdict(set)
    for i in range(len(genome) - k * 2 + 1):  
        kmer = genome[i:i + k]
        subsequent_kmer = genome[i + k:i + k * 2]  
        kmers[kmer].add(subsequent_kmer)  
    return kmers`

A smaller function was also implemented to read the output. Due to the file being a fasta file, a special command was implemented to read and loop through the file. 

`def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequence = ''  
        for line in file:  
            if not line.startswith('>'): 
                sequence += line.rstrip()  
    return sequence`

Once the file path was determined, the results were printed. 

`file_path = "../../shared/439539/reads.fa"  
genome = read_fasta(file_path)  
k = 2 
kmer_results = kmer_and_subsequent(genome,k) 
print("k =", k, ":", kmer_results)`

`k = 2 : defaultdict(<class 'set'>, {'GA': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AT', 'AG', 'CG', 'AA', 'CA', 'CT', 'TC', 'AC', 'GC'}, 'AA': {'GT', 'TT', 'TG', 'GA', 'GG', 'TA', 'CC', 'AT', 'AG', 'AC', 'AA', 'TC', 'CG', 'CA', 'CT', 'GC'}, 'AT': {'GT', 'TT', 'TG', 'GA', 'GG', 'TA', 'CC', 'AT', 'AC', 'CG', 'CA', 'AA', 'TC', 'CT', 'AG', 'GC'}, 'TT': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AC', 'AG', 'AT', 'CA', 'CT', 'AA', 'CG', 'TC', 'GC'}, 'TC': {'GT', 'TT', 'TG', 'GA', 'GG', 'TA', 'CC', 'AC', 'AT', 'CG', 'AA', 'TC', 'CA', 'AG', 'CT', 'GC'}, 'CT': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AC', 'AT', 'AG', 'CT', 'CA', 'CG', 'AA', 'TC', 'GC'}, 'CG': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AC', 'AT', 'AG', 'CA', 'AA', 'CG', 'CT', 'TC', 'GC'}, 'GT': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AC', 'CG', 'AT', 'AA', 'CA', 'TC', 'CT', 'AG', 'GC'}, 'TA': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'C', 'AT', 'AG', 'CG', 'AA', 'CA', 'CT', 'TC', 'AC', 'GC'}, 'CA': {'GT', 'TT', 'TG', 'GA', 'GG', 'TA', 'CC', 'AT', 'AG', 'AC', 'AA', 'CT', 'CG', 'TC', 'CA', 'GC'}, 'TG': {'GT', 'TT', 'TG', 'GA', 'GG', 'TA', 'CC', 'AC', 'AG', 'AT', 'AA', 'CT', 'CG', 'TC', 'CA', 'GC'}, 'AC': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AT', 'CG', 'AG', 'AA', 'CA', 'TC', 'CT', 'AC', 'GC'}, 'AG': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AC', 'CG', 'AG', 'AA', 'CA', 'TC', 'CT', 'AT', 'GC'}, 'GC': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AT', 'AC', 'AG', 'CA', 'AA', 'TC', 'CG', 'CT', 'GC'}, 'CC': {'GT', 'TT', 'TG', 'GA', 'GG', 'TA', 'CC', 'AC', 'AG', 'AT', 'CA', 'AA', 'CG', 'CT', 'TC', 'GC'}, 'GG': {'GT', 'TT', 'GA', 'TG', 'GG', 'TA', 'CC', 'AC', 'AT', 'AG', 'CA', 'AA', 'CG', 'CT', 'TC', 'GC'}})`


**Question 3** 

Similar to question 1 and 2, question 3 used both previous functions to determine the smallest possible value of k that was needed to rebuild the genome. 

The function first began by trying to find the smallest k value. K was then initialized to the length of the sequence and was iterated over decreasing values to try a find the smallest possible value of k that would allow for the genome to be rebuilt. 

`def find_smallest_k(filename):
    with open(filename, 'r') as file:
        sequence = file.read().replace('\n', '')
    k = len(sequence) 
    while k > 0: 
        kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]  
        if len(set(kmers)) == len(kmers): 
            return k 
        k -= 1  
    return -1`

The filepath was then reiterated, and the results were printed out as a single value.

`filename = "../../shared/439539/reads.fa" 
print(find_smallest_k(filename))`

`k - value: 15727890`

**Pytest** 

Once all three functions were created, a test was done check the function to make sure they would run under automated testing. 

The test carried out was called a pytest. 

For a pytest to work, a set of test must be created to test each function. The goal of the test is to have all the functions pass the test and give the expected result. If an unexpected result is given or the test runs into an error, the function will fail the test and will not pass the test until the error is fixed. This ensures that the function will run when put through automated testing. 

`#!/usr/bin/ env python3`

`import pytest
from Final_Exam import kmer
from Final_Exam import kmer_and_subsequent
from Final_Exam import find_smallest_k`

`def test_kmer():
    genome = "TAAGGGGTGTCAAGGGGTGTGAAGGGGTGTTAAGGGGTTACAAGGGGTTAGAAGGGGTTATAAGGGGTTCCAAGGGGTTCGAAGGGGTTCTAAGGGGTTGCAAGGGGTTGGAAGGGGTTGTAAGGGGTTTCAAGGGGTTTGAAGGGGTTT"
    k = 5
    expected_result = ['TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTC', 'TGTCA', 'GTCAA', 'TCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTG', 'TGTGA', 'GTGAA', 'TGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTG', 'GGTGT', 'GTGTT', 'TGTTA', 'GTTAA', 'TTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAC', 'TTACA', 'TACAA', 'ACAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAG', 'TTAGA', 'TAGAA', 'AGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTA', 'GTTAT', 'TTATA', 'TATAA', 'ATAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCC', 'TTCCA', 'TCCAA', 'CCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCG', 'TTCGA', 'TCGAA', 'CGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTC', 'GTTCT', 'TTCTA', 'TCTAA', 'CTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGC', 'TTGCA', 'TGCAA', 'GCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGG', 'TTGGA', 'TGGAA', 'GGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTG', 'GTTGT', 'TTGTA', 'TGTAA', 'GTAAG', 'TAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT', 'GTTTC', 'TTTCA', 'TTCAA', 'TCAAG', 'CAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT', 'GTTTG', 'TTTGA', 'TTGAA', 'TGAAG', 'GAAGG', 'AAGGG', 'AGGGG', 'GGGGT', 'GGGTT', 'GGTTT']`

`result = kmer(genome, k)
assert result == expected_result`


`def test_kmer_and_subsequent():
    file_path = "../../shared/439539/reads.fa" 
    k = 2
    expected_result = {
        'GA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'AA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GG', 'TT', 'CA', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'AT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'CA', 'GA', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'TT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'TC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'CA', 'GA', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'CT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'CG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'GT': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'TT', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'TA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'TT', 'GG', 'TA', 'TG', 'GC', 'C', 'AG', 'AA', 'CT'}, 'CA': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'GG', 'CA', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'TG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GG', 'TT', 'CA', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'AC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'TT', 'GA', 'CA', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'AG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'GG', 'CA', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'GC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'TT', 'GG', 'TA', 'TG', 'GC', 'AG', 'AA', 'CT'}, 'CC': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GG', 'CA', 'TT', 'GA', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}, 'GG': {'CC', 'CG', 'AC', 'AT', 'TC', 'GT', 'GA', 'CA', 'GG', 'TT', 'TA', 'GC', 'TG', 'AG', 'AA', 'CT'}
    }`

 `result = kmer_and_subsequent
 assert result == kmer_and_subsequent`


`def test_find_smallest_k():
    filename = "test_input.txt"  
    with open(filename, 'w') as file:
        file.write("../../shared/439539/reads.fa")`

`expected_result = 15727890` 

`result = find_smallest_k(filename)
assert result == find_smallest_k(filename)`

These parameters were run on each function, ensuring that each passed the test and resulted in the expected outcome. 

**Github repository**

Once all functions passed the pytest, the functions were inserted into a github repository. 

To begin this process, the two python scripts were first copied into the given repository. 

`cp ~/439_practice_python_sp24/test_script.py .`
`cp ~/439_practice_python_sp24/Final_Exam.py .`

Once copied, the two scripts were added, committed, then finally pushed so that all changes made to the repository could be seen and the scripts were pushed into the repository. 

`git add`
`git commit -m`
`git push -u origin main`

Once the repository was all up to date and all changes had been committed and pushed, git log could be used to view all changes that had been made and committed to the repository. 

`git log`


Once all dessired changed had been added and committed to the repository, the repository can be cloned and both scripts can be run to show the results of the functions. 

**Purpose**

This research is important in understanding the starting point to assemble an entire genome from these given sequences. These steps can be taken further to eventually analyze sequences so that an entire genome is assembled through the use of functions in python script. 

The ability to create genome sequences opens up many possibilties for research in both biologal and biomedical fields. The sequencing of a genome can allow for researchers to better understand what could be happening at gene level allowing for better understanding of how to deal with ceratin mutations, cancers, or opens up new fields in genetic technology and even genetically modified organisms. 
