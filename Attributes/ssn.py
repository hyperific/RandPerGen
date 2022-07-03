import random
def get(line):
    s_min = int(line[3])
    s_max = s_min
    if line[4] != 0:
        s_max = int(line[4])
    s = str(random.randint(s_min, s_max+1)).zfill(3)
    g = random.randint(0,100)
    g = str(g).zfill(2)
    n = str(random.randint(0,10000)).zfill(4)
    ssn = s + "-" + g + "-" + n
    return ssn
