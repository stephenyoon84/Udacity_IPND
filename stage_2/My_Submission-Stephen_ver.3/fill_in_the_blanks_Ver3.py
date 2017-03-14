blank_set = ['__1__','__2__','__3__','__4__']
game_data = {
    'easy' : {
        'quiz': 'Python can store values in __1__, for use at a later time.\
You can change them at __2__. You can put in not only __3__, but also text.\
 A __1__ that holds text is called a __4__. ',
        'answer': ['variable','anytime','number','string']
        },
    'medium' : {
        'quiz': 'A function is a block of organized, __1__ code that is used \
to perform a single, related action. Functions provide better modularity \
for your __2__ and a high degree of code reusing. \
As you already know, Python gives you many __3__-in functions like print(), \
etc. but you can also create your own functions. These functions are called \
__4__-defined functions.',
        'answer': ['reusable','application','built','user']
        },
    'hard' : {
        'quiz': 'Python is called an "__1__-oriented programming __2__." \
This means there is a construct in Python called a __3__ that lets you structure \
your software in a __4__ way. Using __3__es, you can add consistency to \
your programs so that they can be used in a cleaner way.',
        'answer': ['object','language', 'class', 'particular']
        }
    }
chances = 4

def player_name():
    ''' Ask player's name.
        Set player's name in user_name
    '''
    global user_name
    user_name = raw_input('What is your name? ')
    print 'Hello!!' + user_name + '.'

def wrong_answer(num_of_try, blank_set, blank_sol, test_set):
    ''' Indicate how many chances left
        Inputs  : number of try, blank_set, blank_sol, test_set
        Outputs : Show how many chances left
    '''
    if num_of_try >= 0 and num_of_try < chances-2:
        print '\nWrong answer. You have '+ str(chances - num_of_try-1) + ' more chances. Please try again.\n'
    elif num_of_try == chances-2:
        print '\nWrong andwer. You have only one chance.'
        print 'Here is a hint - it start with '+ blank_sol[0] # the first character of solution
        print 'Pleae try again\n'
    else:
        print '\nWrong answer. Your chances are all gone. The answer is ' + blank_sol
        print 'Study hard '+user_name+'.'
        test_set = test_set.replace(blank_set,blank_sol)


def problem_set(blank_set, blank_sol, test_set):
    ''' Show problem set and ask the answer. After the quiz, score the player
        Inputs  : blank_set, blank_sol, test_set
        Outputs : total score
    '''
    i = 0
    total_score = 0
    socre_for_answer = 25
    while i < chances:
        num_of_try = 0
        while num_of_try < chances:
            solution1_input = raw_input(test_set + '\n \nPlease fill in the blank ' + str(i+1) +': ')
            if solution1_input == blank_sol[i]:
                print '\nYour solution is correct ' + user_name +'!\n'
                total_score += socre_for_answer
                test_set = test_set.replace(blank_set[i],blank_sol[i])
                break
            else:
                wrong_answer(num_of_try, blank_set[i], blank_sol[i], test_set)
                num_of_try += 1
        i += 1
    print user_name + ', your score is ' + str(total_score)

def choose_level():
    ''' Select level - easy, medium, hard
        Inputs  : take no Inputs
        Outputs : problem_set function
    '''
    level = raw_input('What do you want to solve today? - easy, medium, hard : ')
    if level == 'easy' or level=='medium' or level=='hard':
        print '\nThis is a '+level+ ' python questions. You have \
'+ str(chances) + ' chances to answer each question.\n'
        return problem_set(blank_set, game_data[level]['answer'], game_data[level]['quiz'])
    else:
        print 'Your input is not in the list. Please select correct problem set.'
        return choose_level()

def start_fbgame():
    # start game
    player_name()
    choose_level()

start_fbgame()
