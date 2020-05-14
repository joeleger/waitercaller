
import hashlib
import os
import base64


class PasswordHelper:

    def get_hash(self, plain):
        password_encoded = plain.encode('utf-8')
        hash = hashlib.sha512(password_encoded).hexdigest()
        return hash

        # return hashlib.sha512(plain).encode('utf-8').hexdigest()

    def get_salt(self):
        return base64.b64encode(os.urandom(20)).decode('utf-8')

    def validate_password(self, plain, salt, expected):
        return self.get_hash(plain + salt) == expected
