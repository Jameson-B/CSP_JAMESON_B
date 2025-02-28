// Jameson Bultez, How to Get the Time of Day

#include <stdio.h>
#include <time.h>

int main(void){
    time_t seconds; // Time in seconds since 1/1/1970 @ 0:00

    // Current time
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);

    // Current hour
    time_t now = time(NULL);

    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour; // 24-hour time (0:00-23:59)
    
    // Print greeting based on time of day.
    if (hour == 12) {
        printf("Good noon!");
    } else if (0 <= hour < 12) {
        printf("Good morning.");
    } else if (12 <= hour < 17) {
        printf("Good afternoon.");
    } else if (17 <= hour < 21) {
        printf("Good evening.");
    } else {
        printf("Good night.");
    }
        
    return 0;
}