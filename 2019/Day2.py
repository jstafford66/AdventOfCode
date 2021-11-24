import csv

debug = False

with open('day2_input.txt', 'r') as f:
  reader = csv.reader(f)
  memory = [int(v) for v in list(reader)[0]]

print (memory)

def sum(program, i):
    param1 = program[program[i+1]]
    param2 = program[program[i+2]]
    param3 = program[i+3]
    val = param1 + param2
    program[param3] = val
    return program, 4

def mult(program, i):
    param1 = program[program[i+1]]
    param2 = program[program[i+2]]
    param3 = program[i+3]
    val = param1 * param2
    program[param3] = val
    return program, 4

def runProgram(program):
    # i -- Instruction Pointer
    i = 0

    while(program[i] != 99):
        
        op = program[i]
        if op == 1:
            program, inc = sum(program, i)
        elif op == 2:
            program, inc = mult(program, i)
        elif op == 99:
            inc = 1
            break
        else:
            print ("Error: " + str(op) + " : " + str(i))

        i = i + inc
    
    return program

def restoreProgramDay2_1(memory):
    # Per instructions init value at 1 to 12 and value at 2 to 2
    program = list.copy(memory)
    program[1] = 12
    program[2] = 2

    return runProgram(program)[0]

def restoreGravityDay2_2(memory):

    program = list.copy(memory)
    done = False
    for noun in range(100):
        for verb in range(100):
            #initialze program with noun and verb
            program[1] = noun
            program[2] = verb

            res = runProgram(program)

            if res[0] == 19690720:
                done = True
                #print ("Found It")
                #print (noun)
                #print (verb)
                return ((100 * noun) + verb)
            
            program = list.copy(memory)

        if done == True:
            break

#print(restoreProgramDay2_1(memory)) #5305097
#print(restoreGravityDay2_2(memory)) #4925