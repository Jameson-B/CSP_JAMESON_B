// Jameson Bultez, Loops Notes C

#include <stdio.h>



int main(void){

     //1. What is a loop?
          // a section of code that repeats.
     //2. What are the two types of loops?
          // While Loops
          int start = 0;
          while(start < 5) {
               printf("Hello World!\n");
               start++;
          }
          // For Loops
          int q;
          for(q = 0; q < 5; q++) {
               printf("%d\n", q);
          }

     //3. What is iteration?
          // Iteration is the number of times you're running the loop.
          // An iteration is one instance of a loop
     //4. What are arrays(lists)?
          // An array is a variable that stores mulitple values.
     //8. How do you make arrays(lists) in C?
          // In C, all items in an array must be of the same data type.
          // In C, a string is just an array of characters.
               // a) set the data type.
               // b) place brackets [] after the name indicating how long the array is.
               // c) list must be surrouned by braces {}.
               // d) commas , must separate each item.
          int grades[] = {88, 97, 100, 70, 72, 99, 61};
          // each item is worth 4 bytes.
          
          // change an item in the array.
          grades[2] = 101;

          // print a single item from a list.
          printf("CSP Period 3 Grade: %d%%\n", grades[2]);

          // get the length of a list
          int length = sizeof(grades)/sizeof(grades[0]);
          // sizeof(grades) = 28; sizeof(grades[0]) = 4.
          // int length = 28 / 4 
          // gets the storage of the list in bytes. 
          // in this case, with 7 items in the list, and each one the size of a nibble (4 bits), sizeof returns 28, because 7*4 = 28.
          printf("%d\n", length);

          // array of strings.
          // a list of lists.
          char movies[][20] = {"Cars\n", "Treasure Planet\n", "An American Tail\n", "West Side Story\n"};
          printf("%s\n", movies[1]);

          int mlength = sizeof(movies)/sizeof(movies[0]);

     //9. How do you make for loops in C?
          // iterator: a variable keeps track of times you've gone through the loop.
               // works best as x or i.
          // set the iterator
          int x;
          // for(where to start, where to end, what to count by) {}
          for(x=0; x<=10; x+=2) {
               printf("%d\n", x);
          }

          int m;
          for(m=0; m<mlength; m++) {
               printf("%s", movies[m]);
          } 
     //10. How do you make while loops in C?
     
     return 0;
}