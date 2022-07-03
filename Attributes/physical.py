import random
eye_color = ["Green","Blue","Brown","Hazel","Amber"]
hair_color = ["Black", "Brown", "Auburn","Red","Blonde", "Gray","White","Pink","Green","Blue","Orange"]
def get(age):
    weight = random.randrange(90,250)
    eye = random.choice(eye_color)
    hair = random.choice(hair_color)
    height1 = random.randrange(4,6)
    height2 = random.randrange(0,12)
    bmi = round((weight/(height1*12)**2)*703,1)
    bmi_class = ''
    if bmi <=18.5:
        bmi_class = 'Underweight'
    elif bmi >=18.5 and bmi <= 24.9:
        bmi_class = 'Healthy'
    elif bmi >=25.0 and bmi <=29.9:
        bmi_class = 'Overweight'
    else:
        bmi_class = 'Obese'
    return weight,eye,hair, (height1,height2),(bmi,bmi_class)