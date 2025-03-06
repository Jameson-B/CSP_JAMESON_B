// Jameson Bultez, Family Loop C

#include <stdio.h>

int main(void) {

    // Define string list containing all of my parents' kids.
    char kids[][10] = {"Linnae", "William", "Ethan", "Grace", "Jameson", "Weston"};

    // Define "klength" as length of the list "kids".
    int klength = sizeof(kids)/sizeof(kids[0]);

    // Print a hello message to each item in list "kids".
        // Declare "i" as the iterator.
    int i;
    for (i=0; i<klength; i++) {
        printf("Hello, %s!\n", kids[i]);
    }
     
     return 0;
}