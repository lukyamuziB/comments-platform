"""
this module is inteded to hold comments class
"""

class Comment(object):
    """comment class"""

    def __init__(self,comment):
        """
        init comment attribute
        """
        self.id = comment["id"]
        self.body = comment["body"]
        self.timestamp=comment["timestamp"]
        self.author=comment["author"]
