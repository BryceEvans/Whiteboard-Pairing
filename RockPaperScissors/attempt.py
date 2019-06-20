def rps(n):
    # set up empty array
    finalResult = []
    # set up options
    options = ['rock', 'paper', 'scissors']

    # define recursive function
    def recursive_rps(x, result):
        if x == 0:
            finalResult.append(result)
            return
        else:
            for opt in options:
                # result.append(opt)
                recursive_rps(x-1, result + [opt])

    recursive_rps(n, [])

    return finalResult

print(len(rps(2)))
print(rps(2))

