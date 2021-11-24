import re

'''
acc increases or decreases a single global value called the accumulator by the value given in the argument. 
    For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. 
    After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the 
    argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, 
    jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 
    lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
'''

class interp:

    _instruction_re = '(\w+) ([\-|\+]\d+)'

    # Accumulator
    _acc = 0

    # instruction pointer
    _ip = 0

    _cmds = None

    def __init__(self):
        self._cmds = {
            'acc':interp.acc,
            'jmp':interp.jmp,
            'nop':interp.nop}

    def acc(self,val):
        self._acc += val

    def jmp(self,val):
        # subtact 1 from val because it will be added to ip later
        self._ip += (val-1)
    
    def nop(self, val):
        pass

    def parseProgram(filename):
        input = open(filename)
        lines = input.readlines()
        return lines

    def run(self, prog):
        self._ip = 0

        visited = []

        infinite = False
        while True:

            if self._ip >= len(prog):
                break
            if self._ip in visited:
                infinite = True
                break

            cmd, val = self.parseInstruction(prog[self._ip])

            visited.append(self._ip)

            self._cmds[cmd](self, val)
            self._ip += 1
        
        return self._acc, infinite

    def parseInstruction(self, instruction):
        match = re.findall(self._instruction_re, instruction)

        cmd = match[0][0]
        val = int(match[0][1])

        return cmd, val

