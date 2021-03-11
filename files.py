import os
os.system('cls')

def countLines(file):
    count = 0
    for line in file:
        line.rstrip()
        count+=1
    return count


def getJsonData(file):
    result = ""
    for line in file:
        print(line)
    return result;


try:
    fhand = open('./data.json')
    # lines = countLines(fhand)
    data = getJsonData(fhand)
except:
    print('File error')
