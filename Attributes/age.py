import datetime
import random
def get_dob():
    end = datetime.date(2004,1,1) #Most recent time
    start = datetime.date(1927,1,1) #Least recent time
    delta = end - start #Difference
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds 
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)
def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
