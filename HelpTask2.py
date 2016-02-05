import math
fI = "input.txt"
with open(fI,'r') as input :
    a = int(input.readline())

def isPrime(N):
    if N == 1:
        return False
    for x in xrange(2, int(math.floor(math.sqrt(N)) + 1)):
        if N % x == 0 and N != x:
            return False
    return  True

def isPrimeAndNear():
    for i in xrange(1, min(math.fabs(2*(10**9) - a),a)):
        x = a - i
        y = a + i

        if isPrime(x) and isPrime(y):
            answer =  x
            break
        if isPrime(x) or isPrime(y):
            if isPrime(x):
                answer = x
                break
            else:
                answer = y
                break
    return answer

answer = str(isPrimeAndNear())
print (answer)
fO = "output.txt"
with open(fO,'w') as output :
    output.write(answer)
