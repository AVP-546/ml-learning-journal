import time ##Time module

my_time = int(input("Enter your time in seconds: "))
if(my_time < 0):
    my_time = int(input("Not possible. Enter your time in seconds: "))

for counter in range(my_time, 0, -1): ## Same thing as using the reverse function
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1) ## Our program will actually "sleep" for x seconds, in this case, 1

print("TIME'S UP!!")