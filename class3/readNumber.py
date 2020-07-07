def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiple(line, index):
    token = {'type': 'PRODUCT'}
    return token, index+1

def readDivision(line, index):
    token = {'type':'DIVISION'}
    return token, index+1

def readBracketLeft(line,index):
    token = {'type':'LEFT'}
    return token, index+1

def readBracketRight(line,index):
    token = {'type':'RIGHT'}
    return token, index+1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiple(line, index)
        elif line[index] == '/':
            (token, index) = readDivision(line, index)
        elif line[index] == '(':
            (token, index) = readBracketLeft(line, index)
        elif line[index] == ')':
            (token, index) = readBracketRight(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens
#function to evaluate brackets
def evaluateB(tokens):
    l=[]
    index = -1
    while index < len(tokens)-1:
        index +=1
        if tokens[index]['type'] == 'LEFT':
            l.append(index)
        elif tokens[index]['type'] == 'RIGHT':
            initial = l.pop()
            subtokens = tokens[initial+1:index]
            answer = evaluate2(subtokens)
            tokens[initial]={'type':'NUMBER','number':answer}
            del tokens[initial+1:index+1]
            index = initial
        else:
            continue
    return 0

#function to evaluate * and /
def evaluate1(tokens):
    index = -1
    while index < len(tokens)-1:
        index +=1
        if tokens[index]['type'] == 'PRODUCT':
            answer = tokens[index-1]['number']* tokens[index+1]['number']
        elif tokens[index]['type'] == 'DIVISION':
            if tokens[index+1]['number'] == 0:
                print("error-divided by zero")
                tokens[index] = {'type': 'x'}
                break;
            answer = tokens[index-1]['number']/ tokens[index+1]['number']
        else:
            continue
        tokens[index] = {'type': 'NUMBER', 'number': answer}
        tokens.pop(index-1)
        tokens.pop(index)
        index = index-2
    return 0
#function to evaluate +/-
def evaluate2(tokens):
    evaluateB(tokens)
    evaluate1(tokens)
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer


def test(line):
    tokens = tokenize(line)
    actualAnswer = evaluate2(tokens)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print("==== Test started! ====")
    test("1+2")
    test("1*2")
    test("1.0+2.1-3")
    test("1+2*5/6/8")
    test("0")
    test("1.05*(5+6.05)/11")
    test("(7/5)+((1*2)+3/8)")
    test("1.08+2.75/5-6.00/0")
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
