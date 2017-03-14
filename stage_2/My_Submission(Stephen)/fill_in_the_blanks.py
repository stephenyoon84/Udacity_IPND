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
pp_set = ['Python is well suited to ______ orientated programming in that it \
allows the definition of classes along with composition and inheritance.',
'There is a construct in Python called a _____ that lets you structure your \
software in a particular way. Using _____es, you can add consistency to your \
programs so that they can be used in a cleaner way.']
pp_sol = ['object','class']
mp_set = ['1. 1 + 1 = _ ','2. 9 * 9 = __']
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

# def python_set():
#     num_of_try = 0
#     global total_score
#     while num_of_try < chances:
#         python1_input = raw_input(pp_set[0]+ '\nPlease fill in the blank : ')
#         if python1_input == pp_sol[0]:
#             print 'Your solution is correct ' + name[0]+'!'
#             total_score += 50
#             break
#         else:
#             wrong_answer(num_of_try, pp_sol[0])
#             num_of_try += 1
#     num_of_try = 0
#     while num_of_try < chances:
#         python2_input = raw_input(pp_set[1]+ '\nPlease fill in the blank : ')
#         if python2_input == pp_sol[1]:
#             print 'Your solution is correct ' + name[0]+'!'
#             total_score += 50
#             break
#         else:
#             wrong_answer(num_of_try, pp_sol[1])
#             num_of_try += 1

def problem_set(a, b, c, d):
    num_of_try = 0
    global total_score
    while num_of_try < chances:
        solution1_input = raw_input( a + '\nPlease fill in the blank : ')
        if solution1_input == b:
            print 'Your solution is correct ' + name[0]+'!'
            total_score += 50
            break
        else:
            wrong_answer(num_of_try, b)
            num_of_try += 1
    num_of_try = 0
    while num_of_try < chances:
        solution2_input = raw_input(c+ '\nPlease fill in the blank : ')
        if solution2_input == d:
            print 'Your solution is correct ' + name[0]+'!'
            total_score += 50
            break
        else:
            wrong_answer(num_of_try, d)
            num_of_try += 1

# def wrong_answer(num_of_try, sol):
#     if num_of_try == 0:
#         print 'Wrong answer. You have only one chance Please try again.'
#     else:
#         print 'Wrong answer. Your chances are all gone. The answer is ' + sol#math1_solution
#         print 'Study hard '+name[0]+'.'

# def math_set():
#     #math1_solution = '2'
#     #math2_solution = '81'
#     num_of_try = 0
#     global total_score
#     while num_of_try < chances:
#         #math1_input = raw_input('1. 1 + 1 = ? ')
#         math1_input = raw_input(mp_set[0])
#         if math1_input == mp_sol[0]:#math1_solution:
#             print 'Your solution is correct ' + name[0]+'!'
#             total_score += 50
#             break
#         else:
#             #wrong_answer(num_of_try, mp_sol[0])
#             if num_of_try == 0:
#                 print 'Wrong answer. You have only one chance Please try again.'
#             else:
#                 print 'Wrong answer. Your chances are all gone. The answer is ' + mp_sol[0]#math1_solution
#                 print 'Study hard '+name[0]+'.'
#             num_of_try += 1
#     num_of_try = 0
#     while num_of_try < chances:
#         #math2_input = raw_input('2. 9 * 9 = ')
#         math2_input = raw_input(mp_set[1])
#         if math2_input == mp_sol[1]:#math2_solution:
#             print 'Your solution is correct ' + name[0]+'!'
#             total_score += 50
#             break
#         else:
#             #wrong_answer(num_of_try, mp_sol[1])
#             if num_of_try == 0:
#                 print 'Wrong answer. You have only one chance Please try again.'
#             else:
#                 print 'Wrong answer. Your chances are all gone. The answer is ' + mp_sol[1]#math2_solution
#                 print 'Study hard '+name[0]+'.'
#             num_of_try += 1


def python_problem():
    print '\nThese are python questions. You have 2 chances to answer each question.'
    p_set.append('python')

def math_problem():
    print '\nThese are math questions. You have 2 chances to answer each question.'
    p_set.append('math')

def start_fbgame():
    #total_score = 0

    player_name()
    print 'Hello!!' + name[0] + '.'
    choose_problem()
    if p_set[0] == 'python':
        problem_set(pp_set[0],pp_sol[0],pp_set[1],pp_sol[1])
    else:
        problem_set(mp_set[0],mp_sol[0],mp_set[1],mp_sol[1])

    print name[0] + ', your score is ' + str(total_score)

start_fbgame()
