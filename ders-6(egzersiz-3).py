def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if(first(word)!=last(word)):
        return False
    else:
        if(len(word)>2):
            if(is_palindrome(middle(word))==True):
                return True
            else:
                return False
        else:
            return True

print(is_palindrome("ahmet"))