from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import getQuotes
from .forms import ReviewForm,UpdateProfile,PostForm,CommentForm,UpvoteForm,Downvote
from ..models import Review,User,PhotoProfile,Post,Comment,Upvote,Downvote
from flask_login import login_required,current_user
from .. import db,photos
import requests

import markdown2


# Views
@main.route('/')
def index():
     post = Post.query.all()
     quotes = getQuotes()


     return render_template('index.html',quotes=quotes,post = post)

@main.route('/posts/new/', methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    
    if form.validate_on_submit():
        description = form.description.data
        author = form.author.data
        user_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_post = Post(user_id =current_user._get_current_object().id, author = author,description=description,category=category)
        db.session.add(new_post)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('posts.html',form=form)



# @main.route('/comment/new/<int:post_id>', methods = ['GET','POST'])
# @login_required
# def new_comment(post_id):
#     form = CommentForm()
#     post=Post.query.get(post_id)
#     if form.validate_on_submit():
#         description = form.description.data
       
#         new_comment = Comment(description = description, user_id = current_user._get_current_object().id, post_id = post_id)
#         db.session.add(new_comment)
#         db.session.commit()


#         return redirect(url_for('main.index', post_id= post_id))

#     all_comments = Comment.query.filter_by(post_id = post_id).all()
#     return render_template('comments.html', form = form, comment = all_comments, post = post )


@main.route('/post/<int:post_id>',methods= ['POST','GET'])

def comment(post_id):
    if request.method == 'POST':
        form = request.form
        name = form.get("name")
        description = form.get("description")
       
        
        if  name==None or description==None:
            error = "Comment needs name and description"
            return render_template('navbar.html', error=error)
        else:
            comment = Comment( name=name,description=description,post_id= post_id)
            comment.save_comment()
            comments= Comment.query.filter_by(post_id=post_id).all()
            post = Post.query.get_or_404(post_id)
    return render_template('comments.html') 
    
@main.route('/post/upvote/<int:post_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(post_id):
    post = Post.query.get(post_id)
    user = current_user
    post_upvotes = Upvote.query.filter_by(post_id= post_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.post_id==post_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(post_id=post_id)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))




@main.route('/post/downvote/<int:post_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(post_id):
    post = Post.query.get(post_id)
    user = current_user
    post_downvotes = Downvote.query.filter_by(post_id= post_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.post_id==post_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvote(post_id=post_id)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))

@main.route('/post/<int:id>')
def post(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    post = get_posts(id)
    # title = f'{movie.title}'
    reviews = Review.get_reviews(post.id)

    return render_template('blog.html',title = title,movie = movie,reviews = reviews)


@main.route('/reviews/<int:id>')
def post_reviews(id):
    post = get_posts(id)

    reviews = Review.get_reviews(id)
    title = f'All reviews for {post.author}'
    return render_template('post_reviews.html',author = author,reviews=reviews)


@main.route('/review/<int:id>')
def single_review(id):
    review=Review.query.get(id)
    format_review = markdown2.markdown(review.post_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)




@main.route('/post/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):

    form = ReviewForm()

    post = get_posts(id)

    if form.validate_on_submit():
        author = form.author.data
        review = form.review.data

        new_review = Review(post_id=post.id,post_author=author,post_review=review,user=current_user)

        new_review.save_review()

        return redirect(url_for('.post',id = post.id ))

    author = f'{post.author} review'
    return render_template('new_review.html',author = author, review_form=form, post=post)

@main.route('/user/<uname>')

def profile(uname):
    user = User.query.filter_by(username = uname).first()
    get_posts = Post.query.filter_by(user_id = current_user.id).all()
    print(get_posts)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, posts = get_posts)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():

        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))