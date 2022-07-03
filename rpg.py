from guizero import App, Picture,Box, Text, PushButton, CheckBox, TextBox
import Attributes.ssn, Attributes.personality, Attributes.state, Attributes.name, Attributes.phone, Attributes.occupation, Attributes.age, Attributes.physical, Attributes.signs, Attributes.marital
import random
import math
import locale
locale.setlocale(locale.LC_ALL,'')
def execute():
    file = open('output.tsv','w')
    header = 'Name' + '\t' + 'Gender' + '\t' + 'Ethnicity' + '\t' + "DOB" + '\t' + 'Age' + '\t' + 'State' + '\t' + 'City' + '\t'
    if ui_tgl_occupation.value == 1:
        header += 'Occupation' + '\t'
    if ui_tgl_ssn.value == 1:
        header += 'SSN' + '\t'
    if ui_tgl_pers.value == 1:
        header += 'Personality' + '\t'
    if ui_tgl_pn.value==1:
        header += 'Phone' + '\t'
    if ui_tgl_income.value==1:
        header += 'Income' + '\t'
    if ui_tgl_signs.value==1:
        header += 'Sign' + '\t'
    if ui_tgl_physical.value ==1:
        header += "Eye Color" + '\t' + 'Hair Color' + '\t' + 'Height' + '\t' + 'Weight' + '\t' + 'BMI' + '\t'
    if ui_tgl_marital.value==1:
        header += "Marital Status" + '\t'
    header += '\n'
    data = []
    for _ in range(int(ui_input_num.value)):
        output = ''
        ##NAME, GENDER, ETHNICITY
        name_line = Attributes.name.get()
        nm = name_line[2]
        gnd = name_line[1]
        eth = name_line[0]
        output += nm+'\t'
        output += gnd+'\t'
        output += eth+'\t'
        ##AGE
        dob = Attributes.age.get_dob()
        age = Attributes.age.calculate_age(dob)
        output += str(dob) + '\t'
        output += str(age) + '\t'
        ##STATE, SSN, PHONE
        st_line = Attributes.state.get()
        output += str(st_line[0]) + '\t'
        output += str(st_line[2]) + '\t'
        occupation = Attributes.occupation.get()
        if ui_tgl_occupation.value == 1:
            output+= occupation[0] + '\t'
        if ui_tgl_ssn.value == 1:
            ssn = Attributes.ssn.get(st_line)
            output+= ssn + '\t'
        if ui_tgl_pers.value == 1:
            personality = Attributes.personality.get()
            output += personality + '\t'
        if ui_tgl_pn.value==1:
            phone = Attributes.phone.get(st_line)
            output += phone + '\t'
        if ui_tgl_income.value==1:
            income = locale.currency(int(math.ceil(random.randrange(int(occupation[1]),int(occupation[2]))/100.0))*100,grouping=True)
            output += str(income) + '\t'
        if ui_tgl_signs.value==1:
            sign = Attributes.signs.get(dob)
            output += sign + '\t'
        ## PHYSICAL DESCRIPTION
        if ui_tgl_physical.value ==1:
            weight,eye,hair,height,bmi = Attributes.physical.get(age)
            output += eye +'\t'
            output += hair +'\t'
            output += str(height[0])+ "ft" +str(height[1])+'in' + '\t'
            output += str(weight) +'\t'
            output += str(bmi[0]) + " (" + str(bmi[1]) +")" +'\t'
        if ui_tgl_marital.value==1:
            marital = Attributes.marital.get(age)
            output += marital + '\t'
        data.append(output + '\n')
    file.write(header)
    file.writelines(data)
    print('Done')
def selectall():
    ui_tgl_occupation.value = 1
    ui_tgl_ssn.value = 1
    ui_tgl_pn.value = 1 
    ui_tgl_pers.value = 1
    ui_tgl_income.value = 1
    ui_tgl_physical.value = 1
    ui_tgl_signs.value = 1
    ui_tgl_marital.value = 1
def selectnone():
    ui_tgl_occupation.value = 0
    ui_tgl_ssn.value = 0
    ui_tgl_pn.value = 0 
    ui_tgl_pers.value = 0
    ui_tgl_income.value = 0
    ui_tgl_physical.value = 0
    ui_tgl_signs.value = 0
    ui_tgl_marital.value = 0
## GUI ZERO
app = App(title='Random Person Generator', bg='#656565', height=600, width=400)
pic = Picture(app, image='images/cover.png')
#Quantity
ui_box_quantity=Box(app, border=1, width=250, height=150)
ui_text_quantity=Text(ui_box_quantity, text='Quantity')
ui_input_num = TextBox(ui_box_quantity, width=10)

ui_selectall = PushButton(ui_box_quantity,text= 'Select All',command=selectall)
ui_selectnone = PushButton(ui_box_quantity,text= 'Select None',command=selectnone)
#Options
ui_box_options=Box(app, border=1,layout="grid", width=250, height=300)
ui_text_options=Text(ui_box_options, grid=[1,0], align='top', text='Options')

ui_tgl_occupation = CheckBox(ui_box_options,grid=[1,1],align='left',text='Use Occupation')
ui_tgl_ssn = CheckBox(ui_box_options, grid=[1,2],align='left',text='Use Social Security Number')
ui_tgl_pn = CheckBox(ui_box_options, grid=[1,3],align='left',text='Use Phone Number')
ui_tgl_pers = CheckBox(ui_box_options, grid=[1,4],align='left',text='Use Personality')
ui_tgl_income = CheckBox(ui_box_options, grid=[1,5],align='left',text='Use Income')
ui_tgl_physical = CheckBox(ui_box_options,grid=[1,6],align='left',text="Use Physical")
ui_tgl_signs = CheckBox(ui_box_options,grid=[1,7],align='left',text="Use Astrological Signs")
ui_tgl_marital = CheckBox(ui_box_options,grid=[1,8],align='left',text="Use Marital Status")

#Execute
ui_box_exec=Box(app,border=1, width=250,height=95)
ui_execute = PushButton(ui_box_exec, text='Execute', command=execute)
app.display()