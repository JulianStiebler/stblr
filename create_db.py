# Need to import app and our database object aswell as
# every table-model we want to be created
from flaskapp import app, db
from flaskapp.models import User, Post
from datetime import datetime

# create application context and db
app.app_context().push()
db.create_all()

# provide basic user entry's
user_1 = User(username='Admin', email='123@stblr.com', password='password')
user_2 = User(username='Moderator', email='123@test.com', password='password')
db.session.add(user_1)
db.session.commit()

# Select Admin user and assign dummy post data
user = User.query.filter_by(username='Admin').first()
post_1 = Post(title='Blog Title 1', content='Content of first test entry', user_id=user.id)
post_2 = Post(title='Blog Title 2', content='Content of second test entry', user_id=user.id)
db.session.add(post_1, post_2)
db.session.commit()
