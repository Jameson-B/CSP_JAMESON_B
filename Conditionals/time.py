# Jameson Bultez, How to Get the Time of the Day

import time

# First instance of time in programming
first_time = time.gmtime # Greenwhich Mean Time
# print(first_time)

# Current time in seconds
current = time.time()
# print(time) # seconds sinec January 1, 1970, 0:00

# Current date and time like we noramlly see it
now = time.ctime(current)
# print(now)

# Get just a part of the time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour # 24-hour time (0:00-23:59)

# Print greeting based on time of day.
if hour == 12:
    print("Good noon!")
elif 0 <= hour < 12:
    print("Good mornin'! Good mornin'! It's nice to stay up late.")
elif 12 <= hour < 5:
    print("'Afternoon!")
elif 5<= hour < 9:
    print("What a lovely evening.")
else:
    print("Rock-a-bye, coder, in their bedroom. When the code runs, the compiler will stop. When the code breaks, the coder will fall, and down comes coder, PC and all...")