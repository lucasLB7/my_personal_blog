from app import create_app, db
from flask_script import Manager,Server
from app.models import Role ,PostCategory, Comment, BlogPost,Subscriber,Admin
from  flask_migrate import Migrate, MigrateCommand

 
app = create_app('development')  


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Admin = Admin, BlogPost = BlogPost, Role = Role, Comment = Comment,Subscriber= Subscriber,PostCategory=PostCategory ) 

if __name__ == '__main__':
    manager.run()