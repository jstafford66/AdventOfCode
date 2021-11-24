import re

#382345-843167

start = 382345
stop = 843167

reg = r"(.)\1{2,}"

p = re.compile(reg)

def double_repeats(txt):
    import itertools

    # find possible repeats
    candidates = set(re.findall(r'([0-9])\1', txt))

    # now find the actual repeated blocks
    repeats = itertools.chain(*[re.findall(r"({0}{0}+)".format(c), txt) for c in candidates])

    # return just the blocks of length 2
    return [x for x in repeats if len(x) == 2]

def testNum(s):

    m = double_repeats(s)

    if not m:
        return False
    
    dup = False
    increase = True

    l = s[0]
    for n in s[1:]:

        if n == l:
            dup = True
        elif n < l:
            increase = False
            break

        l = n
    
    if dup and increase:
        return True
    return False

cnt = 0

print(testNum("112233"))
print(testNum("123444"))
print(testNum("111122"))

for v in range(start, stop):
    s = str(v)
    
    if testNum(s):
        cnt = cnt + 1
        print(cnt)

print (cnt)