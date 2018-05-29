from flask import render_template, request, redirect, url_for, abort  
from . import main  
from .forms import CommentsForm, UpdateProfile, PostForm, SubscriptionForm
from ..models import Comment, BlogPost, Admin
from flask_login import login_required, current_user
from .. import db
import markdown2
from ..auth import forms


@main.route('/')
@main.route('/index/')
def index():
    form = SubscriptionForm()
    title = 'Blender Fender - HOME'
    posts= BlogPost.get_all_posts()
    
    if form.validate_on_submit():
        subscriber = Subscriber(email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()

        email_message('Succesfully registered to Blender Fender','email/subscribe_email', subscriber.email, subscriber=subscriber)
        flash('Nice! Welcome to the clan! A confirmation email has been sent to you')
        return redirect(url_for("main.index"))
    return render_template('index.html', title=title, subscribe_form = form, post=posts )



@main.route('/main/<int:id>')
def delete(id):
    post = BlogPost.query.filter_by(id=id).first()
    BlogPost.delete_post(post)
    return redirect(url_for('main.admin'))



@main.route('/main/admin/',methods = ["GET","POST"])
@login_required
def admin():
    form = PostForm()
    title = 'Blender Fender - Admin page'
    search_post = request.args.get('pitch_query')
    posts= BlogPost.get_all_posts()
    

    
    if form.validate_on_submit():
        post = form.content.data
        category_id = form.category_id.data
        mytitle=form.title.data
        description = form.description.data
        new_post = BlogPost(post = post, category_id = category_id, post_title = mytitle, description = description)
        new_post.save_post()
        print(new_post.post)
        print(new_post.post_title)
        print(new_post.description)



    return render_template('admin_page.html', title = title, post = posts, new_posts_form = form)


@main.route('/main/tutorials/', methods = ["GET","POST"])
def tutorials():
    title = 'Blender Fender - Tutorials'
    posts= BlogPost.get_all_posts()
    form = CommentsForm()
    comments = Comment.get_comments()

    if form.validate_on_submit():
        new_comment = Comment(comment=form.comment.data)
        new_comment.save_comment()
        return redirect(url_for('main.tutorials'))

    return render_template('tutorial.html',title= title ,post = posts, comment_form=form, comments = comments, id=id)




#this section consist of the category root functions

@main.route('/introduction/posts/')
def introduction():
    posts = BlogPost.get_all_posts()
    title = 'Introduction to Blender'  
    return render_template('creative_ideas.html', title = title, pitches= pitches )

@main.route('/intermediary/posts/')
def intermediary():

    title = 'Intermediary Blender tutorials'

    posts = BlogPost.get_all_posts()

    return render_template('pick_up_lines.html', title = title, pitches= pitches )

@main.route('/advanced/posts/')
def advanced():
   
    title = 'Advanced Blender tutorials'

    posts = BlogPost.get_all_posts()

    return render_template('promotion.html', title = title, pitches= pitches )


@main.route('/python/posts/')
def python():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Using Python in Blender'
    posts = BlogPost.get_all_posts()
    return render_template('businessIdeas.html', title = title, pitches= pitches )
 
#  end of category root functions

@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

  
    found_pitch= get_pitch(pitch_id)
    title = pitch_id
    pitch_comments = Comment.get_comments(pitch_id)

    return render_template('pitch.html',title= title ,found_pitch= found_pitch, pitch_comments= pitch_comments)

@main.route('/search/<pitch_name>')
def search(pitch_name):
  
    searched_pitches = search_pitch(pitch_name)
    title = 'search results for {}'.format(pitch_name)

    return render_template('search.html',pitches = searched_pitches)



@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_post():
  
    form = PostForm()
    if category is None:
        abort( 404 )

    if form.validate_on_submit():
        pitch= form.content.data
        category_id = form.category_id.data
        new_post= Pitch(pitch= pitch, category_id = category_id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form= form, category= category)

@main.route('/category/<int:id>')
def category(id):
  
    category = PitchCategory.query.get(id)

    if category is None:
        abort(404)

    pitches_in_category = Pitches.get_pitch(id)
    return render_template('category.html' ,category= category, pitches= pitches_in_category)




@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = 'photos/{}'.format(filename)
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    admin = Admin.query.filter_by(username = uname).first()

    if user is None:
        return render_template('fourOwFour.html1')

    return render_template("profile/profile.html", user = user)

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







@main.route('/test/<int:id>')  
def test(id):
    '''
    this is route for basic testing
    '''
    pitch =Pitch.query.filter_by(id=1).first()
    return render_template('test.html',pitch= pitch)

