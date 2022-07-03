import random as rnd
import tsv2list as t2l
statelist = t2l.getlist("data/state.tsv",True)
def get():
    line = statelist[rnd.randint(0,len(statelist)-1)]
    return line
