#!/usr/bin/ env python3 

##Q1 

#Selection single genome sequence 
genome = "TAAGGGGTGTCAAGGGGTGTGAAGGGGTGTTAAGGGGTTACAAGGGGTTAGAAGGGGTTATAAGGGGTTCCAAGGGGTTCGAAGGGGTTCTAAGGGGTTGCAAGGGGTTGGAAGGGGTTGTAAGGGGTTTCAAGGGGTTTGAAGGGGTTT"

#Function to generate kmers from a given sequence 
def kmer(genome, k): #Define function with 'genome' and 'k' 
    kmers = [] #Initialize an empty list to store kmers 
    for i in range(len(genome) - k + 1): #Loop through the genome sequence 
        kmers.append(genome[i:i + k]) #Extract a kmer of length 'k' and append it to the 'kmers' list 
    return kmers #Return the list of kmers 

# Set k as 5
k = 5

# Generate and print kmers for k=5
kmer_results = kmer(genome, k) #Call the 'kmer' function with the genome sequence and value of 'k', and store the results in 'kmer_results' 
print("k =", k, ":", kmer_results) #Print the value of 'k' and the generated kmers 


##Q2 

from collections import defaultdict  # Importing defaultdict from collections module

def kmer_and_subsequent(genome, k):
    kmers = defaultdict(set)
    for i in range(len(genome) - k * 2 + 1):  # Adjusted loop range
        kmer = genome[i:i + k]
        subsequent_kmer = genome[i + k:i + k * 2]  # Adjusted subsequent kmer extraction
        kmers[kmer].add(subsequent_kmer)  # Added subsequent_kmer directly to the set
    return kmers

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequence = ''  # Initialize an empty string to store the genome sequence
        for line in file:  # Iterate through each line in the FASTA file
            if not line.startswith('>'):  # Skip lines starting with '>'
                sequence += line.rstrip()  # Concatenate non-header lines to form the genome sequence
    return sequence  # Return the genome sequence read from the file


file_path = "../../shared/439539/reads.fa"  # Path to the FASTA file containing the genome sequence
genome = read_fasta(file_path)  # Read the genome sequence from the FASTA file
k = 2  # Set the value of k
kmer_results = kmer_and_subsequent(genome,k) # Generate kmers and their subsequent substrings
print("k =", k, ":", kmer_results)  # Print the value of k and the generated kmers and their subsequent substrings
 

##Q3 
#Open the file and read the contents into a single string, remove newline characters 
def find_smallest_k(filename):
    with open(filename, 'r') as file:
        sequence = file.read().replace('\n', '')
    k = len(sequence) #Initialize k to the length of the sequence 
    while k > 0: #Iterate over decreasing values of k 
        kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)] #Generate all possible kmers from the sequence 
        if len(set(kmers)) == len(kmers): #Check if all kmers are unique 
            return k #If all kmers are uniqe, return the current value of k 
        k -= 1 #Decrement k for the next iteration 
    return -1 #If no unique is found, return -1 

#File path 
filename = "../../shared/439539/reads.fa" 
print(find_smallest_k(filename)) #Call the function and print the result 

## k - value: 15727890
