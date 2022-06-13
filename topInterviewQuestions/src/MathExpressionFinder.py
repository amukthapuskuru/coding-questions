def mathExpressionFinder(expr:str)-> float:
    math_dict = {'(':')'}
    stack=[]
    val =int(expr[0])

    for num in range(len(expr)-1):
        print(expr[num+1],expr[num],val)
        if not expr[num].isdigit():
            if expr[num] == '*':
                val *= int(expr[num+1])
            elif expr[num] == '/':
                val /= int(expr[num+1])
            elif expr[num] == '+':
                val += int(expr[num+1])
            elif expr[num] == '-':
                val -= int(expr[num+1])
            else:
                'check the number'
    return val

#def parenthesis()

print(mathExpressionFinder('4*3/2-2*3'))