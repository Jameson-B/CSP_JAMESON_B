#include <stdio.h>
#include <math.h>

int main() {
    double num = 4.3;
    double roundedNum = round(num);
    printf("Rounded value of %.1f is %.1f\n", num, roundedNum); // Output: 4.0
    return 0;
}
