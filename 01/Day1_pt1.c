#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*

Advent of code 2021
Day 1 pt 1

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

	// Counter for each number that is higher than the last
	int counter = 0;

	// Each previous number stored here
	int prev_number;

	// Each current number will be stored here
	int number;

	// Each line of text will be stored here
	char *line;
	line = malloc(1000);

	char new_char;

	while ((new_char = fgetc(input)) != EOF)
	{

		// Concatenate string until new line character

		if (new_char == '\n')
		{

			prev_number = number;

			number = atoi(line);

			char_in_line = 0;

			// Compare if this isn't the first line
			if (total_count > 0)
			{

				if (number > prev_number)
					{
						++counter;
					
					}

			}

			// Advance counter for lines
			++total_count;

		} else
		{

			// Adding character to line

			line[char_in_line] = new_char;

			++char_in_line;

		}

	}

	printf("The number of times current number was greater than previous number is %i\n", counter);

	fclose(input);

	return 0;

}

