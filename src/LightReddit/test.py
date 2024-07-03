# for testing db for now
from LightReddit import db
from LightReddit.models import Comment , Post
from faker import Faker
fake = Faker()


db.drop_all()
db.create_all()




def testPosts(postCount , commentsCount , replyCount ):
    for _ in range(postCount):
        newPost = Post(title = fake.name()  , content = fake.address())
        db.session.add(newPost)
        db.session.commit()
        for _ in range(commentsCount):
            commentNew = Comment(post_id = newPost.id , comment = fake.text() , reply_to_id = None)
            db.session.add(commentNew)
            db.session.commit()
            for _ in range(replyCount):
                reply = Comment(post_id = newPost.id , comment = fake.text() , reply_to_id = commentNew.id)
                db.session.add(reply)
                db.session.commit()
    
    db.session.commit()
        

def modelsToDBML():
    pass
                




