def get(dob):
    dob = str(dob)
    dob = dob.split('-')
    month = int(dob[1])
    day = int(dob[2])
    astr = ''
    if (month==1 and day>=20) or (month==2 and day<=18):
        astr = 'Aquarius'
    elif (month==2 and day>=19) or (month==3 and day<=20):
        astr = 'Pisces'
    elif (month==3 and day>=21) or (month==4 and day<=19):
        astr = 'Aries'
    elif (month==4 and day>=20) or (month==5 and day<=20):
        astr = 'Taurus'
    elif (month==5 and day>=21) or (month==6 and day<=20):
        astr = 'Gemini'
    elif (month==6 and day>=21) or (month==7 and day<=22):
        astr = 'Cancer'
    elif (month==7 and day>=23) or (month==8 and day<=22):
        astr = 'Leo'
    elif (month==8 and day>=23) or (month==9 and day<=22):
        astr = 'Virgo'
    elif (month==9 and day>=23) or (month==10 and day<=22):
        astr = 'Libra'
    elif (month==10 and day>=23) or (month==11 and day<=21):
        astr = 'Scorpio'
    elif (month==11 and day>=22) or (month==12 and day<=21):
        astr = 'Sagittarius'
    elif (month==12 and day>=22) or (month==1 and day<=19):
        astr = 'Capricorn'
    return astr