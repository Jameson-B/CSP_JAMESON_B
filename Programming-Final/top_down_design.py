# Top Down Design Python 

# Purpose of Functions:
    # Break down the program into smaller parts.
    # Avoid repeated code.
    # Make the program more readable.
    # Helps us collaborate by splitting tasks into smaller pieces.

# Decompistion: big problem -> smaller and smaller problems.
# Function Nesting: functions within functions.

runner_x = 1
runner_y = 1

def moveToHurdle(x, y):
    x += 3
    y = y
    return x, y

def jumpHurdle(x, y):
    y += 1
    x += 1
    y -= 1
    return x, y

def runToFinish(x, y):
    x += 4
    y = y
    return x, y

def start():
    print(moveToHurdle(runner_x, runner_y))

    print(jumpHurdle(runner_x, runner_y))

    print(moveToHurdle(runner_x, runner_y))

    print(jumpHurdle(runner_x, runner_y))

    print(runToFinish(runner_x, runner_y))

    # return runner_x, runner_y

start()