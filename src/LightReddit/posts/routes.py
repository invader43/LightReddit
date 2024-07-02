from flask import render_template,request,Blueprint
from LightReddit.models import Post
from LightReddit.posts.utils import GetAllReplies
posts = Blueprint('posts', __name__ )

@posts.route('/posts')
def home():
    posts = Post.query.all()
    
    return render_template('posts.html', posts = posts , getAllRepliesFunc = GetAllReplies )
