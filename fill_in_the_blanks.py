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
p_set = []
def choose_problem():
    level = raw_input('Please select the problem category - python or math : ')
    p_set = level
    if level == 'python':
        return python_problem()
    elif level == 'math':
        return math_problem()
    else:
        print 'Please select correct level.'

def python_problem():
    print '\nThese are python questions.'
    p_set.append('python')

def math_problem():
    print '\nThese are math questions.'
    p_set.append('math')

def start_fbgame():
    choose_problem()
    print p_set[0]

start_fbgame()
