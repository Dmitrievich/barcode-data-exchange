# app.py
# pip install xlwt
import xlwt

# Open a file and read it
inputFile = open('in.txt', 'r')
outData = inputFile.read()

# Make an array from data without '\n' symbols
tempArr = outData.split('\n')

# Clean an array from blank values
outTempArr = []
for item in tempArr:
    if len(item) > 0:
        outTempArr.append(item)
#print(outTempArr)


outDict = {}
while len(outTempArr) > 0:
    temp = outTempArr[0]
    outDict[temp] = outTempArr.count(temp)
    for i in range( outDict[temp] ):
        outTempArr.remove(temp)

#print(outDict)


# Создаем книку
outBook = xlwt.Workbook('utf8')

# Добавляем лист
outSheet = outBook.add_sheet('sheetname')

# Заполняем ящейку (Строка, Колонка, Текст, Шрифт)

row = 0

for key in outDict:
    #print(key)
    column = 0
    outSheet.write(row, column, int(key))
    column += 1
    outSheet.write(row, column, int(outDict[key]))
    row += 1


# Сохраняем в файл
outBook.save('out.xls')



# Close a file
inputFile.close()
print('Файл закритий = {}'.format(inputFile.closed))

# Exit from command prompt
input('Натисніть будь яку клавішу для виходу...')