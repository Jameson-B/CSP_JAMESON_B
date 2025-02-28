// Jameson Bultez, Expressions Notes C

#include <stdio.h>
#include <math.h>

//float x = pow(2, 2);
//float equation = 5+7+11/(5-x);

//int expression = 5*pow(7, 2)/4;
char name[50] = "LaRose";
int num = 12;
float pi = 3.1415926535;
int extra = 11 % 2;
float koalas = 23.6;

// Arithmatic operators are the same in C as in Python, except for the exponenents operator, which is "pow".

int main(void){
     //name[50] = "Vienna";
     //num = 4;
     //printf("%d\n", num);
     // printf("%.10f\n", pi);
     // printf("%f", equation);
     // printf("%f", expression);
     // printf((int)6+9/2);

     printf("%d\n", extra);

     floor(koalas);

     printf("%f\n", koalas);

     return 0;
}
