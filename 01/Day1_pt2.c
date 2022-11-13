#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*

Advent of code 2021
Day 1 pt 2

Compare 3rd number of second "window" to 1st number of first "window".

*/


int main(void)
{

	FILE *input;

	input = fopen("./input.txt", "r");

	if (input == NULL)
	{
		printf("Unable to open file\n");

		return 1;
	}

	// Keep track of total numbers
	int total_count = 0;

	// count chars in line
	int char_in_line = 0;

	// Array of four integers
	// This will contain the three numbers from window 1, and 
	// The one new number from window 2.
	int num_array[4];

	// Counter for each number that is higher than the last
	int counter = 0;

	// Each current number will be stored here
	int number;

	// Each line of text will be stored here
	char *line;
	line = malloc(1000);

	char new_char;

	while ((new_char = fgetc(input)) != EOF)
	{

		// Concatenate string until new line character

		if (new_char != '\n')
		{

			// Adding character to line

			line[char_in_line] = new_char;

			++char_in_line;

		} else if (new_char == '\n')
		{

			number = atoi(line);

			char_in_line = 0;

			// Add to array
			if (total_count < 4)
			{

				num_array[total_count] = number;

			} else
			{

				// Move numbers down array, 
				// and add new number to the end

				num_array[0] = num_array[1];
				num_array[1] = num_array[2];
				num_array[2] = num_array[3];
				num_array[3] = number;

			}

			// Compare if there is enough for two windows
			if (total_count > 2)
			{

				if (num_array[3] > num_array[0])
					{

						++counter;
					
					}

			}

			// Advance counter for lines
			++total_count;

		} 

	}

	printf("The number of times current window sum was greater than previous window sum %i\n", counter);

	fclose(input);

	return 0;

}