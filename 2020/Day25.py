

debug = False

if debug:
    c_key = 5764801
    d_key = 17807724
else:
    c_key = 11239946
    d_key = 10464955

def tranform(subject_number, loop_size):
    value = 1
    divisor = 20201227

    for loop in range(loop_size):
        value = value * subject_number
        value = value % divisor

    return value

def getBothLoops(c_key, d_key, subject_number=7):
    door_loop = -1
    card_loop = -1
    loop_size = 1
    value = 1
    divisor = 20201227

    while card_loop == -1 or door_loop == -1:
        value *= subject_number
        value = value % divisor
        
        if value == c_key:
            card_loop = loop_size
        if value == d_key:
            door_loop = loop_size

        loop_size += 1

    return card_loop, door_loop

def determineLoopSize(public_key, subject_number=7):
    loop_size = 1
    value = 1
    while value != public_key:
        if loop_size%100 == 0:
            print(loop_size)
        value = tranform(subject_number, loop_size)
        if value == public_key:
            break

        loop_size += 1

    return loop_size, subject_number

def getEncryptionKey(c_key, d_key, subject_number=7):
    #find loop size
    card_loop, door_loop = getBothLoops(c_key, d_key)
    print('Door loop:', door_loop)
    print('Card loop:', card_loop)


    # get encryption key
    c_encrypt = tranform(d_key, card_loop)
    d_encrypt = tranform(c_key, door_loop)

    if c_encrypt != d_encrypt:
        print("Something went wrong")
    
    return c_encrypt

encrypt = getEncryptionKey(c_key, d_key)

print(encrypt)