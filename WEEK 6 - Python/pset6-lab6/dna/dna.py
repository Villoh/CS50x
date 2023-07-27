import csv
import sys


def main():

    # Check for command-line usage
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    dna_database = sys.argv[1]
    dna_persons = []

    with open(dna_database) as database:
        reader = csv.DictReader(database)
        for row in reader:
            dna_persons.append(row)

    # Read DNA sequence file into a variable
    sequence = sys.argv[2]

    with open(sequence, "r") as sequence:
        dna_sequence = sequence.read()

    # Get all the subssequences from the database, 0 is the name so w want all after 0.
    subsequences = list(dna_persons[0].keys())[1:]

    # Find longest match of each STR in DNA sequence
    subsequence_counts = {subsequence: 0 for subsequence in subsequences}

    # Get all the subsequence count for each subsequence
    for subsequence in subsequences:
        subsequence_counts[subsequence] = longest_match(dna_sequence, subsequence)

    # Check database for matching profiles
    for dna_person in dna_persons:
        match = 0

        # Loop each subsequence in search of equal counts
        for subsequence in subsequence_counts:
            if int(dna_person[subsequence]) == subsequence_counts[subsequence]:
                match += 1
        # If the match ammount is the same to the length of all the subsequences, print the person.
        if match == len(subsequence_counts):
            print(dna_person['name'])
            break
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()

