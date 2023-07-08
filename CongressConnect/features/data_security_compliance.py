```python
import os
from cryptography.fernet import Fernet
from flask_login import UserMixin, current_user
from flask_principal import RoleNeed, Permission
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

from CongressConnect.database_development import db, UserSchema, RoleSchema

# Define models for User and Role
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    if not User.query.first():
        user_datastore.create_user(email='test@test.com', password='password')
        db.session.commit()

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

# Role-based access control
@app.route('/admin')
@login_required
@roles_required('admin')
def admin_home():
    return render_template('admin_home.html')

# Data encryption
def generate_key():
    return Fernet.generate_key()

def encrypt_message(message):
    key = generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message)
    return cipher_text

def decrypt_message(cipher_text):
    key = generate_key()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return plain_text
```