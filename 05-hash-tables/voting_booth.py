voted = {}

def check_voter(name):
    if voted.get(name):
        print ("kick them out")
    else:
        voted[name] = True
        print ("let them vote")

print (voted)

check_voter("tom")
check_voter("mike")
check_voter("mike")

print (voted)