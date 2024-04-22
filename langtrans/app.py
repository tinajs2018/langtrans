#import and create a flask application
from flask import Flask,render_template,request
app =Flask(__name__)

#define the route for the home page

@app.route('/')
def index():
    # Code to retrieve posts from database (explained later)
    posts = []  # Placeholder for list of posts
    return render_template('index.html', posts=posts)

#notice the route will display all the list of punlished post from the homepage
#show invidual  post
# @app.route('post/<title>')
# def show_post(title):
#     post ={}
#     comments=[]
#     return render_template('post.html',post=post,comments=comments)
def show_post(title):
    # Code to retrieve post details by title (explained later)
    post = {}  # Placeholder for post object
    comments = []  # Placeholder for list of comments
    return render_template('post.html', post=post, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)