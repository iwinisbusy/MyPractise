def lab1_q9a():
    # getting the seconds from User
    hr = int(input("Enter current hr: "))
    min = int(input("Enter current min: "))
    sec = int(input("Enter current sec: "))
    print("Clock time is {:02d}:{:02d}:{:02d}".format(hr, min, sec))

    number = hr*3600 + min*60 + sec + 1  # add 1 sec to current time

    # Processing: computations to convert into hrs, mins and secs
    hours = number // 3600 % 24  # count time then need % 24
    minutes = number // 60 % 60  # % 60 to ensure 61 min = 1 min
    seconds = number % 60    # 661 sec = 1 sec

    # Output: display the result (hours, minutes and seconds)
    #print(hours, "hr", minutes, "min", seconds, "sec")
    print("After 1 second, the time is {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
    
def lab1_q9b():
    hr = int(input("Enter Hour: "))
    min = int(input("Enter Minute: "))
    sec = int(input("Enter Second: "))
    print("Time is {:02d}:{:02d}:{:02d}:".format(hr, min, sec))

    timecal = hr*3600 + min*60 + sec + 1

    hour = timecal//3600%24
    minutes = timecal//60%60
    seconds = timecal%60
    print("1 second later, the time is {:02d}:{:02d}:{:02d}".format(hour, minutes, seconds))

lab1_q9b()