#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float aux = 0;
    for (int i = 0; i < height; i++)
    {
        for (int k = 0; k < width; k++)
        {

            aux = ((float)(image[i][k].rgbtBlue + image[i][k].rgbtGreen + image[i][k].rgbtRed) / 3);

            aux = round(aux);
            image[i][k].rgbtBlue = aux;
            image[i][k].rgbtGreen = aux;
            image[i][k].rgbtRed = aux;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int aux[3];
    int hAux = 0;
    while (hAux < height)
    {
        for (int rows = 0, rows2 = width - 1; rows < round(width / 2); rows++, rows2--)
        {
            aux[0] = image[hAux][rows].rgbtBlue;
            aux[1] = image[hAux][rows].rgbtGreen;
            aux[2] = image[hAux][rows].rgbtRed;

            image[hAux][rows].rgbtBlue = image[hAux][rows2].rgbtBlue;
            image[hAux][rows].rgbtGreen = image[hAux][rows2].rgbtGreen;
            image[hAux][rows].rgbtRed = image[hAux][rows2].rgbtRed;

            image[hAux][rows2].rgbtBlue = aux[0];
            image[hAux][rows2].rgbtGreen = aux[1];
            image[hAux][rows2].rgbtRed = aux[2];
        }
        hAux++;
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE aux[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int k = 0; k < width; k++)
        {
            float sumBlue = 0;
            float sumGreen = 0;
            float sumRed = 0;
            // How many pixels is this one touching
            float counter = 0;

            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    // Check edges and corners
                    if (i + r < 0 || i + r > height - 1)
                    {
                        continue;
                    }

                    if (k + c < 0 || k + c > width - 1)
                    {
                        continue;
                    }

                    // Sum the bits of each color in each pixel
                    sumBlue += image[i + r][k + c].rgbtBlue;
                    sumGreen += image[i + r][k + c].rgbtGreen;
                    sumRed += image[i + r][k + c].rgbtRed;
                    counter++;
                }
            }

            aux[i][k].rgbtBlue = round(sumBlue / counter);
            aux[i][k].rgbtGreen = round(sumGreen / counter);
            aux[i][k].rgbtRed = round(sumRed / counter);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = aux[i][j].rgbtBlue;
            image[i][j].rgbtGreen = aux[i][j].rgbtGreen;
            image[i][j].rgbtRed = aux[i][j].rgbtRed;
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE aux[height][width];

    //Gx and Gy matrix.
    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int k = 0; k < width; k++)
        {
            int gxBlue = 0;
            int gxGreen = 0;
            int gxRed = 0;
            int gyBlue = 0;
            int gyGreen = 0;
            int gyRed = 0;

            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    // Check edges and corners
                    if (i + r < 0 || i + r > height - 1)
                    {
                        continue;
                    }

                    if (k + c < 0 || k + c > width - 1)
                    {
                        continue;
                    }

                    //Sum each color in this pixel multiplied by the Gx and the Gy matrix.
                    gxBlue += image[i + r][k + c].rgbtBlue * gx[r + 1][c + 1];
                    gyBlue += image[i + r][k + c].rgbtBlue * gy[r + 1][c + 1];
                    gxGreen += image[i + r][k + c].rgbtGreen * gx[r + 1][c + 1];
                    gyGreen += image[i + r][k + c].rgbtGreen * gy[r + 1][c + 1];
                    gxRed += image[i + r][k + c].rgbtRed * gx[r + 1][c + 1];
                    gyRed += image[i + r][k + c].rgbtRed * gy[r + 1][c + 1];
                }
            }

            //Compute each new channel value
            int blue = round(sqrt(gxBlue * gxBlue + gyBlue * gyBlue));
            int green = round(sqrt(gxGreen * gxGreen + gyGreen * gyGreen));
            int red = round(sqrt(gxRed * gxRed + gyRed * gyRed));

            //if color is greater than 255 return 255 else return the color value
            aux[i][k].rgbtBlue = (blue > 255) ? 255 : blue;
            aux[i][k].rgbtGreen = (green > 255) ? 255 : green;
            aux[i][k].rgbtRed = (red > 255) ? 255 : red;
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = aux[i][j].rgbtBlue;
            image[i][j].rgbtGreen = aux[i][j].rgbtGreen;
            image[i][j].rgbtRed = aux[i][j].rgbtRed;
        }
    }
}
