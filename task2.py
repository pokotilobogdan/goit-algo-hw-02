from collections import deque

def is_palindrome(string):
    
    dq = deque()
    
    # adding alpha-symbols of the string to the deque
    for char in string:
        if char.isalpha():
            dq.append(char.lower())

    # checking if the string has equal characters on both end
    while len(dq) > 2:
        if dq.popleft() == dq.pop():        
                continue
        else:
            print("That's not a palindrome\n")
            return False
    
    # in case of ODD length of the string
    if len(dq) == 1:
        print("That's a palindrome\n")
        return True

    # in case of EVEN length of the string
    if len(dq) == 2:
        if dq[0] == dq[1]:
            print("That's a palindrome\n")
            return True
        else:
            print("That's not a palindrome\n")
            return False


while True:
    string = input("Type a string: ")
    if string in ['exit', 'close', 'quit']:
        break
    is_palindrome(string)