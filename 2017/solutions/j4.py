MAX_TIME_LOOP = 720

def calculate_favourite_times():
    h = [1, 2]
    m = [0, 0]

    times = []


    for i in range(MAX_TIME_LOOP+1): # full loop of 12*60 minutes
        if (h[0] == 1):
            # no leading zero
            if (h[1]-h[0] == m[0] - h[1] ==  m[1] - m[0]):
                times.append(i)
        else:
            # yes leading zero
            if (m[0] - h[1] ==  m[1] - m[0]):
                times.append(i)

        # clock up
        m[1] += 1
        if (m[1] == 10):
            m = [m[0] + 1, 0]
            if (m[0] == 6):
                m = [0, 0]
                h[1] += 1
                if (h[0] == 1 and h[1] == 3):
                    h = [0, 1]
                elif (h[1] == 10):
                    h = [1, 0]

    return times

def favourite_times(n, times):
    # check if n is in the times array, thats all
    matches = 0

    while n > 0:
        # n is greater than the max time loop
        # as in, the minutes observed are greater
        # so we match it then reduce it by the max
        if (n >= MAX_TIME_LOOP):
            n -= MAX_TIME_LOOP
            matches += len(times)
        else:
            # n is now less than the max, so we
            # try to match it to the highest index
            max_time_index = 0
            for i, t in enumerate(times):
                if (n >= t):
                    # +1 because arrays are 0-indexed
                    max_time_index = i+1
            return matches + max_time_index
    return matches

# precalculate times and store them in an array
# have to do this because the time limit is pretty low
# times = calculate_favourite_times()

# literally wouldv been shorter for me to have done this
# manually lol.. or use a cheese string method
# wanted to do it more iteratively though
times = [34, 71, 83, 95, 107, 119, 130, 142, 154, 166, 178, 201, 213, 225, 237, 260, 272, 284, 296, 331, 343, 355, 390, 402, 414, 461, 473, 520, 532, 591, 671]


n = int(input()) # minutes observed
print(favourite_times(n, times))