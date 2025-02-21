// Jameson Bultez, Hello World Update C

#include <stdio.h>

// Declare variable that will be defined as the user's first name.
char user_name[50];

// Function to print "Hello, (name)."
void helloWorld(char name[50]) {
    printf("Hello, %s.\n", name);
}

int main(void) {

    // Get user's first name and store it in user_name.
    printf("Type your first name: ");
    scanf("%s", user_name);

    // Print hello to user and various other names.
    helloWorld(user_name);
    helloWorld("Marcus");
    helloWorld("Mia");
    helloWorld("Miles");
    helloWorld("Maria");

    return 0;
}