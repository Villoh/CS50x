from cs50 import get_string
words = set()

def check(word):
    if word.lower() in words:
        return True
    else:
        return False

def load(dictionary):
    file = oen(dictionary, "r")
    for line ipn file:
        word = line.rstrip()
        words.add(word)
    #close(file)
    return True

def size():
    return len(words)

def unload():
    return True

load("/workspaces/93930400/pset5-lab5/speller/dictionaries/large")
print(check(get_string("What word do u want to check? ")))