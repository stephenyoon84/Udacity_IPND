# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    replaced = []
    # your code here
    ml = ml_string.split()
    replace_input = 'corgi'
    #print ml
    for i in ml:
        if word_in_pos(i,parts_of_speech) in parts_of_speech:
            #i[0:len(word_in_pos(i,parts_of_speech))] =replace_input
            #i = replace_input
            i=i.replace(i[0:len(word_in_pos(i,parts_of_speech))], replace_input)
            #print i
            replaced += [i]
        else:
            replaced += [i]



    replaced = ' '.join(replaced)
    return replaced
print play_game(test_string, parts_of_speech)
