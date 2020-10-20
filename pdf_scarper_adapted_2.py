import csv 

import datetime

import re

import tabula

import g_calendar


file = "Data/Horario_Ing_Mat_PRUEBA.pdf"

# num_pages = 4

# for i in range(num_pages):
#     tabula.convert_into(file, "converted.csv", output_format="csv", pages=i+1)
diff = 0
n = 3
# for i in range(n):
#     tabula.convert_into(file, "Data/converted_PRUEBA{}_GABRIEL.csv".format(i), output_format="csv", pages=i+1) # better one by one

with open("Data/converted_PRUEBA{}_GABRIEL.csv".format(n), 'r') as f:
    content = csv.reader(f)

    for l in content:
        if bool(re.match('\d\d/\d\d/202\d- \d\d/\d\d/202\d', l[0])):
            # print(l[0])
            l_split = l[0].split('- ')
            startDate = datetime.date(*[int(x) for x in l_split[0].split('/')[::-1]])
            endDate = datetime.date(*[int(x) for x in l_split[1].split('/')[::-1]])

            if n == 2: # Arreglo bruto de atrasamiento de dias de la semana (problema del horario, en grupo 3)
                startDate -= datetime.timedelta(1)

            curDate = startDate - datetime.timedelta(3)

            reps = (endDate - startDate).days//5

        elif (len(l) > 2) and (bool(re.match('\d\d\d\d\d\d', l[1])) or bool(re.match('\d\d\d\d\d\d', l[0]))):
            # print(l[0])
            if l[0]:
                if bool(re.match('\d\d\d\d\d\d', l[0])):
                    diff = 1
                else:
                    if l[0] == 'UNES' or l[0] == 'LUNES':
                        curDate += datetime.timedelta(2)
                    curDate += datetime.timedelta(1)

            else:
                diff = 0
            
            fwdDate = curDate
            # meter evento
            for _ in range(reps):
                if fwdDate > endDate:
                    break
                
                body = '; '.join(l[1-diff:4-diff])
                hours = l[5-diff].split('-\n')
                # print(l, hours, diff)

                sDate = '{}-{:02d}-{:02d}T{}:00'.format(fwdDate.year, fwdDate.month, fwdDate.day, hours[0])
                eDate = '{}-{:02d}-{:02d}T{}:00'.format(fwdDate.year, fwdDate.month, fwdDate.day,  hours[1])
                
                print(body, sDate, eDate)
                g_calendar.add_event(body, sDate, eDate)

                fwdDate += datetime.timedelta(7)