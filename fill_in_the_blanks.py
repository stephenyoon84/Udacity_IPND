# Input your name.
# Select the level(easy, medium, hard):
# Load problem set
    # easy - 2 problem set
    # medium - 3 problem set
    # hard - 4 problem set
# Print out the problem set
# Problem subject - Python related or Calculate or etc.
# Solution set
# User input for solution
# Result print out

def choose_problem(level):
    if level == 'easy':
        return easy_problem()
    elif level == 'medium':
        return medium_problem()
    elif level == 'hard':
        return hard_problem()
    else:
        print 'Please select correct level.'




def easy_problem():
    print 'This problem set is easy.'

def medium_problem():
    print 'This problem set is medium.'

def hard_problem():
    print 'This problem set is hard.'

choose_problem('easy')
choose_problem('medium')
choose_problem('hard')
choose_problem('hello')    
