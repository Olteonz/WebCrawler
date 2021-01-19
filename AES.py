#-*- coding: utf-8 -*-

# Python 3.4
# author: http://blog.dokenzy.com/
# date: 2015. 4. 8

# References
# http://www.imcore.net/encrypt-decrypt-aes256-c-objective-ios-iphone-ipad-php-java-android-perl-javascript/
# http://stackoverflow.com/questions/12562021/aes-decryption-padding-with-pkcs5-python
# http://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
# http://www.di-mgt.com.au/cryptopad.html
# https://github.com/dlitz/pycrypto

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]


class AESCipher(object):
    """
    https://github.com/dlitz/pycrypto
    """

    def __init__(self, key):
        self.key = key.encode("utf8")
        #self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, message):
        """
        It is assumed that you use Python 3.0+
        , so plaintext's type must be str type(== unicode).
        """
        message = message.encode()
        raw = pad(message)
        cipher = AES.new(self.key, AES.MODE_ECB)
        enc = cipher.encrypt(raw)
        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        dec = cipher.decrypt(enc)
        return unpad(dec).decode('utf-8')


