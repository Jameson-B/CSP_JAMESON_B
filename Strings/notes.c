// Jameson Bultez, Strings Notes C

#include <stdio.h>
#include <string.h>

char subject[50];
char name[] = "Victoria";
char sentence[] = "The quick brown fox jumps over the lazy dog.";


int main(void){
     
    // printf("What class are you in? \n");
    // scanf("%s", subject);
    // fgets(subject, sizeof(subject), stdin);
    // printf("You are in %s. That is a cool class. \n", subject);

    // name[0] = 'T';
    // name[1] = 'o';
    // name[2] = 'r';
    // name[3] = 'i';
    // name[4] = ' ';
    // printf("%s", name);

    
    // printf("%lu \n", sizeof(sentence)); // starts counting at 0
    // printf("%d \n", strlen(sentence)); // starts counting at 1

    char one[] = "Hello ";
    char two[] = "World!";
    char three[] = "Welcome to my program. ";
    //printf("%s \n", one);

    //strcat(one, two); // only concatenate two strings at a time.
    //printf("%s \n", one);

    //strcat(three, one); // first parameter in parantheses is set to new variable.
    //printf("%s \n", three);
    char mario[] = "hello ";
    char luigi[] = "world";

    strcat(mario, luigi);
    printf("%s", mario);
    
   

    return 0;
}