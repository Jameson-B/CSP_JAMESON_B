// Jameson Bultez, How to Get the Time of Day

#include <stdio.h>
#include <time.h>

int main(void){
    time_t seconds; // Time in seconds since 1/1/1970 @ 0:00
    // printf("Seconds since Jan. 1, 1970 @ 0:00 = %d\n", seconds);

    // Current time
    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    // printf("Current time and date is %s\n", asctime(timeinfo));

    // Current hour
    time_t now = time(NULL);

    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour; // 24-hour time (0:00-23:59)
    printf("%d\n", hour);

    if (0 <= hour < 12) {
        printf("Good mornin'! Good mornin'! It's nice to stay up late.");
    }

    return 0;
}