# Input your name.
# Select the level(easy, medium, hard):
# Load problem set
    # Python - 3 problem set
    # Math - 3 problem set
# Print out the problem set
# Problem subject - Python related or Calculate or etc.
# Solution set
# User input for solution
# Result print out
name = []
p_set = []
chances = 2

def player_name():
    player_name = raw_input('What are your name? ')
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
                print 'Study hard and try next tiem.'
            num_of_try += 1



def python_problem():
    print '\nThese are python questions. You have 2 chances to answer.'
    p_set.append('python')

def math_problem():
    print '\nThese are math questions. You have 2 chances to answer.'
    p_set.append('math')

def start_fbgame():

    # player_name()
    # print 'Hello!!' + name[0] + '.'
    choose_problem()
    if p_set[0] == 'python':
        python_set()
    else:
        math_set()

start_fbgame()
