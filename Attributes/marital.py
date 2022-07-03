import random
options = ['Single', 'Married','Separated','Divorced','Widowed']
def get(age):
    if age >=18:
        return random.choice(options)
    else:
        return 'Single'