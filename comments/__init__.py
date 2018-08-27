"""get user comment"""
import datetime
from comments import Comment
def create_comment(author,comment_list):
    """create comment instance"""
    body=input("please add your comment")
    timestamp=datetime.now()
    if comment_list:
        id=comment_list[-1]+1
    id=1
    timestamp=datetime.now()
    if body or body == "" or body == " ":
        data={}
        data["id"]=id
        data["timestamp"]=timestamp
        data["author"]=author
        data["body"]=body
        comment = Comment(data
        return comment
    print ("body can't be empty")
