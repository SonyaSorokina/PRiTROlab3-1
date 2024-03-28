def readFile(text):
    f = open(text, 'r', encoding="UTF-8")
    numbers = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        numbers.append(int(line))
    return numbers

def guessTheNumber(numbers):
    for number in numbers:
        answ = 0
        lenNumber = len(str(number))
        for i in range (7, 32):
            if (str(number) == (str(2**i)[0:lenNumber])) and ((len(str(2**i)))/(lenNumber)>2):
                answ = i
                break
        if answ==0:
            print("no power  of  2")
        else:
            print(answ)

from os import listdir, getcwd

print(getcwd())
files = [i for i in listdir(getcwd()) if ".txt" in i]

for i, file in enumerate(files, start=1):
    try:
        print(f"Тест {i}")
        guessTheNumber(readFile(file))
    except Exception as e:
        print(e)

