'''
This class handles the comment as a reply
'''
class Reply(object):

    def __init__(self,body,id,reply_id):
        self.reply_id = reply_id
        self.body = body
        self.id = id
    def serialize_reply(self):
        '''return dict'''
        return dict(
        reply_id=self.reply_id,
        body=self.body,
        id =self.id
        )





