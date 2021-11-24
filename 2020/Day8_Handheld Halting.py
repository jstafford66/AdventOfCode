from BootCode import interp


def part1(filename):
    prog = interp.parseProgram(filename)

    boot = interp()

    val, visited = boot.run(prog)
    visited.sort()
    return val, visited

def part2(filename):
    prog = interp.parseProgram(filename)

    for i in range(len(prog)):
        save = prog[i]
        changed = False
        if 'jmp' in prog[i]:
            prog[i] = prog[i].replace('jmp', 'nop')
            changed = True
        elif 'nop' in prog[i]:
            prog[i] = prog[i].replace('nop', 'jmp')
            changed = True

        if changed:
            boot = interp()
            val, infinite = boot.run(prog)

            if not infinite:
                break
        
        prog[i] = save

    return val

print(part2('d8input.txt'))