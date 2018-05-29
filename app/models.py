from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 



@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

class Admin(UserMixin, db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True) 
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    post = db.relationship('BlogPost',backref = 'admins',lazy="dynamic")

    def save_admin(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        reviews = Comment.query.filter_by(post_id=id).all()
        return comments
    @classmethod
    def delete_comments(cls,id):
        pass


    @property
    def password(self):
        raise AttributeError('Looks like you cant see this')

        

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'Admin {}'.format(self.username)

class Subscriber(UserMixin,db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)

    def __repr__(self):
        return 'Subscriber {}'.format(self.email)        
    

class BlogPost(db.Model):
    '''
    Post class to define BlogPost Objects
    '''
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    post_title = db.Column(db.String)
    description = db.Column(db.String)
    post = db.Column(db.String)
    category_id = db.Column(db.Integer)
    admin_id = db.Column(db.Integer,db.ForeignKey("admins.id"))
    comments = db.relationship('Comment',backref = 'posts',lazy="dynamic")

        

    def save_post(self):
        '''
        Function that saves posts
        '''
        db.session.add(self)
        db.session.commit()

   
    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    
    @classmethod
    def get_all_posts(cls):
        '''
        Function that queries the databse and returns all the posts
        '''
        return BlogPost.query.all()

    @classmethod
    def get_posts_by_category(cls,cat_id):
        '''
        Function that queries the databse and returns posts based on the
        category passed to it
        '''
        return BlogPost.query.filter_by(category_id = cat_id)




class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    username =  db.Column(db.String)
    votes= db.Column(db.Integer)
    

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comment.clear()

    @classmethod
    def get_comments(cls):
        comments = Comment.query.all()

        return comments

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    admins = db.relationship('Admin',backref = 'role',lazy="dynamic") 

    def __repr__(self):
        return 'Admin {}'.format(self.name)  


class PostCategory(db.Model):
    '''
    Function that defines different categories of posts
    '''
    __tablename__ ='post_categories'


    id = db.Column(db.Integer, primary_key=True)
    name_of_category = db.Column(db.String(255))
    category_description = db.Column(db.String(255))

    @classmethod
    def get_categories(cls):
        '''
        This function fetches all the categories from the database
        '''
        categories = PostCategory.query.all()
        return categories
