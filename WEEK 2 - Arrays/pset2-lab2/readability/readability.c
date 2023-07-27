#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
void get_grade(int letters, int words, int sentences);

int main(void)
{
    //Ask the user to type a text
    string text = get_string("Text: ");
    //Calls the get_grade function.
    get_grade(count_letters(text), count_words(text), count_sentences(text));
}

//Function to get the number of letters.
int count_letters(string text)
{
    int letters = 0;
    //Loop every character of the text.
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        //When a letter is found (A-Z/a-z or 65-90/97-122 in ASCII decimal) it sums 1 to the variable letters.
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
        {
            letters++;
        }
    }

    return letters;
}

//Function to get the number of words.
int count_words(string text)
{
    int words = 1;
    //Loop every character of the text.
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        //When a space is found it sums 1 to the variable words.
        if (text[i] == ' ')
        {
            words++;
        }
    }

    return words;
}

//Function to get the number of sentences.
int count_sentences(string text)
{
    int sentences = 0;
    //Loop every character of the text.
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        //When a dot, exclamation or interrogation is found it sums 1 to the variable sentences.
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }

    return sentences;
}

//Function to get the grade of a text.
void get_grade(int letters, int words, int sentences)
{
    //Coleman-Liau formula
    int index = round(0.0588 * letters / words * 100 - 0.296 * sentences / words * 100 - 15.8);
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}