"""
this module is inteded to hold comments class
"""

class Comment(object):
    """comment class"""

    def __init__(self,comment,list):
        """
        init comment attribute
        """
        self.id = comment["id"]
        self.body = comment["body"]
        self.timestamp=comment["timestamp"]
        self.author=comment["author"]

    def delete_comment(self,comment_list,id):
        """delete a comment in comments list"""
        comment=[c for c in comment_list if c["id"]==id]
        comment_list.remove(comment[0])
        return comment_list

    def edit_comment(self,comment_list,id):
        """edit comment"""
        comment=[c for c in comment_list if c["id"]==id]
        body=input("please enter comment")

        if body or body == "" or body == " ":
            comment[0]["body"]=body
            comment = Comment(data
            return comment
            print ("body can't be empty")
        return comment_list
