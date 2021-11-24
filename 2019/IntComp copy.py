import csv
import queue
import itertools

def loadDayInput(loc):
    with open(loc, 'r') as f:
        reader = csv.reader(f)
        memory = [int(v) for v in list(reader)[0]]

    print (memory)
    return memory

class intComp:

    def __init__(self, prog):
        self.program = prog
        self.inputQueue = queue.Queue()
        self.outputQueue = queue.Queue()
        self.ip = 0
        self.sleep = False
    
    def getInstruction(self):
        instruction = str(self.program[self.ip])

        l = len(instruction)
        if l == 1:
            op = int(instruction)
        else:
            op = int(instruction[-2:])
        
        modes = [0,0,0]
        if l >= 3:
            modes[0] = int(instruction[-3])
        if l >= 4:
            modes[1] = int(instruction[-4])
        if l >= 5:
            modes[2] = int(instruction[-5])
        
        return op, modes

    def getParam(self, mode, index):
        if mode == 0:
            return self.program[self.program[index]]
        if mode == 1:
            return self.program[index]

    def addition(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)
        param3 = self.program[self.ip+3]
        val = param1 + param2
        self.program[param3] = val
        self.ip = self.ip + 4

    def mult(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)
        param3 = self.program[self.ip+3]
        val = param1 * param2
        program[param3] = val
        self.ip = self.ip + 4

    def readinput(self, modes):
        param1 = self.program[self.ip+1]

        if self.inputQueue.empty():
            value = input("Waiting for input:")
        else:
            value = self.inputQueue.get()
            print('Input From Queue:' + str(value))

        self.program[param1] = int(value)

        self.ip = self.ip + 2

    def writevalue(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        print("Out: " + str(param1))

        self.outputQueue.put(param1)
        self.sleep = True

        self.ip = self.ip + 2

    def ifTrue(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)

        inc = self.ip+3

        if param1 != 0:
            inc = param2
        
        self.ip = inc

    def ifFalse(slef, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)

        inc = i+3

        if param1 == 0:
            inc = param2
        
        self.ip = inc

    def lessThan(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)
        param3 = self.program[self.ip+3]

        if param1 < param2:
            self.program[param3] = 1
        else:
            self.program[param3] = 0
        
        self.ip = self.ip + 4

    def equal(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)
        param3 = self.program[self.ip+3]

        if param1 == param2:
            self.program[param3] = 1
        else:
            self.program[param3] = 0
        
        self.ip = self.ip + 4

    def run(self):

        operations = [addition, mult, readinput, writevalue, ifTrue, ifFalse, lessThan, equal]
        self.sleep = False

        while(self.program[self.ip] != 99):
            
            op, modes = self.getInstruction()

            if op == 99:
                inc = 1
                break
            else:
                operations[op - 1](self, modes)
            
            if self.sleep:
                return self.outputQueue.get()
        
        return None

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

def testDay5NewOp(memory):
    runProgram(list.copy(memory))

def testDay5Modes(memory):
    runProgram(memory)

def runDay5Part1():
    memory = loadDayInput('Day5_input.txt')

    runProgram(memory)

def runAmps(memory, phaseSequence):

    #Since the first AMP needs zero input, and we want to read output for all other amps.
    #init the output queue with the first one.
    outputQueue.put(0)

    ampMem = [list.copy(memory),list.copy(memory),list.copy(memory),list.copy(memory),list.copy(memory)]

    for amp in range(5):
        #Set the phase input for this amp
        inputQueue.put(phaseSequence[amp])
        #Get the last output as the input for the amp
        inputQueue.put(outputQueue.get())

        ampMem[amp] = runProgram(ampMem[amp])

    return outputQueue.get()

def Day7Part1(memory):
    phaseCombs = itertools.permutations([0,1,2,3,4])

    outputs = []
    for comb in phaseCombs:
        outputs.append(runAmps(list.copy(memory), comb))
    
    res = max(outputs)
    return res
    
#print(restoreProgramDay2_1(loadDay2Input('day2_input.txt'))) #5305097
#print(restoreGravityDay2_2(loadDay2Input('day2_input.txt'))) #4925
#testDay5NewOp([3,0,4,0,99])
#testDay5Modes([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
#runDay5Part1()

#print("Test Out: ", runAmps([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
#1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2]))

#print("Day7 Part 1:", Day7Part1(loadDayInput('Day7_input.txt')))

print("Test Out: ", runAmps([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5]))
