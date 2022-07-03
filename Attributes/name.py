import random as rnd
import tsv2list as t2l
namesList = t2l.getlist("data/names.tsv",False)
def get():
    name = rnd.choice(namesList)
    return name
