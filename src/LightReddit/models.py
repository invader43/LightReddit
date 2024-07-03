from LightReddit import db
from flask_login import UserMixin
from datetime import datetime



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(160), nullable=False)


# class Media(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # post_id

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #poster_id
    #media
    title = db.Column(db.Text , nullable = False)
    content = db.Column(db.Text , nullable = False)
    created_at = db.Column(db.DateTime , nullable = False , default = datetime.utcnow )
    comments = db.relationship('Comment', backref='post',lazy=True)

    def __repr__(self) :
        return f"Post(' {self.title} {self.content} {self.created_at}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # commenter_id = ?
    post_id = db.Column(db.Integer , db.ForeignKey('post.id') , nullable = False)
    reply_to_id = db.Column(db.Integer, db.ForeignKey('comment.id'))  
    # above [if null , meaning its a reply to base post]
    comment = db.Column(db.Text , nullable = False)
    created_at = db.Column(db.DateTime , nullable = False , default = datetime.utcnow )

    #how our object is printed 
    def __repr__(self):
        return f"Comment('{self.post_id}','{self.comment}' , '{self.reply_to_id}')"

# class Subreddit(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name =  db.Column(db.String(80), unique=True, nullable=False)
#     # owner_id = 
#     created_at = db.Column(db.DateTime , nullable = False , default = datetime.utcnow )
#     posts = db.relationship('Post', backref='subreddit', lazy=True)

