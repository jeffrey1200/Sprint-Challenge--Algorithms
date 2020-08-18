'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    counter = 0
    if len(word) == 0 or counter + 1 == len(word):
        return 0
    elif word[counter] == "t" and word[counter + 1] == "h":
        return 1 + count_th(word[counter + 1:])
    else:
        return 0 + count_th(word[counter + 1:])
    
    


