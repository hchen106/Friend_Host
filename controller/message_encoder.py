import sys

class message:

    def __init__(self):
        self.username = " "
        self.message = b' '
        self.string_message = " "
    
    def encode(self,n,mess):
        self.username = n
        self.string_message = mess
        m = self.username + ' ' + self.string_message
        self.message = bytes(m, 'utf-8')
        return self.message
    
    def decode(self,mess):
        m = mess.decode('utf-8')
        lst = m.split(' ',1)
        self.username = lst[0]
        self.string_message = lst[1]
    
    def get_message(self):
        return self.string_message
    
    def get_username(self):
        return self.username
        