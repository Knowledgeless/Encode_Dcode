import Base64 as b64

class MultipleDecoding:
    def __init__(self, user):
        self.user = user
    
    def _get_text__(self):
        byte_text = b64.Decode(self.user)
        decoded_bs64 = byte_text.base64()
        encoded_bs64 = b64.Decode(decoded_bs64)
        encoded_text = encoded_bs64.base64()
        return encoded_text
        

if __name__ == "__main__":
    user = "252aec44c31ec6159cc966ed42a76e1a"
    reverse = MultipleDecoding(user)
    print(reverse._get_text__())