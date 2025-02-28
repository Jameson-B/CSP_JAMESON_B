# Jameson Bultez, How to Get the Time of the Day

import time

# First instance of time in programming
first_time = time.gmtime # Greenwhich Mean Time

# Current time in seconds
current = time.time()

# Current date and time like we noramlly see it
now = time.ctime(current)

# Get just a part of the time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour # 24-hour time (0:00-23:59)

# Print greeting based on time of day.
if hour == 12:
    print("Good noon!")
elif 0 <= hour < 12:
    print("Good morning.")
elif 12 <= hour < 17:
    print("Good afternoon.")
elif 17 <= hour < 21:
    print("Good evening.")
else:
    print("Good night.")
