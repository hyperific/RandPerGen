import random as rnd
def get(line):
    acs = str(line[5]).split()
    ac = rnd.choice(acs)
    prefix = str(rnd.randint(0,1000)).zfill(3)
    line = str(rnd.randint(0,10000)).zfill(4)
    pn = ac + '-' + prefix + '-' + line
    return pn