// Jameson Bultez, Functions Notes C

#include <stdio.h>

// The return you get is the same data type as the one you set when you defined the function.

// In C, everyhting within the curly brackets {} is included in the function.

// You can't write a function in a function.

// * means "all".

//int num;
//char name[50], place[50], verb[50];

/*
int add(int numOne, int numTwo) {
    return numOne+numTwo;
}
*/
/*
const char* word(type) {
    char choice[50];
    print("Please give me a %s:\n", type);
    scanf("%s", choice);
    return choice; 
}
*/

void due(char assignment[50], char day[20]) {
    printf("The %s assignment is due on %s. \n", assignment, day);
}

int main(void) {
    //printf("Please tell me a number:\n");
    //scanf("%d", num);
    // printf(int(add(num,10)));
    /*
    add(3,9);
    add(72,1);
    */
    due("Hello World", "Tuesday");

    return 0;
}