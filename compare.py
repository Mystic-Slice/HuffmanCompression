import os
from tabulate import tabulate

SEPARATOR = "===================="

def readMetadata():
    with open("metadata.txt", "r") as f:
        timeTaken = [line.strip() for line in f if line.startswith('Time Taken: ')][0]
    
    timeTaken = timeTaken.split()
    timeTaken = timeTaken[-1]
    timeTaken = timeTaken[:-1]
    timeTaken = float(timeTaken)
    return round(timeTaken, 3)

def analyseData(cppTime, pythonTime):    
    cppAverage = sum(cppTime)/len(cppTime)
    pythonAverage = sum(pythonTime)/len(pythonTime)

    combinedList = list(zip(cppTime, pythonTime))
    combinedList = [[x+1] + list(combinedList[x]) for x in range(len(combinedList))]
    combinedList += [["Average", cppAverage, pythonAverage]]

    print("Results")
    print(SEPARATOR)
    print(tabulate(combinedList, headers=['Run', 'C++', 'Python'], tablefmt='github'))
    print()
    cppSpeed = 1/cppAverage
    pythonSpeed = 1/pythonAverage

    if(cppSpeed > pythonSpeed):
        print(f'C++ is {round(cppSpeed/pythonSpeed, 2)} times as fast as Python')
    else:
        print(f'Python is {round(pythonSpeed/cppSpeed, 2)} times as fast as C++')


if __name__ == '__main__':
    print("Huffman Compression")
    print(SEPARATOR)
    NUM_RUNS = 10

    os.chdir('cpp/')
    os.system('g++ HuffmanEncoding.cpp -o HuffmanEncoding')
    print("C++")
    print(SEPARATOR)
    cppTime = []
    for i in range(NUM_RUNS):
        print("Run", i+1)
        os.system('HuffmanEncoding')
        time = readMetadata()
        cppTime.append(time)
        print(SEPARATOR)


    os.chdir('..')
    os.chdir('python/')

    print("Python")
    print(SEPARATOR)
    pythonTime = []
    for i in range(NUM_RUNS):
        print("Run", i+1)
        os.system('python HuffmanEncoding.py')
        time = readMetadata()
        pythonTime.append(time)
        print(SEPARATOR)
    analyseData(cppTime, pythonTime)
    print(SEPARATOR)
