def create():
    name=input(" enter name : ")
    phone=input("enter the phone no : ")
    email=input("enter email:")

    vcard=f"""BEGIN:VCARD
VERSION:4.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""
    FILE_NAME=input("enter file name : ")
    with open (FILE_NAME,'+a')as vcard_file:
        vcard_file.write(vcard)

        print(f"saved")

        
create()
