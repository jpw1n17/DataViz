import csv
import copy


lfRegion = 0
lfCount = 1
lfUnder = 2
lfNormal = 3
lfOver = 4
lfObese = 5
lfSObese = 6

nMeasures = 9
wroteHeader = False

ncrd =  { 'region': '', 'data': [] }

def writeHeadings(os, crd):
    headings = ['region', 'year']
    for m in crd['data']:
        headings.append(m[0])
    os.writerow(headings)

def writeRegion(os, crd, yls):
    i = 0
    for yl in yls:
        row = [crd['region'], yl]
        i = i + 1
        for c in crd['data']:
            row.append(c[i])

        os.writerow(row)

with open('Scotish_Primary1_BMI.csv', 'r') as csvin, open('Scotish_Primary1_BMI_T.csv', 'w') as csvout:
    inStream = csv.reader(csvin, delimiter=',')
    fieldnames = ['Region', 'Year', 'Sample size', 'Under weight', 'Healthy weight', 'Overweight', 'Obese', 'Severely obese' ]
    outStream = csv.writer(csvout, delimiter=',')
    rowC = 0
    yearLabels = []
    lf = lfRegion
    curRegion = ''
    crd = {}
    for row in inStream:
        rowC += 1
        if rowC == 1:
            for yl in row:
                if yl == '':
                    continue
                yearLabels.append(yl)
        # skip padding rows
        elif (row[0]) == '' or (row[0][0] == ' '):
            pass
        elif lf == lfRegion:
            crd = copy.deepcopy(ncrd)
            crd['region'] = row[0]
            lf = lfCount
        else:
            crd['data'].append(row)
            lf = lf + 1
            if lf == nMeasures:
                if not wroteHeader:
                    writeHeadings(outStream, crd)
                    wroteHeader = True
                    
                writeRegion(outStream, crd, yearLabels)
                lf = lfRegion


    

    
    

            
            

