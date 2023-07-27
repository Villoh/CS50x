#include <cs50.h>
#include <stdio.h>

//Declaration of the height and the function to check if the number is between 1 and 8.
int check_height(string prompt);
int height = 0;

int main(void)
{
    //Ask the user to introduce a value for the height.
    height = check_height("Height: ");

    //Declaration and assigment of the letter we gonna use for the pyramid.
    char hashtag = '#';

    //Loop for the lines
    for (int rows = 0; rows < height; rows++)
    {
        //Loop for the spaces in each row at the start.
        for (int spaces = height - rows; spaces > 1; spaces--)
        {
            printf(" ");
        }
        //Loop for the left part of the pyramid.
        for (int left_rows = 0; left_rows <= rows; left_rows++)
        {
            printf("%c", hashtag);
        }
        //Spaces in between
        printf("  ");

        //Loop for the right part of the pyramid.
        for (int right_rows = 0; right_rows <= rows; right_rows++)
        {
            printf("%c", hashtag);
        }
        //New Line
        printf("\n");
    }

}

int check_height(string prompt)
{
    do
    {
        height = get_int("%s", prompt);
    }
    while (height < 1 || height > 8);

    return height;
}