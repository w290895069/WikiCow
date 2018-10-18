import time, math

def getTimesdfasfaef():
    timeNow = time.time()

    second = int(timeNow % 60)
    timeNow /= 60
    
    minute = int(timeNow % 60)
    timeNow /= 60
    
    hour = int(timeNow % 24)
    timeNow /= 24
    
    remainder = timeNow % (365 * 4 + 1);
    
    if remainder < 365:
        day = math.ceil(remainder)
        cycle = 1
    elif remainder < 365 * 2:
        day = math.ceil(remainder - 365)
        cycle = 2
    elif remainder < 365 * 3 + 1:
        day = math.ceil(remainder - 2 * 365)
        cycle = 3
    else:
        day = math.ceil(remainder - 1 - 3 * 365)
        cycle = 4
        
    if cycle == 3:
        months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = 1970 + math.floor(timeNow / (365 * 4 + 1) * 4)

    i = 0
    while (day > months[i]):
        day -= months[i]
        i += 1

    month = i + 1

    params = (year, month, day, hour, minute, second)
    return "?/?/? ?:?:?", params
