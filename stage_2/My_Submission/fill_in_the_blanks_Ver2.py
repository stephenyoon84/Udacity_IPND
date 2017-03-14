# Input your name.
# Load problem set
# Print out the problem set
# Problem subject - Python related.
# Solution set
    #Python - pp_sol
# User input for solution
# Chances = 2
# Result print out
name = []
pp_set = ['__1__','__2__','__3__','__4__']
pp_sol = ['object','language', 'class', 'particular']
test_set = 'Python is called an "__1__-oriented programming __2__." \
This means there is a construct in Python called a __3__ that lets you structure \
your software in a __4__ way. Using __3__es, you can add consistency to \
your programs so that they can be used in a cleaner way.'
chances = 4
total_score = 0

def player_name():
    player_name = raw_input('What is your name? ')
    name.append(player_name)

def wrong_answer(num_of_try, p_set, p_sol):
    global test_set
    if num_of_try >= 0 and num_of_try<2:
        print '\nWrong answer. You have '+ str(chances - num_of_try-1) + ' more chances. Please try again.\n'
    elif num_of_try == 2:
        print '\nWrong andwer. You have only one chance.'
        print 'Here is a hint - it start with '+ p_sol[0]
        print 'Pleae try again\n'
    else:
        print '\nWrong answer. Your chances are all gone. The answer is ' + p_sol
        print 'Study hard '+name[0]+'.'
        test_set = test_set.replace(p_set,p_sol)

def solution_input(t, p_set, p_sol):
    num_of_try = 0
    global test_set
    global total_score
    while num_of_try < chances:
        solution1_input = raw_input(test_set + '\n \nPlease fill in the blank ' + str(t) +': ')
        if solution1_input == p_sol:
            print '\nYour solution is correct ' + name[0]+'!\n'
            total_score += 25
            test_set = test_set.replace(p_set,p_sol)
            break
        else:
            wrong_answer(num_of_try, p_set, p_sol)
            num_of_try += 1

def problem_set(a, b):
    global total_score
    global test_set
    i = 0
    while i<4:
        solution_input(i+1, a[i], b[i])
        i += 1

def start_fbgame():

    player_name()
    print 'Hello!!' + name[0] + '.'
    print '\nThis is a python questions. You have '+ str(chances) + ' chances to answer each question.\n'
    problem_set(pp_set, pp_sol)
    print name[0] + ', your score is ' + str(total_score)

start_fbgame()
