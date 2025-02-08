// Jameson Bultez, Financial Calculator C

# include <stdio.h>
# include <math.h>

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
     printf("Welcome to the Monthly Financial Calculator (MFC), Bedrock Edition. \nThis program will ask you for your monthly income and expeneses, then calculate what percent each expense takes of your income, as well as how much money you have left over to spend. Enjoy! \n\n");

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
     savings = income * .1;

     // calculate spending as income - savings - rent/mortgage - utilities - groceries - transportation (variable that is a float)
     spending = income - savings - rent - utilities -  groceries- transport;

     // caclulate percent income of rent/mortgage (rent / income * 100) (variable)
     percentRent = rent / income * 100;

     // caclulate percent income of utilities (utilities / income * 100) (variable)
     percentUtilities = utilities / income * 100;

     // caclulate percent income of groceries (groceries / income * 100) (variable)
     percentGroceries = groceries / income * 100;

     // caclulate percent income of transportation (transportation / income * 100) (variable)
     percentTransport = transport / income * 100;

     // calculte percent income of spending (spending / income * 100) (variable)
     percentSpending = spending / income * 100;

     // announces report
     printf("\nHere is your report: \n\n");

     // Your rent is $XX.XX, which is XX% of your income (printf statement).
     printf("Your rent is $%.2f, which is %.1f%% of your income. \n\n", rent, percentRent);

     // Your utilities is $XX.XX, which is XX% of your income (printf statement).
     printf("Your utilities cost $%.2f, which is %.1f%% of your income. \n\n", utilities, percentUtilities);

     // Your groceries is $XX.XX, which is XX% of your income (printf statement).
     printf("Your groceries cost $%.2f, which is %.1f%% of your income. \n\n", groceries, percentGroceries);

     // Your transportation is $XX.XX, which is XX% of your income (printf statement).
     printf("Your gas/bus fare costs $%.2f, which is %.1f%% of your income. \n\n", transport, percentTransport);

     // Your savings is $XX.XX, which is XX% of your income (printf statement).
     printf("Your savings are $%.2f, which is 10.0%% of your income. \n\n", savings);

     // Your spending is $XX.XX, which is XX% of your income (printf statement).
     printf("You have $%.2f left over to spend, which is %.1f%% of your income. \n\n", spending, percentSpending);

     // printf statement that thanks the user and ends the conversation.
     printf("Thank you for using the Monthly Financial Calculator (MFC), Bedrock Edition. Spend wisely! \n\n");

     return 0;
}