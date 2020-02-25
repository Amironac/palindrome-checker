

def palindrome(word):

    #If you want to put your own word
    #
    # n = input()
    # word = n

    word = "madam"

    original = ""
    copy = ""

    for i in range(0,len(word)):
        copy += word[i]

    for j in range(len(word)-1, -1,-1):
        original += word[j]


    if original == copy:
        return True

    return False

print(palindrome(str()))
