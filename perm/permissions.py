class Permission(object):
    """class Permission."""
    def __init__(self, perm_name,action):
        '''init permission'''
        self.name = perm_name
        self.actions = action
    def serialize_perm(self):
        '''return dict'''
        return dict(
        permission=self.perm_name,
        action=self.action
        )

perm = Permission('add', 'delete')
