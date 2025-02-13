// Jameson Bultez, Silly Sentences C

#include <stdio.h>

// Declare word variables.

char noun[50];
char verb[50];
char adjective[50];
char adverb[50];

int main(void){

    // Print introduction.

    printf("Welcome to Silly Sentences: C Edition. \nEnter the words the computer asks for and it will write a story with them. \n");

    // Set word variables to user inputs.

    printf("Enter one NOUN below. \n");
    scanf("%s", noun);

    printf("Enter one VERB below. \n");
    scanf("%s", verb);

    printf("Enter one ADJECTIVE below. \n");
    scanf("%s", adjective);

    printf("Enter one ADVERB below. \n");
    scanf("%s", adverb);

    // Print story with user inputs.

    printf("Once upon a time there was a %s who loved to %s. Everyone thought they were %s, because they did it %s. The end. \n", noun, verb, adjective, adverb);

    // Print conclusion.

    printf("Thank you for playing Silly Sentences: C Edition. \nMay your days be long and your sentences be silly! \n");
     
    return 0;
}
