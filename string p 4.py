string1=input("enter : ")
string2=input("enter : ")
newstring = " "
if string2 in string1:
    newstring=string1.replace(string2,'')
    print(newstring)
