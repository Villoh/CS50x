#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    //Check there is only one argument, the forensic image
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    //Open the file given as argument
    FILE *infile = fopen(argv[1], "r");

    //Check if the file could be opened.
    if (infile == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }

    //Declare a buffer to store all the image data. 512 is the given size.
    BYTE buffer[512];
    //How many images the forensic image has.
    int jpeg = 0;
    //Declare an outpute file to write every jpg located in the forensic image.
    FILE *outfile = NULL;
    //Declare a char to order all the jpg as 000, 001...
    char filename[8] = {0};

    //Loop every possible jpg the foresinc image has
    while (fread(buffer, sizeof(BYTE) * 512, 1, infile) == 1)
    {
        //Check if the first 4 bytes matches the jpg header.
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //Check if the output file is not null, to close and create a new one.
            if (outfile != NULL)
            {
                fclose(outfile);
            }

            //Give a filename following the pattern.
            sprintf(filename, "%03d.jpg", jpeg);
            //Create an output file (.jpg)
            outfile = fopen(filename, "w");
            //Increment the image counter.
            jpeg++;
        }
        //If the file is not null write all the data in the buffer.
        if (outfile != NULL)
        {
            fwrite(buffer, sizeof(BYTE) * 512, 1, outfile);
        }
    }

    // Close files
    if (outfile != NULL)
    {
        fclose(outfile);
    }

    fclose(infile);

    return 0;
}