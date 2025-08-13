import time

hours = 0
minutes = 0
seconds = 0

while hours < 1:  # run for 1 hour
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.2)  # speed up for demo
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
print("Clock stopped after 1 hour.")
