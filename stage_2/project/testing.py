#import string
pp_set = ['Python is called an "__1__-oriented programming ___2____." \
This means there is a construct in Python called a __3__ that lets you structure \
your software in a particular way. Using __3__es, you can add consistency to \
your programs so that they can be used in a cleaner way.']
pp_sol = ['object','language', 'class']

print pp_set
pp_set[0] = pp_set[0].replace('__1__',pp_sol[0])

print pp_set
