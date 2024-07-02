from LightReddit.models import Post,Comment

def GetAllReplies(post , comment):
    comment_id = None
    if comment:
        comment_id = comment.id 
    #gets all replies for a given post + comment pair
    return Comment.query.filter_by(post_id = post.id  , reply_to_id = comment_id)