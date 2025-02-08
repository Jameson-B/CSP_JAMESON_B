// Jameson Bultez, Financial Calculator C

# include <stdio.h>

float income;
float rent;
float utilities;
float groceries;
float transport;
float savings;
float spending;
float percentRent;
float percentUtilities;
float percentGroceries;
float percentTransport;
float percentSpending;

int main(void) {
     
     // printf statement that welcomes my user and tells them what my program does.
     printf("Welcome to the monthly financial calculator, Bedrock Edition.");

     // ask user what their income is (variable that is an input).
     printf("What is your monthly income?:");
     scanf("%f", &income);

     // ask user what their rent/mortgage is (variable that is an input).
     printf("What is your monthly rent/mortage payment?:");
     scanf("%f", &rent);

     // ask user what their utilities cost (variable that is an input).
     printf("How much do your utilities cost per month?:");
     scanf("%f", &utilities);

     // ask user what their grocereris cost (variable that is an input).
     printf("How much do your groceries cost per month?:");
     scanf("%f", &groceries);

     // ask user what their transportation costs (variable that is an input).
     printf("How much does your gas/bus fare cost per month?:");
     scanf("%f", &transport);

     // calculate savings as 10% of income (income * .1). (variable that is a float).
     savings = income*.1;

     // calculate spending as income - savings - rent/mortgage - utilities - groceries - transportation (variable that is a float)

     // caclulate percent income of rent/mortgage (rent / income * 100) (variable)

     // caclulate percent income of utilities (utilities / income * 100) (variable)

     // caclulate percent income of groceries (groceries / income * 100) (variable)

     // caclulate percent income of transportation (transportation / income * 100) (variable)

     // calculate percent income of savings (percentsavings / income * 100) (variable)

     // calculte percent income of spending (spending / income * 100) (variable)

     // white space printf statement

     // Your rent is $XX.XX, which is XX% of your income (printf statement).

     // Your utilities is $XX.XX, which is XX% of your income (printf statement).

     // Your groceries is $XX.XX, which is XX% of your income (printf statement).

     // Your transportation is $XX.XX, which is XX% of your income (printf statement).

     // Your savings is $XX.XX, which is XX% of your income (printf statement).

     // Your spending is $XX.XX, which is XX% of your income (printf statement).

     // printf statement that thanks the user and ends the conversation.


     return 0;
}