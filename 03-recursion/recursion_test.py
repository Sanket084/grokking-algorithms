# tried recursion program for countdown !not in book

def countdown(i):
    print(i)
    if i <= 0:              # base case
        return
    else:
        countdown(i - 1)    # recursive case

countdown(5)