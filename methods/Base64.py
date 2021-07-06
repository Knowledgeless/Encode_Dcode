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
        encoded_text = self.encoded_text.encode("ascii") #converting byte 
        byte = base64.b64decode(encoded_text)   #converting into plain text 
        decoded_message = str(byte)
        return decoded_message[2:-1]