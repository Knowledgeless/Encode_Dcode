from methods import Base64 as b64, MD5, text2bs64tomd5

if __name__ == "__main__":
    print("""
            Choose An Option
    ------------------------------
        1. Text => Base64
        2. Base64 => Text
        3. Text => md5 
        4. text => base64 => md5
        5. md5 => base64 => text

    """)

    choice = int(input("Option No: "))
    if choice == 1:
        user = input("Your Plain Text: ")
        en = b64.Encode(user)
        print('''
            Given Text:     {}
            Base64 Text:    {}
        '''.format(user, en._bs64()))

    elif choice == 2:
        user = input("Your BASE64 Text: ")
        dc = b64.Decode(user)
        print('''
            Base64 Text:     {}
            Plain Text:      {}
        '''.format(user, dc.base64()))

    elif choice == 3:
        user = input("Your Text: ")
        en = MD5.Encode(user)
        hash_name = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

        print('\n\t Given Text:  {}\n'.format(user))

        for i,j  in zip(en.md5(), hash_name):
            print("\t", j,":", i)
        print()

    elif choice == 4:
        user = input("Your Plain Text: ")
        en = text2bs64tomd5.MulitpleEncoding(user)
        hash_name = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

        print('\n\t Given Text:  {}\n'.format(user))

        for i,j  in zip(en._get_result__(), hash_name):
            print("\t", j,":", i)
        print()

    elif choice == 5:
        print("We are working on it...") 

    else: 
        print("Comming soon.. ")