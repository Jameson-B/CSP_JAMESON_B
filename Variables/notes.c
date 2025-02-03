// Jameson Bultez, Variables Notes C

char name[20];

int age;

float pi;

int main(void){
    printf("What is your name?: \n");
    scanf("%s,", name);
    printf("How old are you?: \n");
    scanf("%d", &age);
    printf("Write out as much pi as you know?: ");
    scanf("%f", &pi);