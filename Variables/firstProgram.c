// Jameson Bultez, First Program C

# include <stdio.h>

char name[15];

int main(void) {
    printf("What is your name?:");
    scanf("%s", name);
    printf("Hello, %s. I've been expecting you. \n", name);

    return 0;
}
