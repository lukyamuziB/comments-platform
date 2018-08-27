class User(object):
    def __init__(self, data={}):
        self.username = data.get('username')
        self.usermail = data.get('usermail')
        self.userpassword = data.get("userpassword")
        self.permission = data.get('permission')



