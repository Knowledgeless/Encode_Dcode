from . import Base64 as b64, MD5

class MulitpleEncoding:
    def __init__(self, user):
        self.user = user
    
    def _get_result__(self):
        encoded_bs64 = b64.Encode(self.user)
        bs_text = encoded_bs64._bs64()
        encoded_md5 = MD5.Encode(bs_text)
        return encoded_md5.md5()

