"""
Assignment Information. To find any of the following required program criteria, please search for the listed comment tag.
if statements - #$if-statements
loops - #$loops
arrays(lists) - #$arrays
files - #$files
functions - #$functions
"""

try:
    import hashlib
    import random
except ImportError:
    print("Error in imports.")

#$functions
def read_wordlist(filename, num_words):
    #reads wordlist, returns list of words to hash

    #open file, put words into lines
    #$files
    words = open("minirock.txt")
    words_rows = words.readlines()
    #$arrays
    list_word = []

    #separate whenever there is a new line
    #$loops
    for row in words_rows:
        row = row.strip("\n")
        list_word.append(row)

    #get a random number for num_words number of words
    #$arrays
    final_list = []
    #$loops
    for num in range(num_words):
        rand_num = random.randint(0, len(list_word) - 1)
        final_list.append(list_word[rand_num])

    return final_list

#$functions
def write_output(words, hashes):
    #open files
    #$files
    output = open("output.txt", "w")
    answers = open("answers.txt", "w")

    #write output
    #$loops
    for num in range(len(words)):
        # writes hashes
        output.write(str(hashes[num]) + "\n")
        # writes hashed:answer answerfile
        temp_words = str(words[num])
        temp_words = temp_words[2:-1]
        answers.write(str(hashes[num]) + ":" + str(temp_words) + "\n")

    #close files
    output.close()
    answers.close()
    print("Words written to output.txt and answers.txt")
    return

#$functions
def run_hashing(words, hashtype):

    #$arrays
    output = []
    #random selector, allows for easy extension
    #$if-statements
    if hashtype == 'random':
        hash_type_list = ['md5', 'sha1', 'sha256']
        hashtype = random.choice(hash_type_list)
    #$if-statements
    if hashtype == 'md5':
        #$loops
        for each in range(len(words)):
            #encodes in utf-8 to enable hashing
            words[each] = words[each].encode('utf-8')
            #hashes and puts in same index
            #hash needs to add the 'hexdigest' to be readable format
            output.append(hashlib.md5(words[each]).hexdigest())
    elif hashtype == 'sha1':
        #$loops
        for each in range(len(words)):
            #encodes in utf-8 to enable hashing
            words[each] = words[each].encode('utf-8')
            #hashes and puts in same index
            #hash needs to add the 'hexdigest' to be readable format
            output.append(hashlib.md5(words[each]).hexdigest())
    elif hashtype == 'sha256':
        #$loops
        for each in range(len(words)):
            #encodes in utf-8 to enable hashing
            words[each] = words[each].encode('utf-8')
            #hashes and puts in same index
            #hash needs to add the 'hexdigest' to be readable format
            output.append(hashlib.sha256(words[each]).hexdigest())
    return output

#$functions
def get_input():
    # $arrays
    to_hash = []
    print('"""""""""""""""""""""""""""""\n"     Welcome to Anticat    "\n"""""""""""""""""""""""""""""\n')

    #input for number of hashes
    print("Please enter the number of words you wish to hash: (1-100)")
    valid = False

    #input validator
    #$loops
    while valid == False:
        try:
            num_words = int(input())
        except ValueError:
            print("Error in input, please enter a number (1-100)")
        #$if-statements
        if num_words < 1 or num_words > 100:
            print("Error in input, please enter a number (1-100)")
        else:
            print("You have entered " + str(num_words) + " words.")
            print("Is this correct? (y/n)")
            answer_check = input()
            #$if-statements
            if answer_check == "y":
                valid = True
            else:
                print("Please enter a number (1-100)")
    to_hash.append(num_words)

    #input for number of hashes
    print("\n Please enter the number for the type of hashes you wish to generate: (1-4)")
    print("1) MD5")
    print("2) SHA1")
    print("3) SHA256")
    print("4) Random")
    valid = False

    #input validator
    #$loops
    while valid == False:
        try:
            hash_type = int(input())
        except ValueError:
            print("Error in input, the number for the type of hashes you wish to generate: (1-4)")
        #$if-statements
        if hash_type < 1 or hash_type > 4:
            print("Error in input, the number for the type of hashes you wish to generate: (1-4)")
        elif hash_type == 1:
            print("You have selected MD5")
            print("Is this correct? (y/n)")
            answer_check = input()
            #$if-statements
            if answer_check == "y":
                hash_type_selected = 'md5'
                valid = True
            else:
                print("Please the number for the type of hashes you wish to generate: (1-4)")
        elif hash_type == 2:
            print("You have selected SHA1")
            print("Is this correct? (y/n)")
            answer_check = input()
            #$if-statements
            if answer_check == "y":
                hash_type_selected = 'sha1'
                valid = True
            else:
                print("Please the number for the type of hashes you wish to generate: (1-4)")
        elif hash_type == 3:
            print("You have selected SHA256")
            print("Is this correct? (y/n)")
            answer_check = input()
            #$if-statements
            if answer_check == "y":
                hash_type_selected = 'sha256'
                valid = True
            else:
                print("Please the number for the type of hashes you wish to generate: (1-4)")
        elif hash_type == 4:
            print("You have selected Random")
            print("Is this correct? (y/n)")
            answer_check = input()
            #$if-statements
            if answer_check == "y":
                hash_type_selected = 'random'
                valid = True
            else:
                print("Please the number for the type of hashes you wish to generate: (1-4)")
    to_hash.append(hash_type_selected)
    return to_hash

#get user input, 2-item list, first item is number of hashes, second is type of hashes
#future input will include type of wordlist
user_input = get_input()

#read wordlist, currently only 'default' testing minilist
#second input is number hashes
raw_passwords = read_wordlist("minirock.txt", user_input[0])

#hash the passwords, type dependent on user input
hashed_passwords = run_hashing(raw_passwords, user_input[1])

#write to file
write_output(raw_passwords, hashed_passwords)