// Jameson Bultez, Old Enough C

#include <stdio.h>

// Declare age variable.
int age;

int main(void){
    
    // Welcome user and tell them what the program does.
    printf("\nWelcome to Old Enough: Bedrock Edition.\nThis program will tell you what you can do at your current age.\n");

    // Set age varible to user input.
    printf("\nWhat is your current age in years?\n");
    scanf("%d", &age);

    // Tell user what they can do at their current age.
    if (age > 110) {
        printf("\nYou are probably old enough to watch over your descendants from heaven. Congrats!");
    } else if (age >= 18) {
        printf("\nYou are old enough to vote.");
    } else if (age >= 16) {
        printf("\nYou are old enough to have a driver's license.");
    } else if (age >= 14) {
        printf("\nYou are old enough to have a learner's permit.");
    } else if (age >= 5) {
        printf("\nYou are old enough to go to school.");
    } else if (0 <= age < 5) {
        printf("\nYou are old enough to do eat, sleep, and cry.");
    } else {
        printf("\nYou are old enough to prepare for your life in abs(%d) years.", age);
    }

    // Conclude.
    printf("\nThat's what you're old enough to do!\nThanks for using Old Enough: Bedrock Edition.\n");

    return 0;
}