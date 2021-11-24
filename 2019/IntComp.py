import csv
import queue
import itertools

def loadDayInput(loc):
    with open(loc, 'r') as f:
        reader = csv.reader(f)
        memory = [int(v) for v in list(reader)[0]]

    return memory

class intComp:

    def __init__(self, prog, outSleep = True, waitForIn = False):
        self.program = prog

        self.program.extend([0 for i in range(len(self.program)*100)])

        self.inputQueue = queue.Queue()
        self.outputQueue = queue.Queue()
        self.ip = 0
        self.rel_base = 0
        self.sleep_on_out = outSleep
        self.wait_for_input = waitForIn
        self.sleep = False
        self.waiting = False
        self.halted = False
        self.operations = [intComp.addition, intComp.mult, intComp.readinput, intComp.writevalue, 
        intComp.ifTrue, intComp.ifFalse, intComp.lessThan, intComp.equal, intComp.setRelativeBase]

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
        if mode == 2:
            return self.program[self.rel_base + self.program[index]]

    def storeValue(self, mode, index, value):
        if mode == 0:
            self.program[self.program[index]] = value
        elif mode == 1:
            print("Trying to store in mode 1, which doesn't makes sense.")
        elif mode == 2:
            self.program[self.rel_base + self.program[index]] = value
        
    def addition(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)
        val = param1 + param2
        self.storeValue(modes[2], self.ip+3, val)
        self.ip = self.ip + 4

    def mult(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)
        val = param1 * param2
        self.storeValue(modes[2], self.ip+3, val)
        self.ip = self.ip + 4

    def readinput(self, modes):
        if self.wait_for_input and self.inputQueue.empty():
            self.waiting = True
            return

        if self.inputQueue.empty():
            value = input("Waiting for input:")
        else:
            value = self.inputQueue.get()

        self.storeValue(modes[0], self.ip+1, int(value))

        self.ip = self.ip + 2

    def writevalue(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)

        self.outputQueue.put(param1)

        if (self.sleep_on_out):
            self.sleep = True
        
        self.ip = self.ip + 2

    def ifTrue(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)

        inc = self.ip+3

        if param1 != 0:
            inc = param2
        
        self.ip = inc

    def ifFalse(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)

        inc = self.ip+3

        if param1 == 0:
            inc = param2
        
        self.ip = inc

    def lessThan(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)

        if param1 < param2:
            val = 1
        else:
            val = 0
        
        self.storeValue(modes[2], self.ip+3, val)

        self.ip = self.ip + 4

    def equal(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)
        param2 = self.getParam(modes[1], self.ip+2)

        if param1 == param2:
            val = 1
        else:
            val = 0
        
        self.storeValue(modes[2], self.ip+3, val)

        self.ip = self.ip + 4

    def setRelativeBase(self, modes):
        param1 = self.getParam(modes[0], self.ip+1)

        self.rel_base += param1
        self.ip = self.ip + 2

    def putInput(self, value):
        self.inputQueue.put(value)
        return self

    def run(self):

        self.sleep = False
        self.waiting = False

        while(self.program[self.ip] != 99):
            
            op, modes = self.getInstruction()

            if op == 99:
                inc = 1
                self.halted = True
                break

            self.operations[op - 1](self, modes)
            
            if self.waiting:
                return None

            if self.sleep:
                return self.outputQueue.get()
        
        self.halted = True
        return None

def runAmps(memory, phaseSequence):

    amps = [intComp(list.copy(memory)).putInput(phase) for phase in phaseSequence]
    signal = 0

    for amp in amps:
        amp.putInput(signal)
        signal = amp.run()

    return signal

def Day7Part1(memory):
    phaseCombs = itertools.permutations([0,1,2,3,4])

    outputs = []
    for comb in phaseCombs:
        outputs.append(runAmps(list.copy(memory), comb))
    
    res = max(outputs)
    return res

def runFeedbackAmps(memory, phaseSequence):
    
    amps = [intComp(list.copy(memory)).putInput(phase) for phase in phaseSequence]
    signal = 0
    result = 0

    while result is not None:
        for amp in amps:
            signal = result
            amp.putInput(signal)
            result = amp.run()

            if result is None:
                break

    return signal

def Day7Part2(memory):
    phaseCombs = itertools.permutations([5,6,7,8,9])

    outputs = []
    for comb in phaseCombs:
        outputs.append(runFeedbackAmps(list.copy(memory), comb))
    
    res = max(outputs)
    return res

#x = intComp(list.copy(loadDayInput('Day9input.txt')),False)

#print(x.run())
#print("Test Out: ", runAmps([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2]))

#print("Day7 Part 1:", Day7Part1(loadDayInput('Day7_input.txt')))

#print("Test Out: ", runFeedbackAmps([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0]))

#print("Test Out: ", runFeedbackAmps([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5]))

# print("Test Out: ", runFeedbackAmps([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], [9,7,8,5,6]))

#print("Day7 Part 2:", Day7Part2(loadDayInput('Day7_input.txt')))

#print(intComp([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99], False).run())

#print(intComp([1102,34915192,34915192,7,4,7,99,0], False).run())
#print(intComp([104,1125899906842624,99], False).run())
