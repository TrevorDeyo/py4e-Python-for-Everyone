while True: # prompts user for file name and if it fails says invalid input
    try:
        fname = input('Enter file name: ')
        fh = open(fname)
        break
    except:
        print('Invalid Input')

lst = [] # creates empty list

for line in fh: # goes line by line
    words = line.split() # splits the line into words
    for word in words: # goes word by word
       if word not in lst: # checks to see if word in lst
           lst.append(word) # if not then adds it

lst.sort() # sorts the lst
print(lst) # prints the lst