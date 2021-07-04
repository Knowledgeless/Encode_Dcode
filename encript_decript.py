import hashlib
from methods import base64 as b64, md5


if __name__ == "__main__":
    print("""
            Chose An Option
    ------------------------------
        1. Text => Base64
        2. Base64 => Text
        3. Text => md5
        4. md5 => Text 
    """)

    choise = int(input("Option No: "))
    if choise == 1:
        user = input("Your Text: ")
        en = b64.Encode(user)
        print('''
            Given Text:     {}
            Base64 Text:    {}
        '''.format(user, en._bs64()))

    elif choise == 2:
        user = input("Your Text: ")
        dc = b64.Decode(user)
        print('''
            Given Text:     {}
            Base64 Text:    {}
        '''.format(user, dc.base64()))

    elif choise == 3:
        user = input("Your Text: ")
        en = md5.Encode(user)
        hash_name = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

        print('\n\t Given Text:  {}\n'.format(user))

        for i,j  in zip(en.md5(), hash_name):
            print("\t", j,":", i)
        print()
    else: 
        print("Comming soon.. ")