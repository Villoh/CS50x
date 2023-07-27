#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string get_cipher_text(string key, string plain_text, char cipher_text[]);

int main(int argc, string argv[])
{
    // Check if there is more tha 2 arguments or only one, if yes then print the instructions.
    if (argc > 2 || argc == 1)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    // Check if the argument length is more or less than 26, if yes then print that the key must contain 26 chars.
    else if (strlen(argv[1]) < 26 || strlen(argv[1]) > 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    string key = argv[1];
    // Loop every character of the key
    for (int i = 0, len = strlen(key); i < len; i++)
    {
        // Check if the char is not alphabetical.
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
        // Another loop for every character of the key, to check if there are duplicated characters.
        for (int n = 0; n < len; n++)
        {
            // Skip the same letters
            if (n != i)
            {
                // Check if letter i is equal to letter n.
                if (key[i] == key[n])
                {
                    printf("Key must not contain repeated characters.\n");
                    return 1;
                }
            }
        }
    }

    // Ask the user to type a plain text.
    string plain_text = get_string("plaintext: ");
    // Declare the array where the encrypted text is going to be stored in the function.
    char cipher_text[(strlen(plain_text)) + 1];
    // Declare and assign the string the encrypted text calling to the function get_cipher_text.
    string cipher_text_str = get_cipher_text(key, plain_text, cipher_text);
    // Print the encrypted text in the terminal.
    printf("ciphertext: %s\n", cipher_text_str);
}

// Function get_cipher_text that returns the text encrypted with the key given as parameter.
string get_cipher_text(string key, string plain_text, char cipher_text[])
{
    // Loop every character of the plain_text
    for (int i = 0, len = strlen(plain_text); i < len; i++)
    {
        // Check if it is upper case
        if (isupper(plain_text[i]))
        {
            // Assign the corresponding value to the i position of the array (For example B-A = 1 or 42-41=1, we will get the position of the corresponding value in the key)
            cipher_text[i] = toupper(key[plain_text[i] - 'A']);
        }
        // Check if it is lower case
        else if (islower(plain_text[i]))
        {
            // Assign the corresponding value to the i position of the array (For example b-a = 1 or 62-61=1, we will get the position of the corresponding value in the key)
            cipher_text[i] = tolower(key[plain_text[i] - 'a']);
        }
        // If it is not an alphabetic character then keep the same value
        else
        {
            cipher_text[i] = plain_text[i];
        }
    }
    // End of the array
    cipher_text[strlen(plain_text)] = '\0';
    // Convert the char array to a string
    string cipher_text_str = (string)cipher_text;
    return cipher_text_str;
}