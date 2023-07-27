#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //Call to the get_string function that returns a string, in this case the name, and assign this return to the string "name".
    string name = get_string("What's your name? ");
    //prints "hello, 'your name'" in console.
    printf("hello, %s\n", name);
}