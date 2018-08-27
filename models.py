class Db:
    def __init__(self, data={}):
        self.comments = data.get('comments')
        self.permissions = data.get('permissions')
        self.users = data.get('users')

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return repr(self.__dict__)