import csv

def LoadLines(file):
    input = open(file)
    lines = input.readlines()
    return lines

def LoadCSV(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        data = [int(v) for v in list(reader)[0]]
    
    return data