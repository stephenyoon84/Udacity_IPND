chances = 2

def math_set():
    math1_solution = '2'
    num_of_try = 0
    while num_of_try < chances:
        math1_input = raw_input('1. 1 + 1 = ? ')
        if math1_input == math1_solution:
            print 'Your solution is correct.'
            break
        else:
            if num_of_try == 0:
                print 'Wrong answer. You have only one chance Please try again.'
            else:
                print 'Wrong answer. Your chances are all gone. The answer is ' + math1_solution
            num_of_try += 1

math_set()
