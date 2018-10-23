times = ["Time {0}".format(i) for i in "ABCDEF"]  # Sou preguiçoso
for time1 in times:
    for time2 in times:
        if time1!=time2:
            print("{0} x {1}".format(time1, time2))
