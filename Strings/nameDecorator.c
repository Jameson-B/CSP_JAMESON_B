// Jameson Bultez, Name Decorator C

#include <stdio.h>
#include <string.h>

// Declare variable "name".

char name[50];

// Declare all string decorator variables.

char arrowsLeft[50] = "<<< ";
char arrowsRight[50] = " >>>";

char paranthesesLeft[50] = "((( ";
char paranthesesRight[50] = " )))";

char dashesLeft[50] = " --- ";
char dashesRight[50] = " --- ";

char smilesLeft[50] = " :) :) ";
char smilesRight[50] = " :) :) ";

char hashesLeft[50] = " ### ";
char hashesRight[50] = " ### ";

char plussesLeft[50] = " +++ ";
char plussesRight[50] = " +++ ";

char tildesLeft[50] = " ~~~ ";
char tildesRight[50] = " ~~~ ";

char equalsLeft[50] = " === ";
char equalsRight[50] = " === ";

int main(void) {
     
    // Welcome user and tell them what the program does.

    printf("Welcome! This is the Name Decorator: Python Edition, by Jameson Bultez. \nThis program will print your first name with various embelishments. \n\n");

    // Set variable "name" to a user input.

    printf("What is your first name? \n");
    scanf("%s", name);
    // fgets(name, sizeof(name), stdin);

    // Concatenate name with string decorators.

    strcat(arrowsLeft, name);
    strcat(arrowsLeft, arrowsRight);

    strcat(paranthesesLeft, name);
    strcat(paranthesesLeft, paranthesesRight);

    strcat(dashesLeft, name);
    strcat(dashesLeft, dashesRight);

    strcat(smilesLeft, name);
    strcat(smilesLeft, smilesRight);

    strcat(hashesLeft, name);
    strcat(hashesLeft, hashesRight);

    strcat(plussesLeft, name);
    strcat(plussesLeft, plussesRight);

    strcat(tildesLeft, name);
    strcat(tildesLeft, tildesRight);

    strcat(equalsLeft, name);
    strcat(equalsLeft, equalsRight);

    // Print new strings.

    printf("%s \n", arrowsLeft);

    printf("%s \n", paranthesesLeft);

    printf("%s \n", dashesLeft);

    printf("%s \n", smilesLeft);

    printf("%s \n", hashesLeft);

    printf("%s \n", plussesLeft);

    printf("%s \n", tildesLeft);

    printf("%s \n\n", equalsLeft);

    // Conclude the program.

    printf("What do you think? \nThank you for using the Name Decorator: Python Edition, by Jameson Bultez. \nHave a nice day! \n\n");

    return 0;
}