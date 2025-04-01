lst=["madam","python","malayalam",12321]
palindrome=[str(name) for name in lst if str(name)==str(name)[::-1]]

print(palindrome)
