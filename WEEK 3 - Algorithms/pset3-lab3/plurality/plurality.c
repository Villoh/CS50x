#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    //Loops every candidate
    for (int i = 0; i < candidate_count; i++)
    {
        //Check if the name prompt is the same as the candidate name
        if (strcasecmp(candidates[i].name, name) == 0)
        {
            //Sums a vote
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // Declaration of the votes aucxiliar to get the most voted and the number of winners
    int votes_aux = 0;
    int n_winners = 1;

    // 1st loop to get the winners array size
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > votes_aux)
        {
            votes_aux = candidates[i].votes;
        }
        else if (candidates[i].votes == votes_aux)
        {
            n_winners++;
        }
    }

    // Declaration of the winners array
    string winners[n_winners];
    n_winners = 0;
    votes_aux = 0;
    // Loop to assign the winners to the array
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > votes_aux)
        {
            votes_aux = candidates[i].votes;
            winners[n_winners] = candidates[i].name;
        }
        else if (candidates[i].votes == votes_aux)
        {
            n_winners++;
            winners[n_winners] = candidates[i].name;
        }
    }
    // Loop to print winners
    for (int i = 0; i <= n_winners; i++)
    {
        printf("%s\n", winners[i]);
    }
}