import base64
class Encode:
    def __init__(self, text):
        self.text = text.encode("ascii")    #converting text to byte

    def _bs64(self):
        byte = base64.b64encode(self.text)  #converting into base64
        st = str(byte)
        return st[2:-1]

class Decode(Encode):
    def __init__(self, text):
        self.encoded_text = text
        
    def base64(self):
        # encoded_text = self._bs64()
        encoded_text = self.encoded_text.encode("ascii") #converting byte 
        byte = base64.b64decode(encoded_text)   #converting into plain text 
        decoded_message = str(byte)
        return decoded_message[2:-1]

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
        en = Encode(user)
        print('''
            Given Text:     {}
            Base64 Text:    {}
        '''.format(user, en._bs64()))
    elif choise == 2:
        user = input("Your Text: ")
        dc = Decode(user)
        print('''
            Given Text:     {}
            Base64 Text:    {}
        '''.format(user, dc.base64()))
    else: 
        print("Comming soon.. ")