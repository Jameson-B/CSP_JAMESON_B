// Jameson Bultez, Fizz Buzz C

#include <stdio.h>

int main(void){
    // Print integers from 1 to 50 and replace multiples of 3 with "Fizz", mulitples of 5 with "Buzz", and multiplies of 3 and 5 with "FizzBuzz". 
        // Set "x", the iterator, to 1.
    int x = 1;
    for(x=1; x<=50; x++) {
        if (x % 3 == 0 && x % 5 == 0) {
            printf("FizzBuzz\n");
        } else if (x % 3 == 0) {
            printf("Fizz\n");
        } else if (x % 5 == 0) {
            printf("Buzz\n");
        } else {
            printf("%d\n", x);
        }
    }

    return 0;
}