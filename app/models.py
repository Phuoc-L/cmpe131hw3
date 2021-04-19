from app import db

'''
The data table for all of the users

columns
------
id : Integer
    A unique identifier that is given to each user
author : String
    The name of this user
'''
class User(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key = True)
    # author (string, unique, can't be null)
    author = db.Column(db.String, unique = True, nullable = False)
    # message (linkd to Messages table)
    message = db.relationship('Messages', backref = 'author', lazy = 'dynamic')
    
    def __repr__(self):
        return f'<User: {self.author}>'

'''
The message table for all posted messages

columns
------
id : Integer
    A unique identifier that is given to each message
message : String
    The content of this message
user_id : Integer
    The id of the user who posted this message
'''
class Messages(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key = True)
    # message (string, not unique, can't be null)
    message = db.Column(db.String, unique = False, nullable = False)
    # user_id link to id (int)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # write __repr__ that outputs
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message
    def __repr__(self):
        return f'<Message: {self.message}>'
