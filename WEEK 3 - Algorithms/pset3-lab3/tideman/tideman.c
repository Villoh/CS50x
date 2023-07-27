#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool check_cycle(int start, int end);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
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
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);
        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO
    //Loop every candidate
    for (int i = 0; i < candidate_count; i++)
    {
        //If the candidate name is the same as the name given as an argument the vote is valid.
        if (strcasecmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO
    //Loop to fill the preferences array with the ranks array
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = 0; j < candidate_count - i; j++)
        {
            //Check that ranks[i] it's not the same as ranks[i + j]
            if (i + j != i)
            {
                preferences[ranks[i]][ranks[i + j]]++;
            }
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO
    //Loop preferences array.
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            //Check that it's not the same position in rows and columns
            if (j != i)
            {
                //If [i][j] is bigger than the opposite, we have a winner and a loser.
                if (preferences[i][j] > preferences[j][i])
                {
                    pair_count++;
                    pairs[pair_count - 1].winner = i;
                    pairs[pair_count - 1].loser = j;
                }
            }
        }
    }
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    //Buble sort algorithm, if the i position is bigger than j, change their values
    int aux_win = 0;
    int aux_los = 0;
    for (int i = 0; i < pair_count - 1; i++)
    {
        for (int j = i + 1; j < pair_count; j++)
        {
            //Check that it's not the same position in rows and columns
            if (i != j)
            {
                if ((preferences[pairs[i].winner][pairs[i].loser] - preferences[pairs[i].loser][pairs[i].winner]) <
                    (preferences[pairs[j].winner][pairs[j].loser] - preferences[pairs[j].loser][pairs[j].winner]))
                {
                    aux_win = pairs[i].winner;
                    aux_los = pairs[i].loser;
                    pairs[i].winner = pairs[j].winner;
                    pairs[i].loser = pairs[j].loser;
                    pairs[j].winner = aux_win;
                    pairs[j].loser = aux_los;
                }
            }
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    // TODO
    for (int i = 0; i < pair_count; i++)
    {
        int winner = pairs[i].winner;
        int loser = pairs[i].loser;
        if (!check_cycle(winner, loser))
        {
            locked[winner][loser] = true;
        }
    }
    return;
}

bool check_cycle(int winner, int loser)
{

    if (locked[loser][winner])
    {
        return true;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        if (locked[loser][i] && check_cycle(winner, i))
        {
            return true;
        }
    }
    return false;
}

// Print the winner of the election
void print_winner(void)
{
    //Boolean to know when there's a winner
    bool is_winner;
    //Loop locked array, rows and columns
    for (int row = 0; row < candidate_count; row++)
    {
        for (int col = 0; col < candidate_count; col++)
        {
            //Check if the position is false or true, because we know there's a winner when he doesn't have any arrows pointing at him, in other terms when all the columns are false.
            if (locked[col][row])
            {
                is_winner = false;
                break;
            }
            else
            {
                is_winner = true;
            }
        }
        //If there's a winner print his name
        if (is_winner)
        {
            printf("%s\n", candidates[row]);
            break;
        }
    }
    return;
}