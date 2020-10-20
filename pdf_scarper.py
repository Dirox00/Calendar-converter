import csv 

import datetime

import re

import tabula

import g_calendar


file = "Horario_Ing_Mat_PRUEBA.pdf"

num_pages = 4

# for i in range(num_pages):
#     tabula.convert_into(file, "converted.csv", output_format="csv", pages=i+1)
tabula.convert_into(file, "converted_PRUEBA.csv", output_format="csv", pages=1) # better one by one
exit()
with open("converted_PRUEBA.csv", 'r') as f:
    content = csv.reader(f)

    for l in content:
        if bool(re.match('\d\d/\d\d/202\d- \d\d/\d\d/202\d', l[0])):
            l_split = l[0].split('- ')
            startDate = datetime.date(*[int(x) for x in l_split[0].split('/')[::-1]])
            endDate = datetime.date(*[int(x) for x in l_split[1].split('/')[::-1]])

            curDate = startDate - datetime.timedelta(3)

            reps = (endDate - startDate).days//5

        elif len(l) > 2 and bool(re.match('\[\d\d\d\d\d\d', l[1])):
            if l[0]:
                if l[0] == 'UNES':
                    curDate += datetime.timedelta(2)
                curDate += datetime.timedelta(1)
            fwdDate = curDate
            # meter evento
            for _ in range(reps):
                body = '; '.join([l[1], l[3], l[4]])
                hours = l[5].split('-\n')
                sDate = '{}-{:02d}-{:02d}T{}:00'.format(fwdDate.year, fwdDate.month, fwdDate.day, hours[0])
                eDate = '{}-{:02d}-{:02d}T{}:00'.format(fwdDate.year, fwdDate.month, fwdDate.day, hours[1])
                print(body, '\n', sDate, '\n', eDate, '\n'*3)

                GMT_OFF = '+02:00'
                EVENT = {
                    'summary': body,
                    'start': {'dateTime': '{}{}'.format(sDate, GMT_OFF)},
                    'end': {'dateTime': '{}{}'.format(eDate, GMT_OFF)}
                }
                g_calendar.add_event(EVENT)

                fwdDate += datetime.timedelta(7)