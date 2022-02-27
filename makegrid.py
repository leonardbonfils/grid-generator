import random
import os
import string

path = os.path.dirname(__file__)
path = path.replace('\\', '/')

with open(path + '/dict_demo.txt') as dict:
    dictLines = dict.readlines()

fixedDictLines = []
for i, line in enumerate(dictLines):
    fixedDictLines.append(dictLines[i].replace('\n', ''))

gridSize = [3, 4, 5, 6, 8, 10, 20, 30, 40, 50, 60, 70, 100, 1000, 2000, 3000, 4000, 5000]
dictSize = len(dictLines)

for size in gridSize:
    i = 0
    with open(path + '/pygrid' + str(size) + '.txt', 'w') as grid:
        grid.write(str(size) + '\n')
        while (i<size):
            newLine = ''
            while len(newLine)<size:
                # 50% chance we insert a real word
                # Other 50% --> insert bad characters
                dictWordOrNot = bool(random.getrandbits(1))
                if dictWordOrNot:
                    # Insert real dictionary word
                    randomWordIndex = random.randrange(1,dictSize)
                    if (size-len(newLine))>=len(fixedDictLines[randomWordIndex]):
                        newLine += fixedDictLines[randomWordIndex]
                    else:
                        newLine += fixedDictLines[randomWordIndex][0:size-len(newLine)]
                else:
                    # Insert 1-3 bad characters
                    if size > len(newLine):
                        numberOfBadChars = random.randrange(0, size-len(newLine))
                        badCharIndex = 0
                        while (badCharIndex < numberOfBadChars):
                            newLine += random.choice(string.ascii_lowercase)
                            badCharIndex += 1
            print(newLine)
            grid.write(newLine + '\n')
            i+= 1
        grid.close()