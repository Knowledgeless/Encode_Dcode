import hashlib

class Encode:
    def __init__(self, text):
        self.text = text.encode()  

    def md5(self):
        _md5 = hashlib.md5()
        sha1 = hashlib.sha1()  
        sha224 = hashlib.sha224()  
        sha256 = hashlib.sha256()          
        sha384 = hashlib.sha384()  
        sha512 = hashlib.sha512()  

        _md5.update(self.text)  #converting into md5
        sha1.update(self.text)   #converting into sha1
        sha224.update(self.text)  #converting into sha224
        sha256.update(self.text)  #converting into sha256        
        sha384.update(self.text)  #converting into sha384
        sha512.update(self.text)  #converting into sha512

        return _md5.hexdigest(), sha1.hexdigest(), sha224.hexdigest(), sha256.hexdigest(), sha384.hexdigest(), sha512.hexdigest()
