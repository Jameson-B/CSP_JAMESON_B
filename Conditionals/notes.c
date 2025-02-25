// Jameson Bultez, Conditionals Notes C

#include <stdio.h>
#include <string.h> // Needed to compare stings

char name[] = "Vienna";
int num;

int main(void){
    //10. How do you write an if statement in C?
    if (strcmp(name, "Vienna") == 0) { // strcmp means "string comparison". When the output is 0, the strings are the same."
        printf("Hello, Vienna!\n");
    //11. How do you write else statements in C?
    } else {
        printf("Hello %s. Welcome to class.\n", name);
    }

    printf("How many sibs you got bruh?:\n");
    scanf("%d", &num);

    //12. How do you write elif/ else if statements in C?
    if (num == 0) {
        printf("You are an only child.\n");
    } else if (num == 1) {
        printf("You have one built-in friend. Congrats.\n");
    } else if (num == 2) {
        printf("You have a couple of siblings.\n");
    } else if (num <= 5) {
        printf("You have a few siblings.\n");
    } else {
        printf("You have a plethera of siblings.\n");
    }

    //13. How do you write the 3 logical operators in C?
        // && and
        // || or
        // ! not
        if (num == 7 || num == 13) { // Example of || or
            printf("%d is an unlucky number.\n", num);
        } else if (num < 10 && num > 5) { // Example of && and
            printf("%d is a large, sinlge-digit number.\n", num);
        } else if (!num < 10) { // Example of ! not
            if (num == 12) { // Example of a nested conditional.
                printf("That's a dozen!\n");
            } else {
                printf("%d is a big number.\n");
            }  
        } else {
            printf("You entered %d.", num);
        }
     
    return 0;
}