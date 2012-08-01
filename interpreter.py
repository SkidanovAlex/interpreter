import sys

REGS = 4

reg_names = [chr(i + ord('a')) for i in range(REGS)]

def identity():
    return [[1 if i == j else 0 for j in range(REGS + 1)] for i in range(REGS + 1)]

# matrix operations

def vecmul(v, m):
    ret = [0 for i in v]
    for i in range(len(ret)):
        for j in range(len(ret)):
            ret[i] += v[j] * m[j][i]
    return ret

def matmul(m1, m2):
    return [vecmul(row, m2) for row in m1]

def matpow(m, p):
    if p == 0: return identity()
    elif p % 2 == 0:
        tmp = matpow(m, p / 2)
        return matmul(tmp, tmp)
    else: return matmul(m, matpow(m, p - 1))

# implementation of =, +=, -=, *=

def movreg(r1, r2):
    ret = identity()
    ret[r1][r1] = 0
    ret[r2][r1] = 1
    return ret

def movval(r, val):
    ret = identity()
    ret[r][r] = 0
    ret[REGS][r] = val
    return ret

def addreg(r1, r2):
    ret = identity()
    ret[r2][r1] = 1
    return ret

def addval(r, val):
    ret = identity()
    ret[REGS][r] = val
    return ret

def subreg(r1, r2):
    ret = identity()
    ret[r2][r1] = -1
    return ret

def subval(r, val):
    return addval(r, -val)

def mulval(r, val):
    ret = identity()
    ret[r][r] = val
    return ret

def doit():
    mat = identity()
    while True:
        line = sys.stdin.readline().lower()
        tokens = line.split()
        if tokens[0] == 'loop':
            cur = matpow(doit(), long(tokens[1]))
        elif tokens[0] == 'end':
            return mat
        else:
            r1 = reg_names.index(tokens[0])
            try:
                r2 = reg_names.index(tokens[2])
            except:
                r2 = -1
            if tokens[1] == '+=':
                if r2 == -1: cur = addval(r1, long(tokens[2]))
                else: cur = addreg(r1, r2)
            elif tokens[1] == '-=':
                if r2 == -1: cur = subval(r1, long(tokens[2]))
                else: cur = subreg(r1, r2)
            elif tokens[1] == '=':
                if r2 == -1: cur = movval(r1, long(tokens[2]))
                else: cur = movreg(r1, r2)
            elif tokens[1] == '*=':
                if r2 == -1: cur = mulval(r1, long(tokens[2]))
                else: assert False
            else: assert False
        mat = matmul(mat, cur)
       
res = vecmul([0 for i in range(REGS)] + [1], doit())
print res[:4]

