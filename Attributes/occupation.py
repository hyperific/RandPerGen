import random as rnd
import tsv2list as t2l
occList = t2l.getlist(r"U:\Code Projects\Python\Utilities\RandPerGen\data\occupations.tsv")
def get():
    return rnd.choice(occList)