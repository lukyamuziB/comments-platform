class Db:
    def __init__(self):
        self.comments = []
        self.permissions = []
        self.users = []
        self.replies = []

    def filter_user_by(self, email):
        # filter by instance by id
        item_ = next((item for item in self.users if item.get('email') == email), {})
        return item_

    def create_users(self, user):
        self.users.append(user)

    def create_permissions(self, perm):
        self.permissions.append(perm)

    def create_comments(self, comment):
        self.comments.append(comment)

    def create_reply(self, reply):
        self.replies.append(reply)

    def get_comments(self):
        return self.comments

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return repr(self.__dict__)