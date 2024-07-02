from flask import render_template,request,Blueprint,jsonify
from LightReddit import db
from LightReddit.models import Post
from LightReddit.posts.utils import GetAllReplies
posts = Blueprint('posts', __name__ )

@posts.route('/posts' , methods = ["GET","POST"])
def posts_html():
    posts = Post.query.all()
    # jsonify(posts)
    return render_template("posts.html" , posts = posts, getAllRepliesFunc = GetAllReplies)


@posts.route('/api/posts' , methods = ["GET","POST"])
def posts_api():
    posts = Post.query.all()
    postlist = [{"title" : post.title , "content" : post.content} for post in posts]
    return jsonify({"posts" : postlist})



'''
example json file would be

{
    "posts" : [
    {"title" : title , "content" : content} ,
    {"title" : title , "content" : content} , 
    {"title" : title , "content" : content}
    ]

}


'''