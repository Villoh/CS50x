// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Get the hash value
    unsigned int index = hash(word);

    // Traverse the linked list at the hashed index
    node *cursor = table[index];
    while (cursor != NULL)
    {
        // Compare the word with the current node's word
        if (strcasecmp(cursor->word, word) == 0)
        {
            // Word found
            return true;
        }
        cursor = cursor->next;
    }

    // Word not found
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Simple hash function: use the first character of the word as the index
    // Convert the character to uppercase and subtract 'A' to get the index in the range [0, N-1]
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Clear the hash table
    for (unsigned int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }

    // Buffer for reading words from the dictionary
    char word[LENGTH + 1];

    // Read words from dictionary and add them to the hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // Create a new node for the word
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(file);
            return false;
        }

        // Copy the word into the new node
        strcpy(new_node->word, word);

        // Get the hash value
        unsigned int index = hash(word);

        // Insert the new node at the beginning of the linked list
        new_node->next = table[index];
        table[index] = new_node;
    }

    // Close dictionary file
    fclose(file);

    // Dictionary loaded successfully
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int word_count = 0;

    // Traverse the hash table and count the number of nodes
    for (unsigned int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            word_count++;
            cursor = cursor->next;
        }
    }

    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Traverse the hash table and free the nodes
    for (unsigned int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }

    // Dictionary unloaded successfully
    return true;
}
