def arithmetic_arranger(problems,printanswer = False):

    sums = list()
    topline = str()
    secondline = str()
    dashline = str()
    answerline = str()

    if len(problems) > 5: return 'Error: Too many problems.'

    for problem in problems:

        probcomp = problem.split()

        if not probcomp[0].isnumeric() or not probcomp[2].isnumeric(): return 'Error: Numbers must only contain digits.'
        if len(probcomp[0]) > 4 or len(probcomp[2]) > 4: return 'Error: Numbers cannot be more than four digits.'
        if not probcomp[1] in ('+','-'): return 'Error: Operator must be \'+\' or \'-\'.'
        
        if probcomp[1] == '+':
            answer = str(int(probcomp[0]) + int(probcomp[2]))
        else:
            answer = str(int(probcomp[0]) - int(probcomp[2]))
        
        maxpad = max(len(probcomp[0]), len(probcomp[1]) , len(probcomp[2]), len(answer) -  2) + 2
        sums.append([probcomp[0],probcomp[1],probcomp[2], answer, maxpad])

    for sum in sums:
        if len(topline) > 0:
            topline = topline + ' ' * 4
            secondline = secondline + ' ' * 4
            dashline = dashline + ' ' * 4
            answerline = answerline + ' ' * 4
    
        topline = topline + sum[0].rjust(sum[4],' ')
        secondline = secondline + sum[1] + ' ' + sum[2].rjust(sum[4] - 2,' ')
        dashline = dashline + '-' * sum[4]
        answerline = answerline + sum[3].rjust(sum[4],' ')

    line = topline + '\n' + secondline + '\n' + dashline
    if printanswer: line = line + '\n' + answerline

    return line
