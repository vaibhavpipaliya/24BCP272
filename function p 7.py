def ispalindrome(reverse_string):
    if reverse_string==string[::-1]:
        print('string is palindrome')
    else:
        print('string is not palindrome')


string=input("enter string : ")
ispalindrome(string)
