import tabula

import csv 

import re


file = "Horario_Ing_Mat_1o_BIEN.pdf"

# tabula.convert_into(file, "converted.csv", output_format="csv", pages="all")

with open("converted.csv", 'r') as f:
    content = csv.reader(f)

    for l in content:
        if bool(re.match('\d\d/\d\d/202\d- \d\d/\d\d/202\d', l[0])):
            l_split = l[0].split('- ')
            startDate = [int(x) for x in l_split[0].split('/')]
            endDate = [int(x) for x in l_split[1].split('/')]

            curDate = startDate - 3
        elif len(l) > 2 and bool(re.match('\[\d\d\d\d\d\d', l[1])):
            if l[0]:
                if l[0] == 'UNES':
                    curDate[0] += 2
                curDate[0] += 1
            # meter evento
            body = l[1] + l[3] + l[4]
            hours = l[5].split('-\n')
            sDate = '{}-{}-{}T{}:00'.format(curDate[2], curDate[1], curDate[0], hours[0])
            eDate = '{}-{}-{}T{}:00'.format(curDate[2], curDate[1], curDate[0], hours[1])
            print(body, '\n', sDate, '\n', eDate, '\n'*3)