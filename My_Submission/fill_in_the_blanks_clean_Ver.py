# Input your name.
# Select the level(math, python):
# Load problem set
    # Python - 2 problem set - pp_set
    # Math - 2 problem set - mp_set
# Print out the problem set
# Problem subject - Python related or Calculate.
# Solution set
    #Python - pp_sol
    #Math - mp_sol
# User input for solution
# Chances = 2
# Result print out
name = []
p_set = []
pp_set = []
pp_sol = []
mp_set = ['1. 1 + 1 = ? ','2. 9 * 9 = ']
mp_sol = ['2','81']
chances = 2
total_score = 0

def player_name():
    player_name = raw_input('What is your name? ')
    name.append(player_name)

def choose_problem():
    level = raw_input('What do you want to solve today? - python or math : ')
    p_set = level
    if level == 'python':
        return python_problem()
    elif level == 'math':
        return math_problem()
    else:
        print 'Your input is not in the list. Please select correct problem set.'
        return choose_problem()

def python_set():
    print 'python'

def wrong_answer(num_of_try, sol):
    if num_of_try == 0:
        print 'Wrong answer. You have only one chance Please try again.'
    else:
        print 'Wrong answer. Your chances are all gone. The answer is ' + sol
        print 'Study hard '+name[0]+'.'

def math_set():
    num_of_try = 0
    global total_score
    while num_of_try < chances:
        math1_input = raw_input(mp_set[0])
        if math1_input == mp_sol[0]:
            print 'Your solution is correct ' + name[0]+'!'
            total_score += 50
            break
        else:
            wrong_answer(num_of_try, mp_sol[0])
            num_of_try += 1
    num_of_try = 0
    while num_of_try < chances:
        math2_input = raw_input(mp_set[1])
        if math2_input == mp_sol[1]:
            print 'Your solution is correct ' + name[0]+'!'
            total_score += 50
            break
        else:
            wrong_answer(num_of_try, mp_sol[1])
            num_of_try += 1

def python_problem():
    print '\nThese are python questions. You have 2 chances to answer each question.'
    p_set.append('python')

def math_problem():
    print '\nThese are math questions. You have 2 chances to answer each question.'
    p_set.append('math')

def start_fbgame():

    player_name()
    print 'Hello!!' + name[0] + '.'
    choose_problem()
    if p_set[0] == 'python':
        python_set()
    else:
        math_set()
    print name[0] + ', your score is ' + str(total_score)

start_fbgame()
